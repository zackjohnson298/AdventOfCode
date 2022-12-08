import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(value) for value in lines]


def main():
    instructions = get_input('input.txt')
    pos = 0
    done = False
    count = 0
    while not done:
        jump = instructions[pos]
        instructions[pos] += 1
        pos += jump
        count += 1
        if not 0 <= pos < len(instructions):
            done = True
    print(count)


main()
