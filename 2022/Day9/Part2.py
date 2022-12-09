import json
import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    instructions = []
    for line in lines:
        a, b = line.split()
        instructions.append([a, int(b)])
    return instructions


def update_tail_pos(head_pos, tail_pos):
    diff = head_pos - tail_pos
    if (np.abs(diff) <= np.array([1, 1])).all():
        return tail_pos
    if diff[0] == 0:
        if diff[1] > 0:
            tail_pos += np.array([0, 1])
        else:
            tail_pos += np.array([0, -1])
    elif diff[1] == 0:
        if diff[0] > 0:
            tail_pos += np.array([1, 0])
        else:
            tail_pos += np.array([-1, 0])
    else:
        diff = np.array([int(diff[0]/abs(diff[0])), int(diff[1]/abs(diff[1]))])
        tail_pos += diff
    return tail_pos


def main():
    instructions = get_input('input.txt')
    segments = 10
    directions = {
        'U': np.array([0, 1]),
        'D': np.array([0, -1]),
        'L': np.array([-1, 0]),
        'R': np.array([1, 0])
    }
    rope = [np.array([0, 0]) for _ in range(segments)]
    visited = [tuple(rope[-1])]
    for direction, value in instructions:
        for step in range(value):
            rope[0] += directions[direction]
            for ii in range(1, len(rope)):
                rope[ii] = update_tail_pos(rope[ii-1], rope[ii])
            if tuple(rope[-1]) not in visited:
                visited.append(tuple(rope[-1]))
    print(len(visited))


main()
