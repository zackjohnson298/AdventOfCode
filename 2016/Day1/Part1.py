import numpy as np


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    # line = 'R5, L5, R5, R3'
    steps = [[step[0], int(step[1:])] for step in line.split(', ')]
    return steps


def rot(angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])


def main():
    steps = get_input('input.txt')
    turns = {'L': rot(np.pi/2), 'R': rot(-np.pi/2)}
    direction = np.array([0., 1.]).T
    pos = np.array([0., 0.]).T
    for turn, distance in steps:
        direction = turns[turn] @ direction
        pos += distance * direction
    print(int(sum(np.abs(np.round(pos)))))


main()
