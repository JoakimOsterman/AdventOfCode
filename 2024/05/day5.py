input_file = 'input.txt'

top_part = True
orders = {}
rule_adhearing_lines = []
rule_breaking_lines = []

# Read in all the rules
with open(input_file, 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            top_part = False
            continue

        if top_part:
            rules = line.strip().split('|')            
            k, v = int(rules[0]), int(rules[1])

            if orders.get(k) is None:
                list_of_vals = [v]
                orders[k] = list_of_vals
            else:
                prev_vals = orders[k]
                prev_vals.append(v)
                orders[k] = prev_vals

        else:
            print_lines = line.strip().split(',')
            print_lines = [int(x) for x in print_lines]
            rule_break = False

            for i in print_lines:
                if i in orders:
                    val_list = orders[i]
                    index_i = print_lines.index(i)
                    for j in print_lines[:index_i]:
                        if j in val_list:
                            # Rule break
                            rule_break = True
                            break
                    if rule_break:
                        break
            if not rule_break:
                rule_adhearing_lines.append(print_lines)
            else:
                rule_breaking_lines.append(print_lines)


# Part 1 answer
ans_part1 = 0

for line in rule_adhearing_lines:
    len_line = len(line)
    if len_line % 2 != 0:
        middle_idx = len_line // 2
    else:
        raise ValueError("Line length is not odd")
    ans_part1 += line[middle_idx]

print(f"Part 1 answer: {ans_part1}")

# Part 2
for line in rule_breaking_lines:
    restart = True
    while restart:
        restart = False
        for i in line:
            if i in orders:
                val_list = orders[i]
                index_i = line.index(i)

                for j in line[:index_i]:
                    if j in val_list:
                        # Rule break
                        index_j = line.index(j)
                        line[index_i], line[index_j] = line[index_j], line[index_i]
                        restart = True


ans_part2 = 0
for line in rule_breaking_lines:
    len_line = len(line)
    if len_line % 2 != 0:
        middle_idx = len_line // 2
    else:
        raise ValueError("Line length is not odd")
    ans_part2 += line[middle_idx]

print(f"Part 2 answer: {ans_part2}")

"""
Part 1 answer: 5964
Part 2 answer: 4719
"""