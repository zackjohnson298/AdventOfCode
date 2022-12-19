import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    points = []
    for line in lines:
        line = line.replace('position=', '')
        line = line.replace('<', '')
        line = line.replace('>', '')
        pos_string, vel_string = line.split(' velocity=')
        pos = tuple([int(value) for value in pos_string.split(', ')])
        vel = tuple([int(value) for value in vel_string.split(', ')])
        point = {
            'pos': pos,
            'vel': vel
        }
        points.append(point)
    return points


def update_point(point):
    pos_vec = np.array(point['pos'])
    vel_vec = np.array(point['vel'])
    pos_vec += vel_vec
    point['pos'] = tuple(pos_vec)


def print_grid(grid):
    for row in grid.T:
        for value in row:
            if value == 1:
                print('##', end='')
            else:
                print('..', end='')
        print()
    print()


def create_grid(points):
    min_x = min([point['pos'][0] for point in points])
    min_y = min([point['pos'][1] for point in points])
    max_x = max([point['pos'][0] for point in points]) + 1
    max_y = max([point['pos'][1] for point in points]) + 1

    grid = np.zeros((max_x-min_x, max_y-min_y))
    for point in points:
        x, y = point['pos']
        grid[x-min_x, y-min_y] = 1
    return grid


def detect_line(points, length=6):
    positions = [point['pos'] for point in points]
    for x, y in positions:
        count = 0
        for dy in range(1, length+1):
            new_pos = (x, y+dy)
            if new_pos not in positions:
                break
        else:
            return True
    return False


def main():
    points = get_input('input.txt')
    count = 0
    grid = create_grid(points)
    # print(count)
    # print_grid(grid)
    # print(detect_line(points))
    # _ = input()
    done = False
    while not done:
        count += 1
        print(count)
        for point in points:
            update_point(point)
        if detect_line(points):
            grid = create_grid(points)
            print(count)
            print_grid(grid)
            print(detect_line(points, length=3))
            _ = input()
    # for point in points:
    #     print(point)

main()
