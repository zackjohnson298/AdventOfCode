import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    claims = {}
    for line in lines:
        claim_id, claim_string = line.split(' @ ')
        start_string, size_string = claim_string.split(': ')
        x_start, y_start = [int(value) for value in start_string.split(',')]
        x_size, y_size = [int(value) for value in size_string.split('x')]
        claims[int(claim_id[1:])] = ((x_start, y_start), (x_size, y_size))
    return claims


def main():
    claims = get_input('input.txt')
    max_x = max([pos[0] + size[0] + 1 for pos, size in claims.values()])
    max_y = max([pos[1] + size[1] + 1 for pos, size in claims.values()])
    grid = np.zeros((max_x, max_y))

    for (x_start, y_start), (x_size, y_size) in claims.values():
        x_end = x_start + x_size
        y_end = y_start + y_size
        grid[x_start:x_end, y_start:y_end] += np.ones((x_size, y_size))

    for claim_id, ((x_start, y_start), (x_size, y_size)) in claims.items():
        x_end = x_start + x_size
        y_end = y_start + y_size
        if sum(sum(grid[x_start:x_end, y_start:y_end] - np.ones((x_size, y_size)))) == 0:
            print(claim_id)

    # print(sum(sum(grid >= 2)))



main()
