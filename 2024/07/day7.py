from tqdm import tqdm
from itertools import product


input_file = 'input.txt'

def read_input(input_file):
    equations = []
    with open(input_file, 'r') as file:
        for line in file:
            e = line.strip().split(' ')
            equations.append(e)
    return equations

def check_if_valid(equation, part=1):
    digits = equation[1:]
    number_of_operators = len(equation) - 2

    if part == 2:
        operators = ['+', '*', '||']
    else:
        operators = ['+', '*']

    prod = list(product(operators, repeat=number_of_operators))
    ans = int(equation[0][:-1])

    eq_check = 0
    prod_with_digits = []

    for p in prod:
        new_eq =   ''.join(f"{digits[i]} {p[i]} " if i < len(p) else f"{digits[i]}" for i in range(len(digits)))
        prod_with_digits.append(new_eq)

    for eq in prod_with_digits:    
        # Evaluate equation left to right
        parts = eq.split()
        res_part1 = int(parts[0])
        res_part2 = int(parts[0])
        
        if part == 1:
            for i in range(1, len(parts), 2):
                num = int(parts[i+1])
                if parts[i] == '+':
                    res_part1 += num
                elif parts[i] == '*':
                    res_part1 *= num
        
        if part == 2:
            for i in range(1, len(parts), 2):
                num = int(parts[i+1])
                if parts[i] == '+':
                    res_part2 += num
                elif parts[i] == '*':
                    res_part2 *= num
                elif parts[i] == '||':
                    res_str = str(res_part2)
                    res_str += str(num)
                    res_part2 = int(res_str)
        
        if part == 1:
            if res_part1 == ans:
                return ans
        elif part == 2:
            if res_part2 == ans:
                return ans
 
    return 0


def main():
    part1 = 0
    equations = read_input(input_file)

    # Part1 
    for eq in tqdm(equations):
        eq_check = check_if_valid(eq, part=1)
        part1 += eq_check

    print(f"Answer to part1 is {part1}")
    
    # Part 2
    part2 = 0
    for eq in tqdm(equations):
        eq_check = check_if_valid(eq, part=2)
        part2 += eq_check
   
    print(f"Answer to part2 is {part2}")

if __name__ == '__main__':
    main()

