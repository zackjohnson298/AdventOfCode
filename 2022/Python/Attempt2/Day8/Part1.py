from typing import *
import json


def get_input(filename: str) -> List[List[int]]:
    with open(filename) as file:
        return [[int(value) for value in line] for line in file.read().splitlines()]


def main():
    grid = get_input('input.txt')
    # for row in grid:
    #     print(''.join(str(value) for value in row))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(grid)
    cols = len(grid[0])
    total = 2*rows + 2*cols - 4
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            current = grid[r][c]
            right = grid[r][c+1:]
            left = grid[r][:c]
            up = [grid[ii][c] for ii in range(r)]
            down = [grid[ii][c] for ii in range(r+1, rows)]
            for trees in [up, down, left, right]:
                if current > max(trees):
                    # print(r, c, current)
                    total += 1
                    break

    print(total)

main()
