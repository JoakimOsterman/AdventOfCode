input_file = 'input.txt'

def read_input(input_file):
    block = []
    line_info = {}

    with open(input_file, 'r') as file:
        line = file.readline().strip()
        
        result = [(int(line[i]), int(line[i + 1]) if i + 1 < len(line) else None)
          for i in range(0, len(line), 2)]
        

        for i, (r1, r2) in enumerate(result):
            line_info[i] = (r1, r2)
            idx = str(i)
            idx_list = [idx] * r1
            if r2 is not None:
                dot_list = ['.'] * r2
                block.extend(idx_list + dot_list)
                continue
            
            block.extend(idx_list)

    return line_info

def optimized_move_blocks_to_free_space(line_info):
    res_block = []
    last_idx = len(line_info) - 1

    for i, (r1, r2) in line_info.items():
        idx = str(i)
        idx_list = [idx] * r1
        res_block.extend(idx_list)
        
        if r2 is not None and i < last_idx:
            for i in range(r2):
                if line_info[last_idx][0] <= 0:
                    last_idx -= 1
                if last_idx < i:
                    break
                val_to_append = str(last_idx)
                res_block.append(val_to_append)
                line_info[last_idx] = (line_info[last_idx][0] - 1, line_info[last_idx][1])  
                
    return res_block
                
                
def checksum(block):
    sum = 0

    for i, b in enumerate(block):
        if b == '.':
            continue
        sum += int(b) * (i)
    return sum



def main():
    line_info_part1 = read_input(input_file)
    block_test = optimized_move_blocks_to_free_space(line_info_part1)

    # Part1
    part1 = checksum(block_test)
    print(f" \n The checksum is: {part1}") # Correct for part 1 was: 6334655979668
    

if __name__ == '__main__':
    main()