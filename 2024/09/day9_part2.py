from collections import defaultdict
import heapq

input_file = 'input.txt'

def read_input(input_file):
    with open(input_file, 'r') as file:
        line = file.readline().strip()
        
        result = [int(line[i]) for i in range(0, len(line))]  
    return result

def func_part2(raw_input):
    lengths = raw_input
    filled_grid = {}  
    gaps = defaultdict(list) 

    cur_pos = 0 

    for i, num in enumerate(lengths):
        if i % 2 == 0:
            filled_grid[i // 2] = [cur_pos, num]
        else:  
            if num > 0:
                heapq.heappush(gaps[num], cur_pos)
        cur_pos += num 

    for i in sorted(filled_grid.keys(), reverse=True):  
        file_start_pos, file_len = filled_grid[i]

        possible_gaps = sorted(
            [[gaps[gap_len][0], gap_len] for gap_len in gaps if gap_len >= file_len]
        )

        if possible_gaps:
            gap_start_pos, gap_len = possible_gaps[0]
            if file_start_pos > gap_start_pos: 
                filled_grid[i] = [gap_start_pos, file_len]
                
                remaining_gap_len = gap_len - file_len
                heapq.heappop(gaps[gap_len])  
                if not gaps[gap_len]:
                    del gaps[gap_len]  
                if remaining_gap_len > 0:
                    heapq.heappush(gaps[remaining_gap_len], gap_start_pos + file_len)

    result = sum(
        num * (start * length + (length * (length - 1)) // 2)
        for num, (start, length) in filled_grid.items()
    )

    return result, filled_grid

def main():
    # 6334655979668 was too low
    # 85452072118 was too low
    # 6349492251099 was correct
    input_part2 = read_input(input_file)
    result_part2, grid = func_part2(input_part2)
    print(f" \n The result is: {result_part2}")



if __name__ == '__main__':
    main()