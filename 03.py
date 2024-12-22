import re

# Input file path
INPUT_FILE = 'inputs/input31.txt'

# Function to read and preprocess input lines
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to calculate the product from a string in "mul(a,b)" format
def parse_multiplication(expression):
    a, b = map(int, expression[4:-1].split(','))
    return a * b

# Part 1 solution: Calculate the sum of all "mul(a,b)" expressions
def part1(lines):
    total_sum = 0
    multiplication_pattern = re.compile(r"mul\(\d+,\d+\)")
    
    for line in lines:
        for match in multiplication_pattern.findall(line):
            total_sum += parse_multiplication(match)
    
    print(total_sum)

# Part 2 solution: Calculate the sum of "mul(a,b)" expressions with conditions
def part2(lines):
    total_sum = 0
    is_active = True
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

    for line in lines:
        for match in pattern.findall(line):
            if match == "do()":
                is_active = True
            elif match == "don't()":
                is_active = False
            elif is_active:
                total_sum += parse_multiplication(match)

    print(total_sum)

# Main function
def main():
    lines = read_input(INPUT_FILE)
    part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()
