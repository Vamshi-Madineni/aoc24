INPUT_FILE = 'inputs/input141.txt'

# Load input data from file
def load_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

# Parse robots' data from the input lines
def parse_robots(lines):
    robots = []
    for line in lines:
        line = line.split()
        y, x = map(int, line[0][2:].split(','))
        vy, vx = map(int, line[1][2:].split(','))
        robots.append([y, x, vy, vx])
    return robots

# Step function to move robots based on time and their velocity
def step(pos, vel, t, width, height):
    y, x = pos
    dy, dx = vel

    x += (dx * t)
    y += (dy * t)

    x %= width
    y %= height

    return x, y

# Part 1: Calculate result based on robots' movements in quadrants
def part1(robots, width, height):
    result = 1
    quadrants = [0] * 4

    for i, j in (step(robot[:2], robot[2:], 100, width, height) for robot in robots):
        half_width = (width >> 1) + 1
        half_height = (height >> 1) + 1

        x, rx = divmod(i, half_width)
        y, ry = divmod(j, half_height)

        if rx == half_width - 1 or ry == half_height - 1:
            continue

        quadrants[x * 2 + y] += 1

    for quadrant in quadrants:
        result *= quadrant

    print(result)

# Function to draw the grid with robots' positions
def draw(curr, width, height):
    print()
    grid = [['.'] * height for _ in range(width)]
    for i, j in curr:
        grid[i][j] = '#'


# Part 2: Find the time when no two robots are in the same position
def part2(robots, width, height):
    t = 1
    while True:
        cur = {step(robot[:2], robot[2:], t, width, height) for robot in robots}
        if len(cur) == len(robots):
            print(t)
            draw(cur, width, height)
            break
        t += 1

# Main function to orchestrate the solution
def main():
    INPUT_FILE = 'inputs/input141.txt'
    WIDTH, HEIGHT = 103, 101

    lines = load_input(INPUT_FILE)
    robots = parse_robots(lines)

    part1(robots, WIDTH, HEIGHT)
    part2(robots, WIDTH, HEIGHT)

if __name__ == '__main__':
    main()
