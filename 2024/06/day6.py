import copy
from tqdm import tqdm
from multiprocessing import Pool


input_file = 'input.txt'

def read_input(input_file):
    grid = []
    with open(input_file, 'r') as file:
        for line in file:
            chars = list(line.strip())
            grid.append(chars)
    return grid

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return (i, j)
    return None

def traverse_and_mark(grid, start):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    dir = directions[0]
    pos = start
    i, j = pos
    grid[i][j] = 'X'

    while i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
        
        i, j = pos
        next_pos = pos[0] + dir[0], pos[1] + dir[1]

        if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[next_pos[0]]):
            break
        next_pos_val = grid[next_pos[0]][next_pos[1]]

        if dir == directions[0]:
            if next_pos_val == '#':
                dir = directions[3]
            else:
                grid[next_pos[0]][next_pos[1]] = 'X'
                pos = next_pos
        elif dir == directions[1]:
            if next_pos_val == '#':
                dir = directions[2]
            else:
                grid[next_pos[0]][next_pos[1]] = 'X'
                pos = next_pos
        elif dir == directions[2]:
            if next_pos_val == '#':
                dir = directions[0]
            else:
                grid[next_pos[0]][next_pos[1]] = 'X'
                pos = next_pos
        elif dir == directions[3]:
            if next_pos_val == '#':
                dir = directions[1]
            else:
                grid[next_pos[0]][next_pos[1]] = 'X'
                pos = next_pos
            
    return grid

def check_if_stuck(grid, start):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    dir = directions[0]
    pos = start
    i, j = pos
    grid[i][j] = 'X'
    stuck = False

    travelled_path = {}

    
    while i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
        i, j = pos
        next_pos = pos[0] + dir[0], pos[1] + dir[1]
        step_from_to = (pos, next_pos) 

        #print(f"Debug size of travelled path: {len(travelled_path)}")

        if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[next_pos[0]]):
            break

        next_pos_val = grid[next_pos[0]][next_pos[1]]

        if next_pos_val != '#':
            if step_from_to in travelled_path:
                stuck = True
                break
            
            travelled_path[step_from_to] = True
            pos = next_pos
        else:
            if dir == directions[0]:
                dir = directions[3]

            elif dir == directions[1]:
                dir = directions[2]

            elif dir == directions[2]:
                dir = directions[0]

            elif dir == directions[3]:
                dir = directions[1]


    return stuck

def process_cell(args):
    original_grid, start, i, j = args
    if original_grid[i][j] == '.':
        grid_mutate = copy.deepcopy(original_grid)
        grid_mutate[i][j] = '#'
        stuck = check_if_stuck(grid_mutate, start)
        if stuck:
            return 1
    return 0

def test_obstacle_for_loop(grid, start):
    original_grid = copy.deepcopy(grid)
    loop_found = False
    count = 0
    tasks = [(original_grid, start, i, j) for i in range(len(original_grid)) for j in range(len(original_grid[i]))]

    with Pool() as pool:
        results = list(tqdm(pool.imap(process_cell, tasks), total=len(tasks)))

    count = sum(results)
    return count  

def count_marked(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                count += 1
    return count

def main():
    original_grid = read_input(input_file)
    grid = copy.deepcopy(original_grid)
    start = find_start(grid)
    traverse_and_mark(grid, start)
    # Part 1
    # Answer: 4988 was correct
    print(count_marked(grid))

    print(count_marked(original_grid))
    # Part 2 1697 was correct
    print(f"Answer to part 2: {test_obstacle_for_loop(original_grid, start)}")
    

    
if __name__ == '__main__':
    main()


