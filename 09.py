# Input file path
INPUT_FILE = 'inputs/input91.txt'

# Load the data from the input file
def load_data(file_path):
    with open(file_path, 'r') as file:
        return [int(c) for c in file.readline().strip()]

# Prepare the processed data based on the given rules
def prepare_data(data):
    full, free = [], []

    for i in range(len(data)):
        (full if i % 2 == 0 else free).append(i)

    processed = []
    nb_to_add = 0

    for i in range(len(full)):
        processed.extend([nb_to_add] * data[full[i]])
        if i < len(free):
            processed.extend(['.'] * data[free[i]])
        nb_to_add += 1

    return processed

# Calculate the checksum for the processed data
def calculate_checksum(processed):
    checksum = 0
    for i, value in enumerate(processed):
        if value != '.':
            checksum += i * value
    return checksum

# Part 1 logic
def part1(data):
    processed = prepare_data(data)

    while '.' in processed:
        last = processed.pop()
        if last != '.':
            dot_index = processed.index('.')
            processed[dot_index] = last

    checksum = calculate_checksum(processed)
    print(checksum)

# Extract blocks of symbols from the processed data
def extract_blocks(processed):
    blocks = []
    current_symbol, start_index, length = processed[0], 0, 0

    for i, symbol in enumerate(processed):
        if symbol == current_symbol:
            length += 1
        else:
            blocks.append((current_symbol, start_index, length))
            current_symbol, start_index, length = symbol, i, 1

    blocks.append((current_symbol, start_index, length))
    return blocks

# Compact the processed data by moving blocks
def compact_files(processed):
    blocks = extract_blocks(processed)

    for symbol, start, length in reversed(blocks):
        if symbol == '.':
            continue

        for free_symbol, free_start, free_length in blocks:
            if free_symbol == '.' and free_length >= length and free_start < start:
                processed[free_start:free_start + length] = [symbol] * length
                processed[start:start + length] = ['.'] * length
                blocks = extract_blocks(processed)
                break

    return processed

# Part 2 logic
def part2(data):
    processed = prepare_data(data)
    processed = compact_files(processed)
    checksum = calculate_checksum(processed)
    print(checksum)

# Main function to orchestrate the solution
def main():
    data = load_data(INPUT_FILE)
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()
