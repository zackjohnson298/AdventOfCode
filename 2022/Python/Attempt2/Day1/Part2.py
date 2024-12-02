from typing import *


def get_input(filename: str) -> List[List[int]]:
    with open(filename) as file:
        lines = file.read().splitlines()

    current = []
    output = []
    line = lines.pop(0)
    while lines:
        if line:
            current.append(int(line))
        else:
            output.append(current)
            current = []
        # if lines:
        line = lines.pop(0)
    if line:
        current.append(int(line))
    if current:
        output.append(current)
    return output


def main():
    calories = sorted(get_input('input.txt'), key=lambda items: sum(items))
    print(sum([sum(items) for items in calories[-3:]]))
    # print(max([sum(items) for items in calories]))


main()
