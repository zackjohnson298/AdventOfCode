import numpy as np


def print_grid(grid):
    for row in grid.T:
        for value in row:
            if value == 0:
                print('.', end='')
            elif value == 1:
                print('=', end='')
            if value == 2:
                print('|', end='')
        print()
    print()



def main():
    depth = 9171
    target = (7, 721)
    erosion_grid = np.zeros((target[0]+1, target[1]+1))
    type_grid = np.zeros(erosion_grid.shape)        # 0: rocky, 1: wet, 2: narrow
    max_x, max_y = erosion_grid.shape
    for x in range(max_x):
        for y in range(max_y):
            if (x, y) == (0, 0) or (x, y) == target:
                geologic_index = 0
            elif y == 0:
                geologic_index = 16807 * x
            elif x == 0:
                geologic_index = 48271 * y
            else:
                geologic_index = erosion_grid[x-1, y] * erosion_grid[x, y-1]
            erosion_level = (geologic_index + depth) % 20183
            erosion_grid[x, y] = erosion_level
            region_type = erosion_level % 3
            type_grid[x, y] = region_type

    print_grid(type_grid)
    print(int(sum(sum(type_grid))))






main()
