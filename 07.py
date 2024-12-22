from itertools import product

# File path to the input data
INPUT_FILE = 'inputs/input71.txt'

# Function to load data from the input file
def load_data(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        for line in file:
            target, numbers = line.split(":")
            target_value = int(target)
            number_list = list(map(int, numbers.split()))
            dataset.append((target_value, number_list))
    return dataset

# Evaluate an expression for Part 1 using the provided operators
def evaluate_expression(nums, ops, advanced=False):
    def concatenate(a, b):
        return int(f"{a}{b}")

    result = nums[0]
    for idx, op in enumerate(ops):
        if op == '+':
            result += nums[idx + 1]
        elif op == '*':
            result *= nums[idx + 1]
        elif advanced and op == '||':
            result = concatenate(result, nums[idx + 1])
    return result

# Check if a target can be achieved using valid operations for Part 1
def is_valid_expression(target, nums, advanced=False):
    operator_set = ['+', '*', '||'] if advanced else ['+', '*']
    num_operators = len(nums) - 1

    for ops in product(operator_set, repeat=num_operators):
        if evaluate_expression(nums, ops, advanced) == target:
            return True
    return False

# Part 1: Solve for basic operations (+, *)
def part1(data):
    result = sum(target for target, nums in data if is_valid_expression(target, nums))
    print(result)

# Part 2: Solve for advanced operations (+, *, ||)
def part2(data):
    result = sum(target for target, nums in data if is_valid_expression(target, nums, advanced=True))
    print(result)

# Main function to execute both parts
def main():
    data = load_data(INPUT_FILE)
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()
