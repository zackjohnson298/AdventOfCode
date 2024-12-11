from typing import *


def get_input(filename: str) -> List[int]:
    with open(filename) as file:
        return [int(value) for value in file.readline().split()]


def main():
    stones = get_input('input.txt')
    blinks = 25
    # print('Initial arrangement:')
    # print(' '.join(str(value) for value in stones))
    # print()
    for blink in range(1, blinks+1):
        print(blink, len(stones))
        index = 0
        while index < len(stones):
            stone = stones[index]
            stone_str = str(stone)
            if stone == 0:
                stones[index] = 1
                index += 1
            elif len(stone_str) % 2 == 0:
                a = int(stone_str[:int(len(stone_str)/2)])
                b = int(stone_str[int(len(stone_str)/2):])
                stones[index] = a
                stones.insert(index+1, b)
                index += 2
            else:
                stones[index] = stone * 2024
                index += 1
        # print(f'After {blink} blinks:')
        # print(' '.join(str(value) for value in stones))
        # print()
    print(len(stones))


main()
