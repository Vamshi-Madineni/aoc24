INPUT_FILE = 'inputs/input201.txt'

# Load the grid from the input file
def load_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

lines = load_input(INPUT_FILE)

# Define directions for movement (right, down, left, up)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Initialize grid and find the start (S) and end (E) positions
GRID = [list(line) for line in lines]
START = END = None
for r, row in enumerate(GRID):
    for c, cell in enumerate(row):
        if cell == 'S':
            START = (r, c)
        elif cell == 'E':
            END = (r, c)

# Find the shortest path using BFS
def find_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = [(start, 0, [start])]  # (position, steps, path)
    visited.add(start)

    while queue:
        (r, c), steps, path = queue.pop(0)
        if (r, c) == end:
            return steps, path

        # Explore neighbors
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in visited:
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), steps + 1, new_path))
                visited.add((nr, nc))

# Find cheatable pairs in the path within a specified range of cheat moves
def find_cheatable_pairs_in_range(path, savings, cheat_moves):
    cheats = 0
    coords_steps = {coord: i for i, coord in enumerate(path)}

    for y, x in path:
        # Try all possible cheat moves in the range
        for dy in range(-cheat_moves, cheat_moves + 1):
            for dx in range(-cheat_moves, cheat_moves + 1):
                if dy == 0 and dx == 0:
                    continue

                manhattan = abs(dy) + abs(dx)
                if manhattan > cheat_moves:
                    continue

                ny, nx = y + dy, x + dx
                if (ny, nx) in coords_steps:
                    # Check if we can "cheat" within the savings range
                    if savings <= (coords_steps[(ny, nx)] - coords_steps[(y, x)] - manhattan):
                        cheats += 1

    return cheats

# Part 1: Calculate the number of cheatable pairs with specific savings and cheat moves
def part1():
    _, path = find_shortest_path(GRID, START, END)

    savings = 100
    cheat_moves = 2
    result = find_cheatable_pairs_in_range(path, savings, cheat_moves)

    print(f"Part 1 result: {result}")

# Part 2: Calculate the number of cheatable pairs with larger cheat moves
def part2():
    _, path = find_shortest_path(GRID, START, END)

    savings = 100
    cheat_moves = 20
    result = find_cheatable_pairs_in_range(path, savings, cheat_moves)

    print(f"Part 2 result: {result}")

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
