import math
from collections import deque

INPUT_FILE = 'inputs/input161.txt'

MOVES = {
    "^": ([">", "<"], (-1, 0)),
    ">": (["v", "^"], (0, 1)),
    "v": (["<", ">"], (1, 0)),
    "<": (["^", "v"], (0, -1))
}

# Load map from file
def load_map(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

# Get start and end positions from the map
def get_start_end(map):
    start = end = (0, 0)
    for idx, row in enumerate(map):
        for idy, cell in enumerate(row):
            if cell == 'S':
                start = (idx, idy)
            elif cell == 'E':
                end = (idx, idy)

    return start, end

# Part 1: Perform BFS to find the shortest path to the end
def part1(map):
    start, end = get_start_end(map)

    # Initialize values table to track distances
    values = [
        [
            {d: math.inf for d in ">v<^"} for _ in row
        ] for row in map
    ]
    q = deque([(*start, ">", 0)])

    while q:
        i, j, d, p = q.popleft()
        if i < 0 or i >= len(map) or j < 0 or j >= len(map[i]):
            continue

        if map[i][j] == '#':
            continue

        if values[i][j][d] <= p:
            continue

        values[i][j][d] = p
        if (i, j) == end:
            continue

        opt, delta = MOVES[d]
        q.append((i + delta[0], j + delta[1], d, p + 1))
        for x in opt:
            q.append((i, j, x, p + 1000))

    score = values[end[0]][end[1]]

    result = math.inf
    for _, v in score.items():
        result = min(result, v)

    print(result)

# Part 2: Find the shortest path considering a set of paths and revisits
def part2(map):
    start, end = get_start_end(map)
    
    # Initialize values table with path tracking
    values = [
        [
            {d: (math.inf, set()) for d in ">v<^"} for _ in row
        ] for row in map
    ]
    
    q = deque([(*start, ">", 0, set([start]))])

    while q:
        i, j, d, p, path = q.popleft()
        if i < 0 or i >= len(map) or j < 0 or j >= len(map[i]):
            continue

        if map[i][j] == '#':
            continue

        path.add((i, j))
        currentMin, currentPath = values[i][j][d]
        if currentMin < p:
            continue
        elif currentMin == p:
            currentPath.update(path)
        else:
            currentPath.clear()
            currentPath.update(path)
            values[i][j][d] = (p, currentPath)

        if (i, j) == end:
            continue

        opt, delta = MOVES[d]
        q.append((i + delta[0], j + delta[1], d, p + 1, set(path)))
        for x in opt:
            q.append((i, j, x, p + 1000, set(path)))

    score = values[end[0]][end[1]]

    result = 0
    minscore = math.inf
    for _, v in score.items():
        s, path = v
        if s < minscore:
            result = len(path)
            minscore = s

    print(result)

# Main function to orchestrate the solution
def main():
    map = load_map(INPUT_FILE)
    part1(map)
    part2(map)

if __name__ == '__main__':
    main()
