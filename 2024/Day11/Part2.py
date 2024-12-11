from typing import *


def get_input(filename: str) -> List[int]:
    with open(filename) as file:
        return [int(value) for value in file.readline().split()]


def main():
    stone_list = get_input('input.txt')
    blinks = 750
    stones = {stone: stone_list.count(stone) for stone in stone_list}
    for blink in range(1, blinks+1):
        new_stones = {}
        for stone, stone_count in stones.items():
            stone_str = str(stone)
            if stone == 0:
                stones_to_add = [1]
            elif len(stone_str) % 2 == 0:
                a = int(stone_str[:int(len(stone_str)/2)])
                b = int(stone_str[int(len(stone_str)/2):])
                stones_to_add = [a, b]
            else:
                stones_to_add = [stone * 2024]
            for new_stone in stones_to_add:
                if new_stone in new_stones:
                    new_stones[new_stone] += stone_count
                else:
                    new_stones[new_stone] = stone_count
        print(blink, len(stones), len(new_stones), len(set(stones).difference(set(new_stones))))
        stones = new_stones
    print(sum(stones.values()))


main()
