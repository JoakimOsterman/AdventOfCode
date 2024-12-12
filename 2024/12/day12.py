from collections import defaultdict

input_file = 'input.txt'

garden_map = {}
with open(input_file) as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            garden_map[(x, y)] = char

def get_neighbors(x, y, garden_map):
    return [((x + dx, y + dy), garden_map.get((x + dx, y + dy))) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)] if garden_map.get((x + dx, y + dy)) is not None] 

def find_regions(garden_map):
    regions = defaultdict(list)
    visited = set()

    def dfs(x, y, char):
        stack = [(x, y)]
        region = {}

        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue

            visited.add((cx, cy))
            region[(cx, cy)] = char

            # Adding adjacent cells to the stack
            for (adj_x, adj_y), adj_char in get_neighbors(cx, cy, garden_map):
                if adj_char == char and (adj_x, adj_y) not in visited:
                    stack.append((adj_x, adj_y))

        return region
    
    for (x, y), char in garden_map.items():
        if (x, y) not in visited:
            regions[char].append(dfs(x, y, char))
    
    return regions
    
def get_region_area(region):
    return len(region)

def get_region_perimeter(region):
    perimiter = 0
    for (x, y), char in region.items():
        sides = 4
        for (adj_x, adj_y), adj_char in get_neighbors(x, y, region):
            if adj_char == char:
                sides -= 1
        perimiter += sides
    return perimiter

def get_neighbors_part2(x, y, garden_map):
    return [((x + dx, y + dy), garden_map.get((x + dx, y + dy))) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

def get_number_of_sides(region, garden_map):
    collection_of_sides = {}

    for (x, y), char in region.items():
        for (adj_x, adj_y), adj_char in get_neighbors_part2(x, y, garden_map):
            if adj_char != char:
                rel_pos = 'above' if adj_y < y else 'below' if adj_y > y else 'left' if adj_x < x else 'right' if adj_x > x else None
                collection_of_sides[(x, y, rel_pos)] = True
 
    connected_sides = defaultdict(list)
    visited_sides = set()

    def side_dfs(x, y, side):
        stack = [(x, y, side)]
        connected = []

        while stack:
            cx, cy, side = stack.pop()
            if (cx, cy, side) in visited_sides:
                continue

            visited_sides.add((cx, cy, side))
            connected.append((cx, cy, side))

            for (adj_x, adj_y, adj_pos), _ in collection_of_sides.items():
                dx, dy = abs(adj_x - cx), abs(adj_y - cy)
                if (adj_x, adj_y, adj_pos) not in visited_sides and adj_pos == side and (adj_x, adj_y) in region:

                    if (adj_pos == 'above' or adj_pos == 'below') and dx == 1 and dy == 0:
                        stack.append((adj_x, adj_y, adj_pos))
                        


                    elif (adj_pos == 'left' or adj_pos == 'right') and dx == 0 and dy == 1:
                            stack.append((adj_x, adj_y, adj_pos))
    
        return connected
    
    for (x, y, pos), _ in collection_of_sides.items():
        connected_sides[(x, y, pos)].append(side_dfs(x, y, pos))
    
    num_of_sides = 0
    for _, connected in connected_sides.items():
        if len(connected[0]) > 0:
            num_of_sides += 1

    return num_of_sides

def main():

    regions = find_regions(garden_map)

    part1 = 0
    for region in regions.values():
        for r in region:
            part1 += get_region_area(r) * get_region_perimeter(r)
    print(f"Part 1: {part1}") # Correct answer was 1465112

    # Part 2
    part2 = 0
    for region in regions.values():
        for r in region:
            part2 += get_number_of_sides(r, garden_map) * get_region_area(r)
    print(f"Part 2: {part2}") # 

if __name__ == '__main__':
    main()