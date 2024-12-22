from collections import defaultdict

# Input file path
INPUT_FILE = 'inputs/input111.txt'

# Load and preprocess the input lines
def load_lines(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]

# Parse the initial stones into a dictionary with counts
def parse_stones(lines):
    stones = defaultdict(int)
    for stone in map(int, lines[0].split()):
        stones[stone] += 1
    return stones

# Transform a stone according to the specified rules
def transform(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        n = len(str(stone)) // 2
        return [int(str(stone)[:n]), int(str(stone)[n:])]
    else:
        return [stone * 2024]

# Perform a "blink" operation to transform all stones
def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        for new_stone in transform(stone):
            new_stones[new_stone] += count
    return new_stones

# Part 1: Simulate 25 blinks and count all stones
def part1(stones):
    for _ in range(25):
        stones = blink(stones)
    print(sum(stones.values()))

# Part 2: Simulate 75 blinks and count all stones
def part2(stones):
    for _ in range(75):
        stones = blink(stones)
    print(sum(stones.values()))

# Main function to orchestrate the solution
def main():
    lines = load_lines(INPUT_FILE)
    stones = parse_stones(lines)
    part1(stones)
    stones = parse_stones(lines)  # Reload stones for part 2
    part2(stones)

if __name__ == '__main__':
    main()
