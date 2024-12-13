import re
from ortools.linear_solver import pywraplp

input_file = 'input.txt'

def read_input(input_file):
    with open(input_file) as f:
        return f.read().strip().splitlines()
    

def solve_minimum_cost_mixed_integer_linear_programming(x_a, y_a, x_b, y_b, P_x, P_y):
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variables
    A = solver.IntVar(0, solver.infinity(), 'A')
    B = solver.IntVar(0, solver.infinity(), 'B')

    # Constraints
    solver.Add(A * x_a + B * x_b == P_x)
    solver.Add(A * y_a + B * y_b == P_y)

    # Objective function: Minimize 3A + B
    solver.Minimize(3 * A + B)

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        return [A.solution_value(), B.solution_value()], solver.Objective().Value()
    else:
        return None, None
    
def iterate_over_input(input, part=1):
    button_a = 'Button A'
    button_b = 'Button B'
    prize = 'Prize'
    x_a, y_a, x_b, y_b, P_x, P_y = 0, 0, 0, 0, 0, 0

    score_list = []
    score = 0
    added_price = 0
    if part == 2:
        added_price = 10000000000000

    for idx, i in enumerate(input):
        if button_a in i:
            x_a, y_a = map(int, re.findall(r'\d+', i)) 
            continue 
        if button_b in i:
            x_b, y_b = map(int, re.findall(r'\d+', i))
            continue
        if prize in i:
            P_x, P_y = map(int, re.findall(r'\d+', i))
            if idx == len(input) - 1:
                solution, fun_val = solve_minimum_cost_mixed_integer_linear_programming(x_a, y_a, x_b, y_b, P_x + added_price, P_y + added_price)
                if solution is not None:
                    score += int(fun_val)
                    score_list.append(fun_val)
                    fun_val = 0
            continue
        if i == '':
            solution, fun_val = solve_minimum_cost_mixed_integer_linear_programming(x_a, y_a, x_b, y_b, P_x + added_price, P_y + added_price)
            if solution is not None:
                score += int(fun_val)
                score_list.append(fun_val)
                fun_val = 0
            x_a, y_a, x_b, y_b, P_x, P_y = 0, 0, 0, 0, 0, 0
            continue

    return score, score_list
            
def main():

    input = read_input(input_file)
    part1, part2 = 0, 0
    # Part 1
    part1, _ = iterate_over_input(input, part=1)
    # Part 2
    part2, _ = iterate_over_input(input, part=2)
    print(f"Part 1: {int(part1)} \n \n Part 2: {int(part2)}")


if __name__ == '__main__':
    main()