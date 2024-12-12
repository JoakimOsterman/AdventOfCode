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
    print(f"Garden map: {garden_map}")
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
    # Each cell has 4 sides, the perimiter is the number of cells that are not adjacent to another cell in the same region
    perimiter = 0
    for (x, y), char in region.items():
        sides = 4
        for (adj_x, adj_y), adj_char in get_neighbors(x, y, region):
            if adj_char == char:
                sides -= 1
        perimiter += sides
    return perimiter

def main():

    regions = find_regions(garden_map)

    part1 = 0
    for region in regions.values():
        for r in region:
            part1 += get_region_area(r) * get_region_perimeter(r)
    print(f"Part 1: {part1}")

if __name__ == '__main__':
    main()