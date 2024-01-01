from typing import List, Tuple, Dict, Optional, Set, Union
import numpy as np


def get_input(filename) -> List[Tuple[Tuple[int], Tuple[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        pos_str, vel_str = line.split(' @ ')
        pos = tuple([int(val) for val in pos_str.split(',')])
        vel = tuple([int(val) for val in vel_str.split(',')])
        output.append((pos, vel))
    return output


def find_intersection(a: Tuple[List[int], List[int]], b: Tuple[List[int], List[int]]) -> Optional[Tuple[float, float]]:
    a_pos, a_vel = a
    b_pos, b_vel = b
    A = np.array([
        [a_vel[0], -b_vel[0]],
        [a_vel[1], -b_vel[1]]
    ])
    b = np.array([
        [b_pos[0] - a_pos[0]],
        [b_pos[1] - a_pos[1]]
    ])
    if np.linalg.det(A) == 0:
        return None
    t = np.linalg.inv(A) @ b
    return float(t[0]), float(t[1])


def evaluate(hailstone: Tuple[List[int], List[int]], t: float) -> List[float]:
    pos, vel = hailstone
    return [
        vel[0]*t + pos[0],
        vel[1]*t + pos[1],
        vel[2]*t + pos[2],
    ]


def paths_cross(a: Tuple[List[int], List[int]], b: Tuple[List[int], List[int]], min_val: float, max_val: float) -> int:
    t = find_intersection(a, b)
    if t is None:
        return 1
    if not all([_t > 0 for _t in t]):
        return 2
    pos = evaluate(a, t[0])
    if not all([min_val < p < max_val for p in pos[:2]]):
        return 3
    return 0


def main():
    hailstones = get_input('input.txt')
    min_val = 200000000000000  # 7
    max_val = 400000000000000  # 27
    total = 0
    for ii in range(len(hailstones)-1):
        for jj in range(1, len(hailstones)):
            a = hailstones[ii]
            b = hailstones[jj]
            t = find_intersection(a, b)
            # print('--------------------------')
            # print(a)
            # print(b)
            ret = paths_cross(a, b, min_val, max_val)
            if ret == 0:
                total += 1
                # print(evaluate(a, t[0])[:2])
                # print(evaluate(b, t[1])[:2])
            else:
                pass
                # print(f'Failed: {ret}')
    # print()
    print(total)


main()


#  Flood Fil Method

# def neighbors(pos: Tuple[int, int], width: int, height: int) -> List[Tuple[int, int]]:
#     output = []
#     r, c = pos
#     for nr in [r - 1, r, r + 1]:
#         for nc in [c - 1, c, c + 1]:
#             if (nr, nc) != pos and 0 <= nr < height and 0 <= nc < width:
#                 output.append((nr, nc))
#     return output

# def main():
#     instructions = get_input('input.txt')
#     directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
#     points = [(0, 0)]
#     for direction, value, color in instructions:
#         r, c = points[-1]
#         dr, dc = directions[direction]
#         new_points = [(r + ii*dr, c + ii*dc) for ii in range(1, value+1)]
#         points.extend(new_points)
#     min_r = min([point[0] for point in points])
#     min_c = min([point[1] for point in points])
#     for ii in range(len(points)):
#         point = points[ii]
#         point = (point[0] - (min_r - 2), point[1] - (min_c - 2))
#         points[ii] = point
#
#     height = max([point[0] for point in points]) + 2
#     width = max([point[1] for point in points]) + 2
#     visited_grid = [[False for _ in range(width)] for _ in range(height)]
#
#     iterations = 0
#     queue = [(0, 0)]
#     while queue:
#         if iterations % 10 == 0:
#             print(f'Queue: {len(queue)},\tIter: {iterations}')
#         iterations += 1
#         r, c = queue.pop(0)
#         visited_grid[r][c] = True
#         for neighbor in neighbors((r, c), width, height):
#             nr, nc = neighbor
#             if not visited_grid[nr][nc] and neighbor not in points + queue:
#                 queue.append(neighbor)
#
#     for r in range(height):
#         line = ''
#         for c in range(width):
#             line = line + ('#' if (r, c) in points else 'o' if visited_grid[r][c] else '.')
#         print(line)
#
#     print('Counting enclosed positions')
#     print(sum([sum([not value for value in row]) for row in visited_grid]))
