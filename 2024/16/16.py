from math import inf
import heapq
from collections import defaultdict

input_file = 'input.txt'

reindeer_map = {}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # E, S, W, N

with open(input_file) as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            reindeer_map[(x, y)] = char

def get_neighbors(x, y, reindeer_map):
    return [((x + dx, y + dy), reindeer_map.get((x + dx, y + dy))) for dx, dy in directions if reindeer_map.get((x + dx, y + dy)) is not None]

def find_starting_point(reindeer_map):
    for (x, y), char in reindeer_map.items():
        if char == 'S':
            return (x, y)

def find_end_point(reindeer_map):
    for (x, y), char in reindeer_map.items():
        if char == 'E':
            return (x, y)

# A modified Dijkstra's algorithm
def find_shortest_path(reindeer_map, start=None, end=None):
    if start is None:
        start = find_starting_point(reindeer_map)
    if end is None:
        end = find_end_point(reindeer_map)

    rotation_cost = 1000
    traverse_cost = 1

    # Priority queue: (cost, x, y, direction)
    pq = [(0, start[0], start[1], 'E')]
    min_cost = defaultdict(lambda: inf)
    parent = defaultdict(list)

    # Initialize starting position
    min_cost[(start[0], start[1], 'E')] = 0

    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        # Stop processing if this state is not optimal
        if cost > min_cost[(x, y, direction)]:
            continue

        # Check all directions and possible moves
        for dx, dy, new_dir in [(1, 0, 'E'), (0, 1, 'S'), (-1, 0, 'W'), (0, -1, 'N')]:
            new_x, new_y = x + dx, y + dy

            # Validate the new position
            if reindeer_map.get((new_x, new_y)) is not None and reindeer_map[(new_x, new_y)] != '#':
                new_cost = cost + traverse_cost + (rotation_cost if direction != new_dir else 0)

                # Update cost and parent if a better cost is found
                if new_cost < min_cost[(new_x, new_y, new_dir)]:
                    min_cost[(new_x, new_y, new_dir)] = new_cost
                    heapq.heappush(pq, (new_cost, new_x, new_y, new_dir))
                    parent[(new_x, new_y, new_dir)] = [(x, y, direction)]
                elif new_cost == min_cost[(new_x, new_y, new_dir)]:
                    # Track additional optimal paths
                    parent[(new_x, new_y, new_dir)].append((x, y, direction))

    optimal_cost = min(min_cost[(end[0], end[1], d)] for d in ['E', 'S', 'W', 'N'])

    # Reconstruct all optimal paths
    all_paths = []
    for direction in ['E', 'S', 'W', 'N']:
        if min_cost[(end[0], end[1], direction)] == optimal_cost:
            reconstruct_all_paths(parent, end[0], end[1], direction, all_paths, [], start)

    return all_paths, optimal_cost

def reconstruct_all_paths(parent, x, y, direction, all_paths, current_path, start):
    if (x, y) == start:
        all_paths.append(current_path[::-1])
        return

    # Backtrack using the parent dictionary
    for prev_state in parent[(x, y, direction)]:
        reconstruct_all_paths(
            parent,
            prev_state[0],
            prev_state[1],
            prev_state[2],
            all_paths,
            current_path + [(x, y, direction)],
            start
        )


def count_distinct_tiles_part_of_optimal_path(paths):
    visited = set()
    for path in paths:
        for x, y, _ in path:
            visited.add((x, y))
    return len(visited) + 1


def main():
    # Part 2
    part2_paths, part1 = find_shortest_path(reindeer_map)
    part2 = count_distinct_tiles_part_of_optimal_path(part2_paths)
    print(f"Part 1: {part1} \n \n Part 2: {part2}")

if __name__ == '__main__':
    main()