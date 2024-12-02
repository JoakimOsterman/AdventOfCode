# Part 2
input_file = 'input.txt'

def main():
    # Read the input file and parse it into a list of lists of integers
    with open(input_file, 'r') as file:
        lines = [[int(x) for x in line.split()] for line in file.readlines()]

    # Initialize a counter for safe reports
    safe_reports = 0

    # Iterate through each line
    for line in lines:
        # For each line, remove one element at a time
        for idx in range(len(line)):
            # New line with element at idx removed
            elements_before = line[:idx]
            elements_after = line[idx + 1:]
            idx_removed = elements_before + elements_after
            
            # Calculate the differences between consecutive elements
            differences = [y - x for x, y in zip(idx_removed, idx_removed[1:])]
            
            # Check if all differences are in the "safe" range
            if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
                safe_reports += 1
                break  # Stop checking further for this line once it's confirmed safe

    print("Safe Reports:", safe_reports) # Correct Safe Reports: 381

if __name__ == "__main__":
    main()
