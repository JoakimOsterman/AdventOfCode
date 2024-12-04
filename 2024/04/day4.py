input_file = 'input.txt'


def read_input(input_file):
    array2D = []
    with open(input_file, 'r') as file:
        for line in file:
            chars = list(line.strip())
            array2D.append(chars)
    return array2D

def get_diagonal_adjacent_chars(array, i, j):
    diag_chars = []
    char_set = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 or y == 0:
                continue
            if i + x < 0 or i + x >= len(array):
                continue
            if j + y < 0 or j + y >= len(array[i]):
                continue
            c = array[i + x][j + y]
            char_set.add(c)
            res = (c, (i + x, j + y))
            diag_chars.append(res)
    return diag_chars, char_set



def get_adjacent_chars(array, i, j):
    adjacent_chars = []
    char_set = set()
    
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if i + x < 0 or i + x >= len(array):
                continue
            if j + y < 0 or j + y >= len(array[i]):
                continue
            c = array[i + x][j + y]
            char_set.add(c)

            res = (c, (i + x, j + y))
            adjacent_chars.append(res)
    
    return adjacent_chars, char_set

def traverse_diagonally(array, i_0, j_0):
    start_char = array[i_0][j_0]
    char_set_left = set()
    char_set_right = set()

    # Left diagonal
    left_i = i_0 - 1
    left_j = j_0 - 1
    for i in range(3):
        if left_i < 0 or left_i >= len(array) or left_j < 0 or left_j >= len(array[left_i]):
            raise ValueError('Index out of bounds')
        c = array[left_i][left_j]
        left_i += 1
        left_j += 1
        char_set_left.add(c)
    
    # Right diagonal
    right_i = i_0 - 1
    right_j = j_0 + 1
    for i in range(3):
        if right_i < 0 or right_i >= len(array) or right_j < 0 or right_j >= len(array[right_i]):
            raise ValueError('Index out of bounds')
        c = array[right_i][right_j]
        right_i += 1
        right_j -= 1
        char_set_right.add(c)
    
    if 'S' in char_set_left and 'M' in char_set_left:
        if 'S' in char_set_right and 'M' in char_set_right:
            return True
    return False



def traverse_array(array, i_0, j_0, i_1, j_1):
    """
    Input: 2D array, starting indices (i_0, j_0), traverse indices (i_1, j_1)
    Should already be in case of X -> M
    Return: True if XMAS is found, False otherwise
    """
    traverse_direction = (i_1 - i_0, j_1 - j_0)
    next_i = i_1 + traverse_direction[0]
    next_j = j_1 + traverse_direction[1]

    if next_i >= 0 and next_i < len(array) and next_j >= 0 and next_j < len(array[next_i]):
        char_1 = array[next_i][next_j]
        if char_1 != 'A':
            return False
        next_i += traverse_direction[0]
        next_j += traverse_direction[1]
        if next_i < 0 or next_i >= len(array) or next_j < 0 or next_j >= len(array[next_i]):
            return False
        char_2 = array[next_i][next_j]
        if char_2 != 'S':
            return False
        return True
    return False

def main():
    array2D = read_input(input_file)
    xmas_count_part1 = 0
    xmas_count_part2 = 0

    # Part 1
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] != 'X':
                continue
            adjacent_chars, char_set = get_adjacent_chars(array2D, i, j)
            
            if 'M' not in char_set:
                continue

            for c, (a, b) in adjacent_chars:
                if c == 'M':
                    if traverse_array(array2D, i, j, a, b):
                        xmas_count_part1 += 1 
                        # Test
                        if array2D[i][j] != 'X' or array2D[a][b] != 'M':
                            raise ValueError('Error in logic')  
                    else:
                        continue

    # Part 1 answer
    print(xmas_count_part1)  

    # Part 2
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] != 'A':
                continue
            diag_chars, char_set = get_diagonal_adjacent_chars(array2D, i, j)
            if 'S' not in char_set:
                continue
            if 'M' not in char_set:
                continue

            s_count = 0
            m_count = 0    
            for c, (a, b) in diag_chars:
                if c == 'S':
                    s_count += 1
                if c == 'M':
                    m_count += 1
            if s_count < 2 or m_count < 2:
                continue
            if traverse_diagonally(array2D, i, j):
                xmas_count_part2 += 1
                # Test
                if array2D[i][j] != 'A':
                    raise ValueError('Error in logic')
    # Part 2 answer
    print(xmas_count_part2)

            



if __name__=='__main__':
    main()
        

# Answer 1: 2635 too high
# Answer 2: 2571 was correct