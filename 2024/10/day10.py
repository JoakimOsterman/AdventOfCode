input_file = 'input.txt'

grid = {}

with open(input_file) as f:
    for y, line in enumerate(f):
        for x, digit in enumerate(line.strip()):
            grid[(x, y)] = digit

def find_start():
    start_positions = [xy for xy, value in grid.items() if value == '0']
    return start_positions

def find_trailhead_score_part1(start_position, visited=None):
    if visited is None:
        visited = set()
    x, y = start_position
    if start_position in visited:
        return 0
    visited.add(start_position)

    if grid[start_position] == '9':
        return 1

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    score_sum = 0
    current_value = int(grid[start_position])

    for dx, dy in directions:
        next_pos = (x + dx, y + dy)
        if next_pos in grid and next_pos not in visited:
            next_value = int(grid[next_pos])
            if next_value == current_value + 1:  # Valid uphill step
                score_sum += find_trailhead_score_part1(next_pos, visited)

    visited.remove(start_position)

    return score_sum  

def find_trailhead_score_part2(start_position):
    x, y = start_position
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    score_sum = 0
    if grid[start_position] == '9':
        return 1
    else:
        value = grid[(x, y)]
        adj = [((x + dx, y + dy), grid.get((x + dx, y + dy))) for dx, dy in directions if grid.get((x + dx, y + dy)) is not None] 

        possible_adj = [adjacent for adjacent, adjacent_value in adj if int(adjacent_value) - int(value) == 1]
        if len(possible_adj) == 0:
            return 0
        else:
            for possible_position in possible_adj:
                score_sum += find_trailhead_score_part2(possible_position)
            return score_sum           
        

def main():
    start_positions = find_start()
    print(f"Amount of start positions: {len(start_positions)}") 
    total_score_part1 = 0
    for start_position in start_positions:
        total_score_part1 += find_trailhead_score_part1(start_position)
    print(total_score_part1)

    total_score_part2 = 0
    for start_position in start_positions:
        total_score_part2 += find_trailhead_score_part2(start_position)
    print(total_score_part2)


if __name__ == '__main__':  
    main()