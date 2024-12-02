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
    max_score = 0
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            current = grid[r][c]
            right = grid[r][c+1:]
            left = reversed(grid[r][:c])
            up = reversed([grid[ii][c] for ii in range(r)])
            down = [grid[ii][c] for ii in range(r+1, rows)]
            current_score = 1
            for trees in [up, down, left, right]:
                direction_score = 0
                for tree in trees:
                    direction_score += 1
                    if tree >= current:
                        break

                current_score *= direction_score
            # print(current_score, r, c)
            if current_score > max_score:
                max_score = current_score
    print(max_score)

main()
