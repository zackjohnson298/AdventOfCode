import numpy as np


def get_input():
    with open('input.txt') as file:
        lines = file.read().splitlines()
    segments = [[[int(value) for value in point.split(',')] for point in line.split(' -> ')] for line in lines]
    return segments


def generate_line(segment, shape):
    a, b = segment
    line = np.zeros(shape)
    if a[0] == b[0] or a[1] == b[1]:
        x1 = min((a[0], b[0]))
        x2 = max((a[0], b[0]))
        y1 = min((a[1], b[1]))
        y2 = max((a[1], b[1]))
        line[x1:x2 + 1, y1:y2 + 1] = np.ones((x2 - x1 + 1, y2 - y1 + 1))
    return line


def main():
    segments = get_input()
    max_x = max([max([point[0] for point in segment]) for segment in segments]) + 1
    max_y = max([max([point[1] for point in segment]) for segment in segments]) + 1

    grid = np.zeros((max_x, max_y))
    for segment in segments:
        line = generate_line(segment, grid.shape)
        grid += line

    print(sum(sum(grid >= 2)))


main()
