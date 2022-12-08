import numpy as np
from math import sqrt


def get_sum(pos, grid):
    r, c = pos
    total = 0
    for nr in [r - 1, r, r + 1]:
        for nc in [c - 1, c, c + 1]:
            total += grid[nr, nc]
    return total


def main():
    desired = 347991
    grid = np.zeros((int(sqrt(desired/2)), int(sqrt(desired/2))), dtype='int')
    pos = np.array([0, 0])
    grid[tuple(pos)] = 1
    m = np.array([[0, -1], [1, 0]])
    direction = np.array([1, 0])
    pos = np.array([0, 0])
    ii = 1
    done = False
    for steps in range(1, desired):
        for _ in range(2):
            for step in range(steps):
                total = get_sum(pos, grid)
                grid[tuple(pos)] = get_sum(pos, grid)
                if total >= desired:
                    print(pos, total)
                    done = True
                    break
                pos += direction
                ii += 1
            direction = m @ direction
            if done:
                break
        if done:
            break


main()
