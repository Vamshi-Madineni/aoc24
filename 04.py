# Input file path
INPUT_FILE = 'inputs/input41.txt'

# Function to read the grid from the input file
def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

# Utility function to check if coordinates are within the grid bounds
def is_valid_coordinate(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

# Check if a given text matches "XMAS" or its reverse
def is_xmas(text):
    return text == 'XMAS' or text[::-1] == 'XMAS'

# Check if a given text matches the custom patterns in part2
def is_x_mas_pattern(text):
    return text in {"MMSS", "SSMM", "MSMS", "SMSM"}

# Part 1: Count occurrences of "XMAS" horizontally, vertically, and diagonally
def part1(grid):
    rows, cols = len(grid), len(grid[0])
    xmas_count = 0

    for x in range(rows):
        for y in range(cols):
            # Check horizontal (rightward)
            if is_valid_coordinate(x + 3, y, rows, cols):
                text = ''.join(grid[x + i][y] for i in range(4))
                if is_xmas(text):
                    xmas_count += 1

            # Check vertical (downward)
            if is_valid_coordinate(x, y + 3, rows, cols):
                text = ''.join(grid[x][y + i] for i in range(4))
                if is_xmas(text):
                    xmas_count += 1

            # Check diagonal (bottom-right)
            if is_valid_coordinate(x + 3, y + 3, rows, cols):
                text = ''.join(grid[x + i][y + i] for i in range(4))
                if is_xmas(text):
                    xmas_count += 1

            # Check diagonal (bottom-left)
            if is_valid_coordinate(x + 3, y - 3, rows, cols):
                text = ''.join(grid[x + i][y - i] for i in range(4))
                if is_xmas(text):
                    xmas_count += 1

    print(xmas_count)

# Part 2: Count occurrences of "A" surrounded by specific patterns
def part2(grid):
    rows, cols = len(grid), len(grid[0])
    pattern_count = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] == 'A':
                surrounding_text = (
                    grid[x - 1][y - 1] +
                    grid[x - 1][y + 1] +
                    grid[x + 1][y - 1] +
                    grid[x + 1][y + 1]
                )
                if is_x_mas_pattern(surrounding_text):
                    pattern_count += 1

    print(pattern_count)

# Main function to execute the parts
def main():
    grid = read_grid(INPUT_FILE)
    part1(grid)
    part2(grid)

if __name__ == '__main__':
    main()
