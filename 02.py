# Input file path
INPUT_FILE = 'inputs/input21.txt'

# Function to read and parse levels from the input file
def read_levels(file_path):
    levels = []
    with open(file_path, 'r') as file:
        for line in file:
            level = list(map(int, line.strip().split(' ')))
            levels.append(level)
    return levels

# Helper functions for condition checks
def is_positive(number):
    return number > 0

def is_negative(number):
    return number < 0

def fits_range(value, min_val, max_val):
    return min_val <= abs(value) <= max_val

# Check if a level is safe based on its differences
def is_level_safe(differences):
    if 0 in differences:
        return False
    if all(is_positive(diff) for diff in differences) or all(is_negative(diff) for diff in differences):
        if all(fits_range(diff, 1, 3) for diff in differences):
            return True
    return False

# Calculate differences between consecutive levels
def calculate_differences(level):
    return [level[i] - level[i + 1] for i in range(len(level) - 1)]

# Part 1 solution: Count safe levels
def part1(levels):
    safe_count = sum(1 for level in levels if is_level_safe(calculate_differences(level)))
    print(safe_count)

# Check if removing a single problem point makes the level safe
def check_with_removed_element(level, index):
    modified_level = level[:index] + level[index + 1:]
    return is_level_safe(calculate_differences(modified_level))

# Part 2 solution: Count safe levels with a problem dampener
def part2(levels):
    safe_count = 0
    for level in levels:
        differences = calculate_differences(level)
        if is_level_safe(differences):
            safe_count += 1
        else:
            for i in range(len(level)):
                if check_with_removed_element(level, i):
                    safe_count += 1
                    break
    print(safe_count)

# Main function
def main():
    levels = read_levels(INPUT_FILE)
    part1(levels)
    part2(levels)

if __name__ == '__main__':
    main()
