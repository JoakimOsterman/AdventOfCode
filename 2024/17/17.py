import re

# Input parsing
input_file = 'input.txt'
registers = {'A': 0, 'B': 0, 'C': 0}
program = []

with open(input_file, 'r') as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        if idx % 5 == 0:
            registers['A'] = int(line.split(': ')[1].strip())
        elif idx % 5 == 1:
            registers['B'] = int(line.split(': ')[1].strip())
        elif idx % 5 == 2:
            registers['C'] = int(line.split(': ')[1].strip())
        elif idx % 5 == 4:
            program = list(map(int, line.split(': ')[1].strip().split(',')))

# Combo operand resolution
def get_combo_operand(combo):
    if combo == 7:
        raise ValueError("Invalid combo operand")
    return combo if combo < 4 else registers[chr(65 + combo - 4)]  # A=4, B=5, C=6

# Instruction execution
def execute_instruction(pointer, output):
    opcode, operand = program[pointer], program[pointer + 1]

    if opcode == 0:  # ADV
        registers['A'] //= 2 ** get_combo_operand(operand)
    elif opcode == 1:  # BXL
        registers['B'] ^= operand
    elif opcode == 2:  # BST
        registers['B'] = get_combo_operand(operand) % 8
    elif opcode == 3:  # JNZ
        if registers['A'] != 0:
            return operand, output  # Jump
    elif opcode == 4:  # BXC
        registers['B'] ^= registers['C']
    elif opcode == 5:  # OUT
        output.append(str(get_combo_operand(operand) % 8))
    elif opcode == 6:  # BDV
        registers['B'] = registers['A'] // (2 ** get_combo_operand(operand))
    elif opcode == 7:  # CDV
        registers['C'] = registers['A'] // (2 ** get_combo_operand(operand))
    return pointer + 2, output

# Program runner
def run_program():
    pointer = 0
    output = []

    while pointer < len(program):
        pointer, output = execute_instruction(pointer, output)

    print(','.join(output))  # Join outputs with commas

# Run the program
run_program()
