import numpy as np


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    # line = 'R8, R4, R4, R8'
    steps = [[step[0], int(step[1:])] for step in line.split(', ')]
    return steps


def rot(angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])


def main():
    steps = get_input('input.txt')
    turns = {'L': rot(np.pi/2), 'R': rot(-np.pi/2)}
    direction = np.array([0., 1.]).T
    pos = np.array([0., 0.]).T
    visited = []
    # while not done:
    for jj, (turn, distance) in enumerate(steps):
        direction = turns[turn] @ direction
        done = False
        for ii in range(distance):
            pos += direction
            if [int(value) for value in np.round(pos).tolist()] not in visited:
                visited.append([int(value) for value in np.round(pos).tolist()])
            else:
                done = True
                break
        if done:
            break
    print(int(sum(np.abs(np.round(pos)))))


main()
