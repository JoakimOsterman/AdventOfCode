import time
from collections import Counter

from tqdm import tqdm

def read_input(input_file):
    stones = []
    with open(input_file) as f:
        stones = [int(val) for val in f.read().split()]
    return stones

def blink(stones, num_blinks):
    start_time = time.time()
    stone_counts = Counter(stones)

    for _ in range(num_blinks):
        next_counts = Counter()
        for stone, count in stone_counts.items():
            stone_str = str(stone)
            if stone == 0:
                next_counts[1] += count
            elif len(stone_str) % 2 == 0:
                left = int(stone_str[:len(stone_str) // 2])
                right = int(stone_str[len(stone_str) // 2:])
                next_counts[left] += count
                next_counts[right] += count
            else:
                next_counts[stone * 2024] += count

        stone_counts = next_counts
    print(f"Time taken: {time.time() - start_time} seconds")
    return stone_counts


def main():
    stones = read_input('input.txt')
    print(sum(blink(stones, 25).values())) # Correct answer to part 1 was 185205

    # Part 2
    print(sum(blink(stones, 75).values())) # Correct answer to part 2 was 221280540398419


if __name__ == '__main__':
    main()

