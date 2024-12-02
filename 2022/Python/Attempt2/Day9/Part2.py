from typing import *
import json


def get_input(filename: str) -> List[Tuple[Tuple[int, int], int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    directions = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    for line in lines:
        direction, count = line.split()
        output.append((directions[direction], int(count)))
    return output


def update_tail(head_pos: Tuple[int, int], tail_pos: Tuple[int, int]) -> Tuple[int, int]:
    hr, hc = head_pos
    tr, tc = tail_pos
    r_dist = hr - tr
    c_dist = hc - tc

    if abs(r_dist) == 2:
        tc = hc
        tr = hr - int(r_dist / 2)
    elif abs(c_dist) == 2:
        tr = hr
        tc = hc - int(c_dist / 2)
    elif abs(r_dist) not in (1, 0) or abs(c_dist) not in (1, 0):
        raise Exception(f'{r_dist}, {c_dist}')

    return tr, tc


def main():
    steps = get_input('test_input2.txt')
    length = 10
    rope = [(0, 0) for _ in range(length)]
    visited: Set[Tuple[int, int]] = {rope[-1]}
    for (dr, dc), count in steps:
        for _ in range(count):
            rope[0] = (rope[0][0] + dr, rope[0][1] + dc)
            for ii in range(1, len(rope)):
                rope[ii] = update_tail(rope[ii-1], rope[ii])
            # print(rope)
            visited.add(rope[-1])
    print(visited)
    rmin = min([point[0] for point in visited]) - 9
    rmax = max([point[0] for point in visited])
    cmin = min([point[1] for point in visited])
    cmax = max([point[1] for point in visited]) + 4
    # print(rmin, rmax, cmin, cmax)
    for r in range(rmin, rmax+1):
        line = ''
        for c in range(cmin, cmax+1):
            line = line + ('#' if (r, c) in visited else '.')
        print(line)
    print(len(visited))


main()
