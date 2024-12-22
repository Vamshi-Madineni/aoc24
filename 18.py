INPUT_FILE = 'inputs/input181.txt'

# Load the input data
def load_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [tuple(map(int, line.strip().split(','))) for line in lines]

BYTES_IN = load_input(INPUT_FILE)

# Helper functions for BFS
def adjs(x, y):
    """Returns the 4 neighboring coordinates of (x, y)."""
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def is_valid(x, y, size, obstacles):
    """Checks if a given position is within bounds and not an obstacle."""
    return 0 <= x <= size and 0 <= y <= size and (x, y) not in obstacles

# BFS function to find the shortest path from start to end
def bfs(obstacles, start, end, size):
    """Performs BFS to find the shortest path from start to end, avoiding obstacles."""
    dist = {start: 0}
    queue = [start]
    
    while queue:
        x, y = queue.pop(0)
        
        for nx, ny in adjs(x, y):
            if is_valid(nx, ny, size, obstacles) and (nx, ny) not in dist:
                dist[(nx, ny)] = dist[(x, y)] + 1
                queue.append((nx, ny))
                
                if (nx, ny) == end:
                    return dist[end]
    
    return float('inf')

# Part 1: Find the shortest path in the map
def part1():
    size = max(max(x, y) for x, y in BYTES_IN)  # Find the map size based on input
    obstacles = set(BYTES_IN[:1024])  # First 1024 positions are obstacles
    result = bfs(obstacles, (0, 0), (size, size), size)

    print(result)

# Part 2: Find the first obstacle that, when removed, allows a path to the end
def part2():
    size = max(max(x, y) for x, y in BYTES_IN)  # Find the map size based on input
    result = None
    
    obstacles = set()
    for (x, y) in BYTES_IN:
        obstacles.add((x, y))  # Add obstacle to the set
        
        # Check if removing this obstacle allows a valid path to the end
        if bfs(obstacles, (0, 0), (size, size), size) == float('inf'):
            result = (x, y)
            break

    print(result)

# Main function to execute the solution
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
