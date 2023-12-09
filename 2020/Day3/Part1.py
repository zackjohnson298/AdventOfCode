from typing import List, Optional, Tuple


def get_input(filename) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def main():
    forest = get_input('input.txt')
    width = len(forest[0])
    row = 0
    col = 0
    d_row = 1
    d_col = 3
    count = 0
    while row < len(forest):
        if forest[row][col % width] == '#':
            count += 1
        row += d_row
        col += d_col
    print(count)



main()
