# Input file path
INPUT_FILE = 'inputs/input101.txt'

# Load the grid from the input file
def load_grid(file_path):
    with open(file_path, 'r') as file:
        return [[int(x) if x.isdigit() else -1 for x in line] for line in file.read().splitlines()]

# Find all trailheads (positions with value 0) in the grid
def find_trailheads(grid):
    return [(x, y) for x, row in enumerate(grid) for y, value in enumerate(row) if value == 0]

# Get valid moves from the current position in the grid
def find_valid_moves(x, y, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    return [
        (x + dx, y + dy)
        for dx, dy in directions
        if 0 <= x + dx < rows and 0 <= y + dy < cols
    ]

# Find all reachable positions with a value of 9 starting from a trailhead
def find_reachable_nines(start_x, start_y, grid):
    from collections import deque

    visited = set()
    reachable_nines = set()
    queue = deque([(start_x, start_y, 0)])  # BFS queue

    while queue:
        x, y, height = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue

        for next_x, next_y in find_valid_moves(x, y, grid):
            if grid[next_x][next_y] == height + 1:
                queue.append((next_x, next_y, grid[next_x][next_y]))

    return reachable_nines

# Calculate the path rating using DFS
def calculate_rating(start_x, start_y, grid):
    visited = set()
    path_count = 0

    def dfs(x, y, height):
        nonlocal path_count
        if grid[x][y] == 9:
            path_count += 1
            return

        visited.add((x, y))
        for next_x, next_y in find_valid_moves(x, y, grid):
            if (next_x, next_y) not in visited and grid[next_x][next_y] == height + 1:
                dfs(next_x, next_y, grid[next_x][next_y])
        visited.remove((x, y))

    dfs(start_x, start_y, 0)
    return path_count

# Part 1: Sum of reachable positions with value 9 for all trailheads
def part1(grid):
    result = sum(len(find_reachable_nines(x, y, grid)) for x, y in find_trailheads(grid))
    print(result)

# Part 2: Sum of path ratings for all trailheads
def part2(grid):
    result = sum(calculate_rating(x, y, grid) for x, y in find_trailheads(grid))
    print(result)

# Main function to orchestrate the solution
def main():
    grid = load_grid(INPUT_FILE)
    part1(grid)
    part2(grid)

if __name__ == '__main__':
    main()
