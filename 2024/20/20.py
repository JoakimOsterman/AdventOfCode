from collections import deque, defaultdict, Counter
from tqdm import tqdm

input_file = 'input.txt'
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

grid_map = {}
with open(input_file, 'r') as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid_map[(x, y)] = char

def find_start(grid_map):
    for key, value in grid_map.items():
        if value == 'S':
            return key
    raise ValueError('No start found')

def find_end(grid_map):
    for key, value in grid_map.items():
        if value == 'E':
            return key
    raise ValueError('No end found')

def djikstra(grid_map, start, end):
    visited = set()
    parent = {}
    queue = deque([(start, 0)])
    parent[start] = None
    min_cost = defaultdict(lambda: float('inf'))
    min_cost[start] = 0

    while queue:
        current, distance = queue.popleft()
        
        if current in visited:
            continue
        visited.add(current)
        
        if current == end:
            return distance, parent, min_cost
        
        for dx, dy in DIRECTIONS:
            new_x, new_y = current[0] + dx, current[1] + dy
            new_pos = (new_x, new_y)
            if grid_map.get(new_pos) is not None and grid_map[new_pos] != '#':
                new_distance = distance + 1
                if new_distance < min_cost[new_pos]:
                    min_cost[new_pos] = new_distance
                    parent[new_pos] = current
                    queue.append((new_pos, new_distance))

    raise ValueError('No path found')

def print_path(grid_map, parent, start, end):
    current = end
    path = []
    while current != start:
        path.append(current)
        grid_map[current] = 'X'
        current = parent[current]
    if current == start:
        path.append(current)

    grid_map[start] = 'S'
    grid_map[end] = 'E'
    path.reverse()

    return path     

def print_map(grid_map):
    for y, x in sorted(grid_map.keys(), key=lambda x: (x[1], x[0])):
        print(grid_map[(y, x)], end='')
    print()

def find_every_possible_cheat(grid_map, start, end, optimal_path, optimal_distance, min_cost, part = 1):
    if part == 2:
        picoseconds = 20
    else:
        picoseconds = 2

    dist_from_nodes = {}
    dist_from_nodes[start] = min_cost[end]
    dist_from_nodes[end] = 0
    for idx, node in enumerate(optimal_path):
        if idx == 0:
            assert node == start
            prev_distance = min_cost[end]
            continue
        dist_from_nodes[node] = prev_distance - 1
        prev_distance -= 1

    cheats = {}
    
    # Find all possible cheats
    for node in tqdm(optimal_path):
        visited_cheat_path = set()
        visited_cheat_path.add(node)
        queue = deque([(node, 0)])

        while queue:
            current, distance = queue.popleft()
            if distance >= picoseconds:
                continue

            for dx, dy in DIRECTIONS:
                new_x, new_y = current[0] + dx, current[1] + dy
                new_pos = (new_x, new_y)
                if grid_map.get(new_pos) is not None and new_pos not in visited_cheat_path:
                    visited_cheat_path.add(new_pos)
                    queue.append((new_pos, distance + 1))
                    if new_pos in optimal_path:
                        cheat_cost = min_cost[node] + distance + 1 + dist_from_nodes[new_pos]
                        if cheat_cost < optimal_distance and (node, new_pos) not in cheats:
                            cheats[(node, new_pos)] = optimal_distance - (cheat_cost)
                        if (node, new_pos) in cheats and cheat_cost < cheats[(node, new_pos)] and cheat_cost < optimal_distance:
                            cheats[(node, new_pos)] = optimal_distance - (cheat_cost)
    return cheats


start, end = find_start(grid_map), find_end(grid_map)
dist, parent, min_cost = djikstra(grid_map, start, end)
print(f"Distance: {dist}")
path = print_path(grid_map, parent, start, end)

cheats = find_every_possible_cheat(grid_map, start, end, path, dist, min_cost)
counter_cheat = Counter(cheats.values())
print(f"Part1: Sum of values: {sum(value for key, value in counter_cheat.items() if key >= 100)}")

# Part 2
cheats_2 = find_every_possible_cheat(grid_map, start, end, path, dist, min_cost, part = 2)
counter_cheat_2 = Counter(cheats_2.values())
print(f"Part2: Sum of values: {sum(value for key, value in counter_cheat_2.items() if key >= 100)}")


