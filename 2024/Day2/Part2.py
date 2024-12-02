from typing import *


def get_input(filename: str) -> List[List[int]]:
    with open(filename) as file:
        return [[int(value) for value in line.split()] for line in file.read().splitlines()]


def is_safe(line: List[int]) -> bool:
    direction = -1 if line[0] < line[1] else 1
    for ii in range(1, len(line)):
        a = line[ii-1]
        b = line[ii]
        diff = direction * (a - b)
        if not (1 <= diff <= 3):
            return False
    return True


def is_safe_p2(line: List[int]) -> bool:
    if is_safe(line):
        return True
    for ii in range(len(line)):
        if is_safe(line[:ii] + line[ii+1:]):
            return True
    return False


def main():
    lines = get_input('input.txt')
    print(sum([is_safe_p2(line) for line in lines]))


main()
