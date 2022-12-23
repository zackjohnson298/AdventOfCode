import numpy as np
import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    elves = {}
    elf_id = 0
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '#':
                elf = {
                    'id': elf_id,
                    'pos': (r, c),
                    # 'choices': ['n', 's', 'e', 'w'],
                    'proposed_pos': None
                }
                elves[elf_id] = elf
                elf_id += 1
    return elves


def create_grid(elves):
    max_r = max([elf['pos'][0] for elf in elves.values()]) + 5
    max_c = max([elf['pos'][1] for elf in elves.values()]) + 5
    min_r = min([elf['pos'][0] for elf in elves.values()]) - 5
    min_c = min([elf['pos'][1] for elf in elves.values()]) - 5
    grid = np.zeros((max_r-min_r, max_c-min_c))
    for elf in elves.values():
        pos = elf['pos']
        grid[pos] = 1
    return grid


def draw_grid(grid):
    for row in grid:
        for value in row:
            print('#' if value == 1 else '.', end='')
        print()
    print()


def get_positions(pos: (int, int), direction: str):
    r, c = pos
    if direction == 'n':
        return [(r-1, c-1), (r-1, c), (r-1, c+1)]
    if direction == 's':
        return [(r+1, c-1), (r+1, c), (r+1, c+1)]
    if direction == 'e':
        return [(r-1, c+1), (r, c+1), (r+1, c+1)]
    if direction == 'w':
        return [(r-1, c-1), (r, c-1), (r+1, c-1)]


def get_neighbors(grid, pos):
    r, c = pos
    neighbors = []
    for nr in [r-1, r, r+1]:
        for nc in [c-1, c, c+1]:
            if (nr, nc) == (r, c):
                continue
            if grid[nr, nc] == 1:
                neighbors.append((nr, nc))
    return neighbors


def update(elves, choices):
    grid = create_grid(elves)
    directions = {
        'n': np.array((-1, 0)),
        's': np.array((1, 0)),
        'e': np.array((0, 1)),
        'w': np.array((0, -1)),
    }
    proposed_moves = {}
    invalid_ids = []
    # First half of the round
    for elf_id, elf in elves.items():
        pos = elf['pos']
        neighbors = get_neighbors(grid, pos)
        if len(neighbors) == 0:
            elf['proposed_pos'] = None
            continue
        for direction in choices:
            positions = get_positions(pos, direction)
            total = sum([grid[position] for position in positions])
            if total == 0:
                new_pos = tuple(np.array(pos) + directions[direction])
                elf['proposed_pos'] = new_pos
                if new_pos in proposed_moves:
                    invalid_ids.append(elf_id)
                    invalid_ids.append(proposed_moves[new_pos])
                    elf['proposed_pos'] = None
                    elves[proposed_moves[new_pos]]['proposed_pos'] = None
                else:
                    proposed_moves[new_pos] = elf_id
                break
        else:
            elf['proposed_pos'] = None
            # print('CONFUSION', pos)
    # Second half of the round:
    for elf_if, elf in elves.items():

        if elf_if not in invalid_ids and elf['proposed_pos'] is not None:
            elf['pos'] = elf['proposed_pos']
            elf['proposed_pos'] = None
    choices.append(choices.pop(0))


def create_main_grid(elves):
    max_r = max([elf['pos'][0] for elf in elves.values()])+1
    max_c = max([elf['pos'][1] for elf in elves.values()])+1
    min_r = min([elf['pos'][0] for elf in elves.values()])
    min_c = min([elf['pos'][1] for elf in elves.values()])
    grid = np.zeros((max_r - min_r, max_c - min_c))
    for elf in elves.values():
        pos = tuple(np.array(elf['pos']) - np.array((min_r, min_c)))
        grid[pos] = 1
    return grid


def main():
    elves = get_input('input.txt')
    choices = ['n', 's', 'w', 'e']
    grid = create_main_grid(elves)
    # draw_grid(grid)
    # print(choices)
    # _ = input(0)
    # print()
    count = 1
    while True:
        update(elves, choices)
        new_grid = create_main_grid(elves)
        if new_grid.shape == grid.shape and (new_grid == grid).all():
            break
        else:
            count += 1
            grid = new_grid
        # draw_grid(grid)
        # print(choices)
        # _ = input(ii+1)
        # print()
        print(count)
    print()
    print(count)
    # print(sum(sum(grid == 0)))


main()
