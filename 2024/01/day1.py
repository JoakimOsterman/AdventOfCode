from collections import Counter
# Part 1
input_file = 'input.txt'

left_list = []
right_list = []
difference_list = []
similarity_score = 0

with open(input_file, 'r') as file:
    for line in file:
        l, r = map(int, line.strip().split())
        
        left_list.append(l)
        right_list.append(r)

left_list.sort()
right_list.sort()

difference_list = [abs(l_i - r_i) for l_i, r_i in zip(left_list, right_list)]
total_distance = sum(difference_list)
print(total_distance) # Answer to part 1

# Part 2
left_list_counts = Counter(left_list) 
right_list_counts = Counter(right_list)

for val in left_list_counts.keys():
    sim_score = val * left_list_counts[val] * right_list_counts[val]
    similarity_score += sim_score

print(similarity_score) # Answer to part 2