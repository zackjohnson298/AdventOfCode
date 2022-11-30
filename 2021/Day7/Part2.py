import numpy as np


def get_input():
    with open('input.txt') as file:
        line = file.readline()
    return [int(value) for value in line.split(',')]


def main():
    positions = get_input()
    cost_arr = []
    for new_position in range(max(positions) + 1):
        cost = []
        for position in positions:
            n = abs(new_position - position)
            cost.append(int(n * (n + 1) / 2))
        cost_arr.append(sum(cost))
    # print(cost_arr)
    print(min(cost_arr))


main()
