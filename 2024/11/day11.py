def read_input(input_file):
    stones = []
    with open(input_file) as f:
        stones = [int(val) for val in f.read().split()]
    return stones

def blink(stones, num_blinks):

    for _ in range(num_blinks):
        alt_stones = []
        for i, stone in enumerate(stones):
            stone_str = str(stone)
            if stone == 0:
                #stones[i] = 1
                alt_stones.append(1)
            elif len(stone_str) % 2 == 0:
                left = int(stone_str[:len(stone_str) // 2])
                right = int(stone_str[len(stone_str) // 2:])
                alt_stones.append(left)
                alt_stones.append(right)
                #stones[i] = left
                #stones.insert(i + 1, right)
            else:
                #stones[i] = stone * 2024
                alt_stones.append(stone * 2024)
        stones = alt_stones[:]
    return stones


def main():
    test = [125, 17]
    stones = read_input('input.txt')
    print(len(blink(stones, 25))) # Correct answer to part 1 was 185205


if __name__ == '__main__':
    main()

