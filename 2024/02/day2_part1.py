# Part 1
input_file = 'input.txt'
increasing = None
prev_val = None
safe_line = True

safe_reports = 0

with open(input_file, 'r') as file:
    for line in file:
        # Split the line into array of integers separated by space
        integers = list(map(int, line.split()))

        for val in integers:
            if prev_val is None:
                prev_val = val
                continue

            # Check if breaking increase/decrease pattern
            if increasing is None:
                if val < prev_val:
                    increasing = False
                if val > prev_val:
                    increasing = True
            else:
                if increasing and val < prev_val:
                    safe_line = False
                    break
                if not increasing and val > prev_val:
                    safe_line = False
                    break
            
            # Check if prev_val and val are differing by at least one and at most three
            diff = abs(val - prev_val)
            if diff < 1 or diff > 3:
                safe_line = False
                break

            prev_val = val
        
        if safe_line:
            safe_reports += 1
        
        safe_line = True
        increasing = None
        prev_val = None
        
print(safe_reports) # Answer to part 1

# Part 2






            

            
            
                




        


        

