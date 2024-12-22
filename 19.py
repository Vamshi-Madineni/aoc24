from functools import cache

INPUT_FILE = 'inputs/input191.txt'

# Load the input data
def load_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

lines = load_input(INPUT_FILE)

# Split the input data into patterns and designs
index = lines.index('')
PATTERNS = lines[:index][0].split(', ')
DESIGNS = lines[index + 1:]

# Cache the valid design check to improve efficiency
@cache
def is_valid(design):
    """Checks if the given design can be created using the available patterns."""
    if not design:
        return True

    for pattern in PATTERNS:
        if design.startswith(pattern):
            if is_valid(design[len(pattern):]):
                return True

    return False

def part1():
    """Count the number of valid designs using the available patterns."""
    result = sum(1 for design in DESIGNS if is_valid(design))
    print(result)

# Cache the count of ways to form a design to avoid redundant calculations
@cache
def count_ways(design):
    """Counts the number of ways to form a design using the available patterns."""
    if not design:
        return 1

    total = 0
    for pattern in PATTERNS:
        if design.startswith(pattern):
            total += count_ways(design[len(pattern):])

    return total

def part2():
    """Count the total number of ways to form all designs using the available patterns."""
    result = sum(count_ways(design) for design in DESIGNS)
    print(result)

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
