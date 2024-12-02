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
    return tr, tc


def main():
    steps = get_input('input.txt')
    head = (0, 0)
    tail = (0, 0)
    visited: Set[Tuple[int, int]] = {tail}
    for (dr, dc), count in steps:
        for _ in range(count):
            head = (head[0] + dr, head[1] + dc)
            tail = update_tail(head, tail)
            # print(head, tail)
            visited.add(tail)
    print(len(visited))

main()
