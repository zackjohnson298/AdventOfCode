from typing import List, Optional, Tuple


def get_input(filename) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def main():
    forest = get_input('input.txt')
    width = len(forest[0])
    total = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for d_col, d_row in slopes:
        row = 0
        col = 0
        count = 0
        while row < len(forest):
            if forest[row][col % width] == '#':
                count += 1
            row += d_row
            col += d_col
        total *= count
    print(total)



main()
