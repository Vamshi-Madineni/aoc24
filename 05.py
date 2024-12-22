from collections import defaultdict

# Input file path
INPUT_FILE = 'inputs/input51.txt'

# Function to parse the input file
def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    split_index = lines.index('')
    rule_lines = lines[:split_index]
    update_lines = lines[split_index + 1:]

    rules = defaultdict(list)
    for rule in rule_lines:
        key, value = rule.split('|')
        rules[key].append(value)

    updates = [update.split(',') for update in update_lines]

    return rules, updates

# Get the middle element of a list
def get_middle_element(update):
    return update[len(update) // 2]

# Validate whether an update follows the rules
def is_valid_update(update, rules):
    for idx, page in enumerate(update):
        for element in rules[page]:
            if element in update[:idx]:
                return False
    return True

# Swap elements in the update list to resolve conflicts
def swap_elements(update, element, page):
    idx = update.index(element)
    page_idx = update.index(page)
    update[idx], update[page_idx] = update[page_idx], update[idx]
    return update

# Recursively fix an update to make it valid
def fix_update(update, rules):
    if is_valid_update(update, rules):
        return update

    for idx, page in enumerate(update):
        for element in rules[page]:
            if element in update[:idx]:
                update = swap_elements(update, element, page)

    return fix_update(update, rules)

# Part 1: Calculate the sum of middle elements for valid updates
def part1(rules, updates):
    total = 0
    for update in updates:
        if is_valid_update(update, rules):
            total += int(get_middle_element(update))
    print(total)

# Part 2: Fix invalid updates and calculate the sum of middle elements
def part2(rules, updates):
    total = 0
    for update in updates:
        if not is_valid_update(update, rules):
            update = fix_update(update, rules)
        total += int(get_middle_element(update))
    print(total)

# Main function to run the program
def main():
    rules, updates = parse_input(INPUT_FILE)
    part1(rules, updates)
    part2(rules, updates)

if __name__ == '__main__':
    main()
