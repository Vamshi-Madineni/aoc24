# Input file path
INPUT_FILE = 'inputs/input81.txt'

# Load the grid and extract antenna positions
def load_grid(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
    rows, cols = len(lines), len(lines[0])

    antennas = [
        (row, col, char)
        for row, line in enumerate(lines)
        for col, char in enumerate(line)
        if char != '.'
    ]

    return lines, rows, cols, antennas

# Part 1: Count unique antinodes based on antenna frequencies
def count_unique_antinodes(antennas, rows, cols, extend=False):
    antinodes = set()

    for idx1, (x1, y1, freq1) in enumerate(antennas):
        for idx2, (x2, y2, freq2) in enumerate(antennas):
            if freq1 != freq2:  # Only compare antennas with the same frequency
                continue

            dx, dy = x2 - x1, y2 - y1
            if dx == 0 and dy == 0:
                continue

            ax, ay = x2, y2
            while 0 <= ax < rows and 0 <= ay < cols:
                if not extend:
                    antinodes.add((ax + dx, ay + dy))
                    break
                antinodes.add((ax, ay))
                ax += dx
                ay += dy

    return len(antinodes)

# Part 1: Solve for basic antinode computation
def part1(antennas, rows, cols):
    result = count_unique_antinodes(antennas, rows, cols, extend=False)
    print(result)

# Part 2: Solve for extended antinode propagation
def part2(antennas, rows, cols):
    result = count_unique_antinodes(antennas, rows, cols, extend=True)
    print(result)

# Main function to orchestrate the solution
def main():
    grid, rows, cols, antennas = load_grid(INPUT_FILE)
    part1(antennas, rows, cols)
    part2(antennas, rows, cols)

if __name__ == '__main__':
    main()
