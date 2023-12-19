from typing import List, Tuple, Dict, Optional, Set


def get_input(filename) -> List[Tuple[str, int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    directions = 'RDLU'
    for line in lines:
        instruction_str = line.split()[-1]
        instruction_str = instruction_str.replace(')', '')
        instruction_str = instruction_str.replace('(#', '')
        value = int(instruction_str[:-1], 16)
        direction = directions[int(instruction_str[-1])]
        output.append((direction, value))
    return output


def get_area(vertices: List[Tuple[int, int]]) -> int:
    total = 0
    for ii in range(1, len(vertices)):
        x1, y1 = vertices[ii-1]
        x2, y2 = vertices[ii]
        total += (x1*y2 - y1*x2)
    total /= 2
    return abs(total)


def main():
    instructions = get_input('input.txt')
    directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    points = [(0, 0)]
    perimeter = 0
    for direction, value in instructions:
        r, c = points[-1]
        perimeter += value
        dr, dc = directions[direction]
        new_point = (r + value*dr, c + value*dc)
        points.append(new_point)
    area = get_area(points) + (perimeter - 2)/2 + 2
    print(area)


main()
