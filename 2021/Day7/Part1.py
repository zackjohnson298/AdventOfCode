import numpy as np


def get_input():
    with open('input.txt') as file:
        line = file.readline()
    return [int(value) for value in line.split(',')]


def main():
    positions = get_input()
    cost = []
    for new_position in range(max(positions) + 1):
        cost.append(sum([abs(new_position - position) for position in positions]))
    print(cost)
    print(min(cost))


main()
