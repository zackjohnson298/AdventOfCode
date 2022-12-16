import numpy as np


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return line


def reduce(line, debug=False):
    line = line.copy()
    for ii in range(len(line) - 1, 0, -1):
        print(ii) if debug else ''
        while ii < len(line) and line[ii].swapcase() == line[ii - 1]:
            a = line[ii]
            b = line[ii - 1]
            line.pop(ii - 1)
            line.pop(ii - 1)
    return len(line)


def main():
    line = get_input('input.txt')
    # line = 'dabAcCaCBAcCfFcaDAfF'
    line = [value for value in line]
    print(reduce(line, debug=True))


main()