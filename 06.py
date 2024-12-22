# Input file path
INPUT_FILE = 'inputs/input61.txt'

# Read the input map from the file
def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

# Direction mappings and turning rules
DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

TURN_RIGHT = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

# Find the initial position and direction in the map
def get_initial_position(grid):
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell in DIRECTIONS:
                return (row_idx, col_idx), cell
    return None, None

# Trace the path based on the rules
def trace_path(grid):
    current_pos, current_dir = get_initial_position(grid)
    visited_positions = set()
    rows, cols = len(grid), len(grid[0])

    while current_pos:
        visited_positions.add(current_pos)
        dr, dc = DIRECTIONS[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)

        # Check bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        next_row, next_col = next_pos
        # Change direction if encountering an obstacle
        if grid[next_row][next_col] == '#':
            current_dir = TURN_RIGHT[current_dir]
        else:
            current_pos = next_pos

    return visited_positions

# Check if a path forms a cycle
def has_path_cycle(grid, start_pos, start_dir):
    seen_states = set()
    current_pos, current_dir = start_pos, start_dir

    rows, cols = len(grid), len(grid[0])

    while current_pos:
        state = (current_pos, current_dir)
        if state in seen_states:
            return True
        seen_states.add(state)

        dr, dc = DIRECTIONS[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)

        # Check bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        next_row, next_col = next_pos
        # Change direction if encountering an obstacle
        if grid[next_row][next_col] == '#':
            current_dir = TURN_RIGHT[current_dir]
        else:
            current_pos = next_pos

    return False

# Part 1: Calculate the number of unique positions visited
def part1(grid):
    visited_positions = trace_path(grid)
    print(len(visited_positions))

# Part 2: Simulate obstruction and check for cycles
def part2(grid):
    visited_positions = trace_path(grid)
    initial_pos, initial_dir = get_initial_position(grid)
    cycle_count = 0

    for obstruction in visited_positions:
        new_grid = [row[:] for row in grid]
        obstruct_row, obstruct_col = obstruction
        new_grid[obstruct_row][obstruct_col] = '#'

        if has_path_cycle(new_grid, initial_pos, initial_dir):
            cycle_count += 1

    print(cycle_count)

# Main function to execute both parts
def main():
    grid = read_map(INPUT_FILE)
    part1(grid)
    part2(grid)

if __name__ == '__main__':
    main()
