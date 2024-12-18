from collections import deque, defaultdict
from math import inf

input = 'input.txt'

MEM_SIZE = 70
NUM_OF_BYTES = 1024
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

falling_bytes = deque()
memory_space = {}

with open(input) as f:
    for line in f:
        line = line.strip()
        x, y = map(int, line.split(','))
        falling_bytes.append((x, y))

def create_memory_space(mem_size = 70):
    for y in range(mem_size + 1):
        for x in range(mem_size + 1):
            memory_space[(x, y)] = '.'

def simulate_falling_bytes(num_of_bytes):
    for _ in range(num_of_bytes):
        x, y = falling_bytes.popleft()
        memory_space[(x, y)] = '#'

def print_memory_space(mem_size = 6):
    for y in range(mem_size + 1):
        for x in range(mem_size + 1):
            print(memory_space[(x, y)], end = '')
        print()

def find_shortest_path(start=(0, 0), end=(MEM_SIZE, MEM_SIZE)):
    if memory_space[start] == '#' or memory_space[end] == '#':
        raise ValueError("Start or end point is corrupted.")
    
    distance = {key: inf for key in memory_space}
    distance[start] = 0
    visited = set()
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x <= MEM_SIZE and 0 <= new_y <= MEM_SIZE and 
                memory_space[(new_x, new_y)] == '.' and (new_x, new_y) not in visited):
                visited.add((new_x, new_y))
                distance[(new_x, new_y)] = distance[(x, y)] + 1
                queue.append((new_x, new_y))
        
    return distance.get(end, inf)        

create_memory_space(mem_size = MEM_SIZE)
simulate_falling_bytes(NUM_OF_BYTES)
print_memory_space(mem_size = MEM_SIZE)
print(find_shortest_path())
    
             