import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    points = []
    steps = []
    line = lines.pop(0)
    while len(line) > 0:
        points.append([int(value) for value in line.split(',')])
        line = lines.pop(0)
    for line in lines:
        step = []
        if 'x' in line:
            step.append('left')
        else:
            step.append('up')
        step.append(int(line.split('=')[1]))
        steps.append(step)
    return points, steps


def print_points(points):
    max_x = max([point[0] for point in points]) + 1
    max_y = max([point[1] for point in points]) + 1
    for y in range(max_y):
        for x in range(max_x):
            if [x, y] in points:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def main():
    points, steps = get_input('input.txt')
    for direction, value in steps:
        new_points = []
        for point in reversed(points):
            x, y = point
            if direction == 'left' and x > value:
                new_point = [value - (x - value), y]
                points.remove(point)
                if new_point not in points:
                    new_points.append(new_point)
            elif direction == 'up' and y > value:
                points.remove(point)
                new_point = [x, value - (y - value)]
                if new_point not in points:
                    new_points.append(new_point)
        points += new_points
    print_points(points)


main()
