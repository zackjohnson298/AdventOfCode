import numpy as np


'''
INCOMPLETE
'''


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    clay_positions = []
    for line in lines:
        string1, string2 = line.split(', ')
        a = int(string1.split('=')[1])
        b, c = [int(value) for value in string2.split('=')[1].split('..')]
        if string1[0] == 'x':       # Vertical line
            for y in range(b, c+1):
                clay_positions.append((a, y))
        else:                       # Vertical line
            for x in range(b, c + 1):
                clay_positions.append((x, a))

    return clay_positions


def get_grid_size(clay_positions):
    max_x = max([pos[0] for pos in clay_positions]) + 2
    max_y = max([pos[1] for pos in clay_positions]) + 2
    return max_x, max_y


def print_grid(grid):
    for row in grid.T:
        for value in row:
            if value == 0:
                print('.', end='')
            elif value == 1:
                print('#', end='')
            elif value == 2:
                print('~', end='')
            elif value == 3:
                print('|', end='')
        print()
    print()


def add_water_layer(grid, start_pos):
    current_pos = np.array(start_pos)
    down = np.array((0, 1))
    max_x, max_y = grid.shape
    while (current_pos + down)[1] < max_y and grid[tuple(current_pos + down)] == 0:
        current_pos += down
    if (current_pos + down)[1] == max_y:     # outside of grid
        return
    # see if we are in a basin (at some point going left=1 and going right=1):
    # Go left
    left = np.array((-1, 0))
    while grid[tuple(current_pos + left)] == 0:
        current_pos += left
        if grid[tuple(current_pos + down)] == 0:
            add_water_layer(grid, current_pos)
            return
    left_most_x = current_pos[0]
    # Go right
    right = np.array((1, 0))
    while grid[tuple(current_pos + right)] == 0:
        current_pos += right
        if grid[tuple(current_pos + down)] == 0:
            add_water_layer(grid, current_pos)
            return
    right_most_x = current_pos[0]
    # Fill Basin
    for x in range(left_most_x, right_most_x+1):
        grid[x, current_pos[1]] = 2
    return


def main():
    clay_positions = get_input('test_input.txt')
    grid = np.zeros(get_grid_size(clay_positions))
    for x, y in clay_positions:
        grid[x, y] = 1
    for ii in range(10):
        add_water_layer(grid, (500, 0))
        print_grid(grid[494:508, :])
        _ = input(f'{ii+1}: ')


main()
