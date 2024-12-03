import re

input_file ='input.txt'
with open(input_file, 'r') as file:
    input_str = file.read()

iterator_pattern = '(don\'t\(\))|(do\(\))'
matches = re.finditer(iterator_pattern, input_str)

filtered_list = []
prev_index = len(input_str) - 1

for idx, match in reversed(list(enumerate(matches))):
    if match.group() == "do()":
        filtered_list.append(input_str[match.end():prev_index])
        prev_index = match.start()

    if match.group() == "don't()":
        prev_index = match.start()
        continue

filtered_list.append(input_str[:prev_index])
filtered_list.reverse()
filtered_str = ''.join(filtered_list) 

# Same as part 1 regex
pattern = 'mul\((\d+,\d+)\)'

result = re.findall(pattern, filtered_str)

sum = 0
for i in result:
    tup = tuple(int(num) for num in i.split(','))
    sum += tup[0] * tup[1]

print(sum) 
# Amswer to part 1: 182780583 
# Answer to part 2: 90772405
