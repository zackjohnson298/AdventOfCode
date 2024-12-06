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


def main():
    directions = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0),
        '^': (-1, 0)
    }
    options = ['^', '>', 'v', '<']
    grid, pos, direction = get_input('input.txt')
    r, c = pos
    rows = len(grid)
    cols = len(grid[0])
    positions = {pos}
    nr, nc = pos
    while 0 <= nr < rows and 0 <= nc < cols:
        if grid[nr][nc]:
            index = options.index(direction)
            direction = options[(index + 1) % len(options)]
        else:
            pos = nr, nc
            positions.add(pos)
        dr, dc = directions.get(direction)
        nr, nc = (pos[0] + dr, pos[1] + dc)

    print(len(positions))


main()
