from scipy.optimize import linprog
import re

input_file = 'input.txt'

def read_input(input_file):
    with open(input_file) as f:
        return f.read().strip().splitlines()
    
def solve_minimum_cost(x_a, y_a, x_b, y_b, P_x, P_y):

    # Objective function
    # minimize z = 3A + B
    c = [3, 1]

    # With the following constraints:
    # A*x_a + B*x_b = P_x
    # A*y_a + B*y_b = P_y
    # A, B >= 0 and integers
    # x_a, x_b, y_a, y_b, P_x, P_y >= 0 and integers
    A_eq = [[x_a, x_b], [y_a, y_b]]
    b_eq = [P_x, P_y]

    bounds = [(0, None), (0, None)]

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs', integrality=[1, 1])
    sol_vector = res.x

    return sol_vector, res.fun


def main():
    button_a = 'Button A'
    button_b = 'Button B'
    prize = 'Prize'

    input = read_input(input_file)
    part1 = 0

    for i in input:
        if i == '':
            solution, fun_val = solve_minimum_cost(x_a, y_a, x_b, y_b, P_x, P_y)
            if solution is not None:
                part1 += fun_val
            x_a, y_a, x_b, y_b, P_x, P_y = 0, 0, 0, 0, 0, 0
            continue
        if button_a in i:
            x_a, y_a = map(int, re.findall(r'\d+', i)) 
            continue 
        if button_b in i:
            x_b, y_b = map(int, re.findall(r'\d+', i))
            continue
        if prize in i:
            P_x, P_y = map(int, re.findall(r'\d+', i))
            continue
    
    print(f"Part 1: {int(part1)}")

if __name__ == '__main__':
    main()