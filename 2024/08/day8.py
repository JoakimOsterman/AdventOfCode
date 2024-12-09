
input_file = 'input.txt'

def read_input(input_file):
    grid = {}
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                grid[(i, j)] = char
    return grid

def get_char_to_coords(grid):
    char_to_coords = {}
    for pos, char in grid.items():
        if char != '.':
            if char not in char_to_coords:
                char_to_coords[char] = [pos]
            else:
                char_to_coords[char].append(pos)
    return char_to_coords


def place_antinodes_part1(char_to_coords, grid):
    from_to_distances = {}
    for char, coords in char_to_coords.items():
        for coord in coords:
            distances = [(c[0] - coord[0], c[1] - coord[1]) for c in coords if c != coord]
            from_to_distances[coord] = distances
            for d in distances:
                a1 = (coord[0] - d[0], coord[1] - d[1])
                a2 = (coord[0] + 2*d[0], coord[1] + 2*d[1])
                # Check if the grid position for a1 and a2 are '.' chars. If they are, then we can add them to the grid
                if grid.get(a1) == '.' or (grid.get(a1) != char and grid.get(a1) != '#' and grid.get(a1) != None):
                    grid[a1] = '#'
                if grid.get(a2) == '.' or (grid.get(a2) != char and grid.get(a2) != '#' and grid.get(a2) != None):
                    grid[a2] = '#'
    return grid

def place_antinodes_part2(char_to_coords, grid):
    from_to_distances = {}
    for char, coords in char_to_coords.items():
        for coord in coords:
            # Check if the char only has one coordinate
            if len(coords) == 1:
                continue
            distances = [(c[0] - coord[0], c[1] - coord[1]) for c in coords if c != coord]
            from_to_distances[coord] = distances
            for d in distances:
                prev_a1 = coord
                prev_a2 = (coord[0] + d[0], coord[1] + d[1])

                if grid.get(prev_a1) != '#' and grid.get(prev_a1) != None:
                    grid[prev_a1] = '#'
                if grid.get(prev_a2) != '#' and grid.get(prev_a2) != None:
                    grid[prev_a2] = '#'

                while grid.get(prev_a1) != None:
                    a1 = (prev_a1[0] - d[0], prev_a1[1] - d[1])
                    if grid.get(a1) != '#' and grid.get(a1) != None:
                        grid[a1] = '#'
                    prev_a1 = a1

                while grid.get(prev_a2) != None:
                    a2 = (prev_a2[0] + d[0], prev_a2[1] + d[1])
                    if grid.get(a2) != '#' and grid.get(a2) != None:
                        grid[a2] = '#'
                    prev_a2 = a2

             
    return grid

def count_antinodes_in_grid(grid):
    count = 0
    for pos, char in grid.items():
        if char == '#':
            count += 1

    return count

def main():
    # Part 1
    grid = read_input(input_file)
    grid_2 = grid.copy()
    char_to_coords = get_char_to_coords(grid)
    grid = place_antinodes_part1(char_to_coords, grid)
    count = count_antinodes_in_grid(grid)
    print(f"Number of antinodes, part 1: {count}")

    # Part 2
    grid_2 = place_antinodes_part2(char_to_coords, grid_2)
    count_2 = count_antinodes_in_grid(grid_2)
    print(f"Number of antinodes, part 2: {count_2}")



if __name__ == '__main__':
    main()

        