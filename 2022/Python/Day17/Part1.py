import numpy as np


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [char for char in line]


def get_rocks() -> {int: np.array}:
    rocks = {
        1: np.array([
                [1, 1, 1, 1]
            ], dtype='bool'),
        2: np.array([
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]
            ], dtype='bool'),
        3: np.array([
                [0, 0, 1],
                [0, 0, 1],
                [1, 1, 1]
            ], dtype='bool'),
        4: np.array([
                [1],
                [1],
                [1],
                [1]
            ], dtype='bool'),
        5: np.array([
                [1, 1],
                [1, 1]
        ], dtype='bool')
    }
    return rocks


def get_new_grid(grid: np.array, rock: np.array):
    rock_height, _ = rock.shape
    grid_height, grid_width = grid.shape
    top_index = find_top_index(grid)
    new_grid_height = grid_height + rock_height + (3 - top_index)
    new_grid = np.zeros((new_grid_height, grid_width), dtype='bool')
    if grid_height < new_grid_height:
        new_grid[-grid_height:, :grid_width] = grid
    else:
        new_grid = grid[-new_grid_height:, :grid_width]
    return new_grid


def find_top_index(grid):
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                return r
    return None


def can_move(grid, rock, rock_x, rock_y, direction):
    grid_height, grid_width = grid.shape
    rock_height, rock_width = rock.shape
    if direction == '>':
        for r in range(rock_height):
            for c in range(rock_width):
                if rock[r, c] and (rock_x + c + 1 >= grid_width or grid[rock_y+r, rock_x+c+1] != 0):
                    return False
    if direction == '<':
        for r in range(rock_height):
            for c in range(rock_width):
                if rock[r, c] and (rock_x + c < 1 or grid[rock_y+r, rock_x+c-1] != 0):
                    return False
    if direction == 'v':
        for r in range(rock_height):
            for c in range(rock_width):
                if rock[r, c] and (grid[rock_y + r + 1, rock_x + c] != 0):
                    return False
    return True


def print_grid(grid, rock, rock_x, rock_y):
    new_grid = grid.copy()
    rock_height, rock_width = rock.shape
    for r in range(rock_height):
        for c in range(rock_width):
            new_grid[r+rock_y, c+rock_x] |= rock[r, c]
    for row in new_grid:
        for value in row:
            print('#' if value else '.', end='')
        print()
    print()


def main():
    jets = get_input('input.txt')
    rocks = get_rocks()
    jet_index = 0
    rock_count = 0
    max_rock_count = 2022
    grid = np.ones((1, 7), dtype='bool')

    for rock_count in range(max_rock_count):
        current_rock = rocks[rock_count % len(rocks) + 1]
        grid = get_new_grid(grid, current_rock)
        rock_height, rock_width = current_rock.shape
        rock_y = -1
        rock_x = 2
        # print_grid(grid, current_rock, rock_x, rock_y+1)
        # _ = input()
        done = False
        tick = 0
        while not done:
            if tick % 2 == 0:
                direction = 'v'
            else:
                direction = jets[jet_index]
                jet_index += 1
                if jet_index == len(jets):
                    jet_index = 0
            if can_move(grid, current_rock, rock_x, rock_y, direction):
                if direction == 'v':
                    rock_y += 1
                else:
                    rock_x += 1 if direction == '>' else -1
            elif direction == 'v':
                done = True
                for r in range(rock_height):
                    for c in range(rock_width):
                        grid[rock_y+r, rock_x+c] |= current_rock[r, c]
            # _ = input()
            tick += 1
    print(grid.shape[0] - find_top_index(grid) - 1)

main()
