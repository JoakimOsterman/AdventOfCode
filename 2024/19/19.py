input_file = 'input.txt'

available_towels = {}
desired_patterns = []

with open(input_file, 'r') as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        if idx == 0:
            available_towels = {x.strip(): True for x in line.split(',')}
        elif line.strip() != '':
            desired_patterns.append(line.strip())

def composable(substring, available_towels):
    return composable_recursive(substring, available_towels, {})

def composable_recursive(substring, available_towels, memo):
    # Base case
    if substring == '':
        return 1
    # Check if substring is in memo
    if substring in memo:
        return memo[substring]
    
    memo[substring] = 0

    for towel in list(available_towels.keys()):
        start, remaining = substring[:len(towel)], substring[len(towel):]
        remaining_num = composable_recursive(remaining, available_towels, memo)

        if start == towel and remaining_num > 0:
            memo[substring] += remaining_num
    
    return memo[substring]

def count_composable(desired_patterns, available_towels):
    count_part1 = 0
    count_part2 = 0

    for pattern in desired_patterns:
        num = composable(pattern, available_towels)
        if num > 0:
            count_part1 += 1
            count_part2 += num
    return count_part1, count_part2

print(count_composable(desired_patterns, available_towels))

    