import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    ranges = []
    for line in lines:
        line = line.split('@ ')[1]
        start_string, size_string = line.split(': ')
        x_start, y_start = [int(value) for value in start_string.split(',')]
        x_size, y_size = [int(value) for value in size_string.split('x')]
        ranges.append(((x_start, y_start), (x_size, y_size)))
    return ranges


def main():
    ranges = get_input('input.txt')
    max_x = max([pos[0] + size[0] + 1 for pos, size in ranges])
    max_y = max([pos[1] + size[1] + 1 for pos, size in ranges])
    grid = np.zeros((max_x, max_y))

    for (x_start, y_start), (x_size, y_size) in ranges:
        x_end = x_start + x_size
        y_end = y_start + y_size
        # print(grid[x_start:x_end, y_start:y_end].shape)
        # print(np.ones((x_size+1, y_size+1)).shape)

        grid[x_start:x_end, y_start:y_end] += np.ones((x_size, y_size))

    print(sum(sum(grid >= 2)))



main()
