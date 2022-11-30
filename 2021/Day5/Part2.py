import numpy as np


def get_input():
    with open('input.txt') as file:
        lines = file.read().splitlines()
    segments = [[[int(value) for value in point.split(',')] for point in line.split(' -> ')] for line in lines]
    return segments


def generate_line(segment, shape):
    (x1, y1), (x2, y2) = segment
    line = np.zeros(shape, dtype='int')
    x_dir = int((x2 - x1) / abs(x2 - x1)) if x2 != x1 else 0
    y_dir = int((y2 - y1) / abs(y2 - y1)) if y2 != y1 else 0
    direction = np.array([x_dir, y_dir], dtype='int')
    pos = np.array([x1, y1])
    line[pos[0], pos[1]] = 1
    while np.linalg.norm(pos - np.array([x2, y2])) > 0.1:
        pos += direction
        line[pos[0], pos[1]] = 1
    return line


def print_grid(grid):
    for row in grid.T:
        for value in row:
            print(value if value > 0 else '.', end='')
        print()


def main():
    segments = get_input()
    max_x = max([max([point[0] for point in segment]) for segment in segments]) + 1
    max_y = max([max([point[1] for point in segment]) for segment in segments]) + 1

    grid = np.zeros((max_x, max_y), dtype='int')
    for segment in segments:
        line = generate_line(segment, grid.shape)
        grid += line

    # print_grid(grid)
    print(sum(sum(grid >= 2)))


main()
