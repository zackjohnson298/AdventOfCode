from typing import List, Tuple, Dict, Optional, Set


def get_input(filename) -> List[Tuple[str, int, str]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        direction, value_str, color_str = line.split()
        color_str = color_str.replace(')', '')
        color_str = color_str.replace('(', '')
        output.append((direction, int(value_str), color_str))
    return output


def neighbors(pos: Tuple[int, int], width: int, height: int) -> List[Tuple[int, int]]:
    output = []
    r, c = pos
    for nr in [r - 1, r, r + 1]:
        for nc in [c - 1, c, c + 1]:
            if (nr, nc) != pos and 0 <= nr < height and 0 <= nc < width:
                output.append((nr, nc))
    return output


def main():
    instructions = get_input('input.txt')
    directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    points = [(0, 0)]
    for direction, value, color in instructions:
        r, c = points[-1]
        dr, dc = directions[direction]
        new_points = [(r + ii*dr, c + ii*dc) for ii in range(1, value+1)]
        points.extend(new_points)
    min_r = min([point[0] for point in points])
    min_c = min([point[1] for point in points])
    for ii in range(len(points)):
        point = points[ii]
        point = (point[0] - (min_r - 2), point[1] - (min_c - 2))
        points[ii] = point

    height = max([point[0] for point in points]) + 2
    width = max([point[1] for point in points]) + 2
    visited_grid = [[False for _ in range(width)] for _ in range(height)]

    iterations = 0
    queue = [(0, 0)]
    while queue:
        if iterations % 10 == 0:
            print(f'Queue: {len(queue)},\tIter: {iterations}')
        iterations += 1
        r, c = queue.pop(0)
        visited_grid[r][c] = True
        for neighbor in neighbors((r, c), width, height):
            nr, nc = neighbor
            if not visited_grid[nr][nc] and neighbor not in points + queue:
                queue.append(neighbor)

    for r in range(height):
        line = ''
        for c in range(width):
            line = line + ('#' if (r, c) in points else 'o' if visited_grid[r][c] else '.')
        print(line)

    print('Counting enclosed positions')
    print(sum([sum([not value for value in row]) for row in visited_grid]))
    # print()
    # print(max_r-min_r, max_c-min_c)

main()
