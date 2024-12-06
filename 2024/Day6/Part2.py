from typing import *


def get_input(filename: str) -> Tuple[List[List[bool]], Tuple[int, int], str]:
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = []
    pos = ()
    direction = ()
    for r, line in enumerate(lines):
        row = []
        for c, char in enumerate(line):
            if char == '.':
                row.append(False)
            elif char == '#':
                row.append(True)
            else:
                pos = (r, c)
                direction = char
                row.append(False)
        grid.append(row)
    return grid, pos, direction


def run(grid: List[List[bool]], pos: Tuple[int, int], direction: str) -> bool:
    directions = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0),
        '^': (-1, 0)
    }
    options = ['^', '>', 'v', '<']
    rows = len(grid)
    cols = len(grid[0])
    states = set()
    nr, nc = pos
    while 0 <= nr < rows and 0 <= nc < cols:
        if grid[nr][nc]:
            index = options.index(direction)
            direction = options[(index + 1) % len(options)]
        else:
            pos = nr, nc
            state = (pos, direction)
            if state in states:
                # print(states)
                return True
            states.add(state)
        dr, dc = directions.get(direction)
        nr, nc = (pos[0] + dr, pos[1] + dc)
    return False


def main():
    grid, pos, direction = get_input('input.txt')
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] or (r, c) == pos:
                continue
            new_grid = [[value for value in row] for row in grid]
            new_grid[r][c] = True
            if run(new_grid, pos, direction):
                count += 1
    print(count)


main()
