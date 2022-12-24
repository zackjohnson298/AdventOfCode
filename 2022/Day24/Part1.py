from math import lcm
import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    start_pos = (-1, 0)
    grid = [line[1:-1] for line in lines[1:-1]]
    end_pos = (len(grid), len(grid[0])-1)
    return grid, start_pos, end_pos


def populate_safe_cells(grid, start_pos, end_pos):
    rows = len(grid)
    cols = len(grid[0])
    period = lcm(rows, cols)
    directions = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }
    all_positions = {(r, c) for r in range(rows) for c in range(cols)} | {start_pos, end_pos}
    safe = []
    clouds = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value in '><v^':
                clouds.append([(r, c), directions[value]])

    for t in range(period):
        cloud_positions = {position for position, _ in clouds}
        safe_positions = all_positions - cloud_positions
        for cloud in clouds:
            r, c = cloud[0]
            dr, dc = cloud[1]
            cloud[0] = ((r + dr) % rows, (c + dc) % cols)
        safe.append(safe_positions)
    return safe


def navigate(safe_cells, start_pos, end_pos):
    period = len(safe_cells)
    options = {start_pos}
    t = 0
    while True:
        t += 1
        neighbors = set()
        for r, c in options:
            destinations = {(r, c), (r+1, c), (r-1, c), (r, c+1), (r, c-1)}
            safe_destinations = destinations & safe_cells[t % period]
            if end_pos in safe_destinations:
                return t
            neighbors |= safe_destinations
        options = neighbors


def main():
    grid, start_pos, end_pos = get_input('input.txt')
    safe = populate_safe_cells(grid, start_pos, end_pos)
    print(navigate(safe, start_pos, end_pos))


main()