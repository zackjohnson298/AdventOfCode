from typing import *


def get_input(filename: str) -> Tuple[List[int], List[int]]:
    with open(filename) as file:
        lines = [line.split() for line in file.read().splitlines()]
        return [int(line[0]) for line in lines], [int(line[1]) for line in lines]


def main():
    l1, l2 = get_input('input.txt')
    total = sum([l2.count(a) * a for a in l1])
    print(total)


main()
