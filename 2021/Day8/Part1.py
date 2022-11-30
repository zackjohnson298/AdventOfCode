import numpy as np


def get_input():
    with open('input.txt') as file:
        lines = file.read().splitlines()
    data = []
    for line in lines:
        inputs, outputs = line.split('|')
        data.append([inputs.split(), outputs.split()])
    return data


def main():
    data = get_input()
    count = 0
    for _, outputs in data:
        for value in outputs:
            if len(value) in [2, 4, 3, 7]:
                count += 1
    print(count)


main()
