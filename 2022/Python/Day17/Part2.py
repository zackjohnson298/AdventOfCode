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
    max_rock_count = 1000000000000
    grid = np.ones((1, 7), dtype='bool')
    state_list = []
    state_value_list = []
    second_occurrence_state_value = {}
    first_occurrence_state_value = {}
    for rock_count in range(max_rock_count):
        print(f'Iteration {rock_count + 1} / {max_rock_count}')
        current_rock = rocks[rock_count % len(rocks) + 1]
        grid = get_new_grid(grid, current_rock)
        rock_height, rock_width = current_rock.shape
        rock_y = -1
        rock_x = 2
        done = False
        tick = 0
        while not done:
            if tick % 2 == 0:
                direction = 'v'
            else:
                direction = jets[jet_index]
                jet_index = (jet_index + 1) % len(jets)
            if can_move(grid, current_rock, rock_x, rock_y, direction):
                if direction == '>':
                    rock_x += 1
                elif direction == '<':
                    rock_x -= 1
                else:
                    rock_y += 1
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
                'height': grid.shape[0] - find_top_index(grid) - 1
            })
        else:
            print()
            print(f'Loop Found!')
            print(f'\t  Profile: {state[0]}')
            print(f'\tNext Rock: {state[1]}')
            print(f'\tJet Index: {state[2]}')
            first_occurrence_state_value = state_value_list[state_list.index(state)]
            second_occurrence_state_value = {
                'rock_count': rock_count,
                'height': grid.shape[0] - find_top_index(grid) - 1
            }
            break

    # Loop Found, determine period and offset values
    first_occurrence_rock_count = first_occurrence_state_value['rock_count']
    rock_count_period = second_occurrence_state_value['rock_count'] - first_occurrence_rock_count

    # Find integer N such that first_rock_count + N*period < desired_rock_count < first_rock_count + (N+1)*period
    N = floor((max_rock_count - first_occurrence_rock_count) / rock_count_period)
    delta_rock_count = max_rock_count - first_occurrence_rock_count - N * rock_count_period

    print()
    print(f'N = {N}')
    print(f'Count Period = {rock_count_period}')
    print(f'First Count = {first_occurrence_rock_count}')
    print(f'Delta Count = {delta_rock_count}')

    height_at_first_occurrence = first_occurrence_state_value['height']
    height_period = second_occurrence_state_value['height'] - height_at_first_occurrence
    # Define Starting Height such that starting_height + N * height_period = Desired_height
    starting_height = state_value_list[first_occurrence_rock_count + delta_rock_count]['height']

    print(f'Height Period = {height_period}')
    print(f'Starting Height = {starting_height}')
    print()

    height = N * height_period + starting_height - 1
    print(height)


main()
