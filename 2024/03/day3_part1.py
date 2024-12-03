import re

input_file ='input.txt'
with open(input_file, 'r') as file:
    input_str = file.read()

pattern = 'mul\((\d+,\d+)\)'

result = re.findall(pattern, input_str)

sum = 0
for i in result:
    tup = tuple(int(num) for num in i.split(','))
    sum += tup[0] * tup[1]

print(sum) # Amswer to part 1: 182780583
