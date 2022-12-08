import numpy as np


def main():
    desired = 347991
    pos = np.array([0, 0])
    m = np.array([[0, -1], [1, 0]])
    items = {}
    direction = np.array([1, 0])
    pos = np.array([0, 0])
    ii = 1
    done = False
    for steps in range(1, desired):
        for _ in range(2):
            for step in range(steps):
                items[ii] = pos.tolist()
                if ii == desired:
                    done = True
                    break
                pos += direction
                ii += 1
            direction = m @ direction
            if done:
                break
        if done:
            break
    print(desired, items[desired], sum([abs(value) for value in items[desired]]))


main()
