import numpy as np
import re
from collections import Counter, defaultdict

GRID_SIZE_X = 101
GRID_SIZE_Y = 103
TICKS = 100
robot_pos_and_vel = {}

# Parse input
with open('input.txt') as f:
    for idx, line in enumerate(f):
        parts = line.strip().split()
        p = tuple(map(int, parts[0].split('=')[1].split(',')))
        v = tuple(map(int, parts[1].split('=')[1].split(',')))
        robot_pos_and_vel[idx] = (p, v)

def simulate_robot_movement(ticks):
    for _ in range(ticks):
        positions = Counter()
        for robot in robot_pos_and_vel:
            (x, y), (dx, dy) = robot_pos_and_vel[robot]
            # Update position with wrapping
            new_x = (x + dx) % GRID_SIZE_X
            new_y = (y + dy) % GRID_SIZE_Y
            positions[(new_x, new_y)] += 1
            robot_pos_and_vel[robot] = ((new_x, new_y), (dx, dy))
        yield positions

def calc_safety_factor(positions):
    x_mid, y_mid = GRID_SIZE_X // 2, GRID_SIZE_Y // 2
    quadrants = defaultdict(int)
    for (x, y), count in positions.items():
        if x == x_mid or y == y_mid:
            continue
        if x < x_mid and y < y_mid:
            quadrants['top_left'] += count
        elif x < x_mid and y > y_mid:
            quadrants['bottom_left'] += count
        elif x > x_mid and y < y_mid:
            quadrants['top_right'] += count
        elif x > x_mid and y > y_mid:
            quadrants['bottom_right'] += count
    return quadrants['top_left'] * quadrants['bottom_left'] * quadrants['top_right'] * quadrants['bottom_right']    

def print_grid():
    for (x, y), count in positions.items():
        print(f"{x}, {y}: {count}")


# Simulation and safety factor
positions = Counter()
for positions in simulate_robot_movement(TICKS):
    pass
print(f"Safety Factor: {calc_safety_factor(positions)}")

# Part 2, 6142 was too low and so was 6143, 6150 was too low

input_matrix = np.fromregex('input.txt', r'-?\d+', [('',int)]*4).view(int).reshape(-1,2,2)

def matrix_func(matrix, mod):
    mod_list = np.arange(mod)
    pos = np.outer(mod_list, matrix[:,1]) + matrix[:,0]
    return (pos % mod).var(axis=1).argmin()

x = matrix_func(input_matrix[...,0], GRID_SIZE_X)
y = matrix_func(input_matrix[...,1], GRID_SIZE_Y)
print((pow(GRID_SIZE_X, -1, GRID_SIZE_Y) * (y - x) % GRID_SIZE_Y) * GRID_SIZE_X + x)