import re

# Load input data from file
def load_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Extract values using regex patterns
def extract_values(lines, pattern):
    return [(int(m.group(1)), int(m.group(2))) 
            for line in lines 
            if (m := re.search(pattern, line))]

# Solve the equation for a given set of coordinates
def solve(ax, ay, bx, by, x, y):
    # matrix representation of the system of equations
    mat_div = ax * by - bx * ay
    na, ra = divmod(by * x - bx * y, mat_div)
    nb, rb = divmod(ax * y - ay * x, mat_div)

    if na >= ra == 0 == rb <= nb:
        return (na, nb)

    return None

# Calculate the total tokens for a given set of button coordinates
def calculate_tokens(buttons):
    tokens = 0
    for button in buttons:
        a, b = button
        tokens += ((a * 3) + (b * 1))
    return tokens

# Part 1: Solve the equations without any adjustments
def part1(A, B, PRIZE):
    tokens = 0
    buttons = []

    for (ax, ay), (bx, by), (x, y) in zip(A, B, PRIZE):
        solution = solve(ax, ay, bx, by, x, y)
        if solution:
            buttons.append(solution)

    tokens = calculate_tokens(buttons)
    print(tokens)

# Part 2: Solve the equations with large adjustments to x and y values
def part2(A, B, PRIZE):
    tokens = 0
    buttons = []

    for (ax, ay), (bx, by), (x, y) in zip(A, B, PRIZE):
        x += 10000000000000
        y += 10000000000000
        solution = solve(ax, ay, bx, by, x, y)
        if solution:
            buttons.append(solution)

    tokens = calculate_tokens(buttons)
    print(tokens)

# Main function to orchestrate the solution
def main():
    INPUT_FILE = 'inputs/input131.txt'
    lines = load_input(INPUT_FILE)

    # Extract button and prize coordinates using regex
    A = extract_values(lines, r'Button A: X\+(\d+), Y\+(\d+)')
    B = extract_values(lines, r'Button B: X\+(\d+), Y\+(\d+)')
    PRIZE = extract_values(lines, r'Prize: X=(\d+), Y=(\d+)')

    # Execute both parts
    part1(A, B, PRIZE)
    part2(A, B, PRIZE)

if __name__ == '__main__':
    main()
