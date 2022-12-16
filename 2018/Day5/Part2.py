import json


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
    chars = set([value.lower() for value in line])
    min_count = float('inf')
    min_char = None
    for ii, char in enumerate(chars):
        print(ii, '/', len(chars))
        new_line = [value for value in line if value.lower() != char]
        count = reduce(new_line)
        if count < min_count:
            min_count = count
            min_char = char
    print()
    print(min_char, min_count)


main()
