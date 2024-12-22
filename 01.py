from collections import Counter

# Input file path
INPUT_FILE = 'inputs/input11.txt'

# Function to read input data
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split('   ') for line in file.readlines()]

# Parse numbers from the file
def parse_numbers(lines):
    list1, list2 = [], []
    for pair in lines:
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))
    return list1, list2

# Solution for Part 1
def calculate_absolute_difference_sum(sorted_list1, sorted_list2):
    return sum(abs(a - b) for a, b in zip(sorted_list1, sorted_list2))

# Solution for Part 2
def calculate_weighted_sum(list1, list2):
    counter = Counter(list2)
    return sum(num * counter[num] for num in list1 if num in counter)

# Main function
def main():
    input_data = read_input(INPUT_FILE)
    nums1, nums2 = parse_numbers(input_data)

    # Part 1: Compute result
    part1_result = calculate_absolute_difference_sum(sorted(nums1), sorted(nums2))
    print(part1_result)

    # Part 2: Compute result
    part2_result = calculate_weighted_sum(nums1, nums2)
    print(part2_result)

if __name__ == '__main__':
    main()
