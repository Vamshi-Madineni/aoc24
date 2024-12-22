from itertools import product
from functools import cache

INPUT_FILE = 'inputs/input211.txt'

# Define the numeric and directional keypad keys
NUMERIC = "789456123 0A"
DIRECTIONAL = " ^A<v>"

# Load the codes from the input file
def load_codes(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

CODES = load_codes(INPUT_FILE)

@cache
def paths(keymap):
    """
    Precomputes all paths between pairs of keys on the keypad.
    The keymap is a string representing the keys, where ' ' represents an invalid position.
    Returns a dictionary of paths between each pair of keys.
    """
    # Map key positions on the grid
    locations = {
        c: (x, y)
        for y, row in enumerate(keymap[i:i + 3] for i in range(0, len(keymap), 3))
        for x, c in enumerate(row)
    }

    pathmap = {}

    # Compute the path for each pair of keys
    for a, b in product((c for c in keymap if c != ' '), repeat=2):
        if a == b:
            pathmap[a, b] = ['']  # No movement needed if keys are the same
            continue

        (ax, ay), (bx, by) = locations[a], locations[b]
        dx, dy = bx - ax, by - ay

        # Generate movement directions for x and y
        moves_x = '>' * max(0, dx) + '<' * max(0, -dx)
        moves_y = 'v' * max(0, dy) + '^' * max(0, -dy)

        # Handle the movement if there's a gap
        if dx == 0 or dy == 0 or locations[' '] not in [(bx, ay), (ax, by)]:
            pathmap[a, b] = [moves_x + moves_y, moves_y + moves_x]
        elif locations[' '] == (bx, ay):
            pathmap[a, b] = [moves_y + moves_x]
        else:
            pathmap[a, b] = [moves_x + moves_y]

    return pathmap


@cache
def presses(code, depth, keypad=NUMERIC):
    """
    Recursively computes the minimum number of button presses for a given code with the specified number of robots.
    `depth` refers to the number of robots.
    """
    if depth == 1:
        return len(code)  # Only one robot, number of presses is the length of the code

    keypaths = paths(keypad)
    total_presses = 0

    for pair in zip('A' + code, code):
        # For each pair of consecutive keys, calculate the minimum presses needed
        total_presses += min(
            presses(path + 'A', depth - 1, DIRECTIONAL)
            for path in keypaths[pair]
        )

    return total_presses


def part1():
    """
    Part 1: Calculate the total complexity for 2 robots.
    The complexity is calculated by multiplying the number of presses by the numeric value of the code (excluding the last digit).
    """
    result = 0
    for code in CODES:
        complexity = presses(code, 4) * int(code[:-1])
        result += complexity

    print(f"Part 1 result: {result}")


def part2():
    """
    Part 2: Calculate the total complexity for 25 robots.
    This is similar to part 1 but with more robots involved.
    """
    result = 0
    for code in CODES:
        complexity = presses(code, 27) * int(code[:-1])
        result += complexity

    print(f"Part 2 result: {result}")


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
