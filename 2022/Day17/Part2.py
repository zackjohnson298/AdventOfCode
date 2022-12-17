import numpy as np
from math import floor


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


def trim_grid(grid, min_width=1):
    grid_height, grid_width = grid.shape
    # trim_index = grid_height
    sums = sum(grid.T).tolist()
    if grid_width in sums:
        trim_index = sums.index(grid_width)
        new_grid = grid[:trim_index+1, :grid_width]
        new_grid[-1, :] = np.ones((1, grid_width))
        return new_grid, grid_height - trim_index - 1
    return grid, 0


def get_profile(grid: np.array):
    profile = [None]*grid.shape[1]
    depth = 0
    for height, row in enumerate(grid):
        for c, value in enumerate(row):
            if value and profile[c] is None:
                profile[c] = height
        if None not in profile:
            break
        depth += 1
    return tuple([depth-value for value in profile])


def main():
    jets = get_input('input.txt')
    rocks = get_rocks()
    jet_index = 0
    # _ = input(len(jets))
    rock_count = 0
    max_rock_count = 1000000000000
    grid = np.ones((1, 7), dtype='bool')
    total_trimmed = 0
    state_list = []
    state_value_list = []
    current_state_value = {}
    last_state_value = {}
    loop_state = ()
    for rock_count in range(max_rock_count):
        # if rock_count % 100 == 0:
        print(rock_count, max_rock_count)
        current_rock = rocks[rock_count % len(rocks) + 1]
        grid = get_new_grid(grid, current_rock)
        grid, trimmed = trim_grid(grid)
        total_trimmed += trimmed
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
            tick += 1
        profile = get_profile(grid)
        state = (profile, rock_count % len(rocks) + 1, jet_index)
        if state not in state_list:
            state_list.append(state)
            state_value_list.append({
                'rock_count': rock_count,
                'height': grid.shape[0] - find_top_index(grid) - 1 + total_trimmed
            })
        else:
            print(f'Loop Found!: {state}')
            loop_state = state
            last_state_value = state_value_list[state_list.index(state)]
            current_state_value = {
                'rock_count': rock_count,
                'height': grid.shape[0] - find_top_index(grid) - 1 + total_trimmed
            }
            break
    period = current_state_value['rock_count'] - last_state_value['rock_count']
    offset = last_state_value['rock_count']
    current_rock_count = offset
    # print(offset, period)
    n = floor(((max_rock_count - offset)/period))
    count_difference = max_rock_count - n*period + offset
    subtracted_height = state_value_list[state_list.index(loop_state) - count_difference]['height']
    # print(state_value_list[state_list.index(loop_state) - count_difference]['height'])
    height_gained_in_period = current_state_value['height'] - last_state_value['height']
    # print(n*period + offset)
    print((n+1)*height_gained_in_period + last_state_value['height'] - subtracted_height - 1)

    # print(grid.shape[0] - find_top_index(grid) - 1 + total_trimmed)
    # print()
    # print_grid(grid[:20, :], np.array([[]]), 0, 0)


main()
