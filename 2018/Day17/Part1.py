from typing import Tuple, List, Dict


class Grid:
    def __init__(self, lines: List[str]):
        self.grid


def get_input(filename: str) -> List[List[bool]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    blocks = []
    for line in lines:
        a_str, b_str = line.split(', ')
        a_axis, a_val_str = a_str.split('=')
        b_axis, b_range = b_str.split('=')
        b_lower, b_upper = b_range.split('..')
        if a_axis == 'x':
            for y in range(int(b_lower), int(b_upper)+1):
                blocks.append((int(a_val_str), y))
        else:
            for x in range(int(b_lower), int(b_upper) + 1):
                blocks.append((x, int(a_val_str)))
    min_x = min([block[0] for block in blocks]) - 1
    min_y = min([block[1] for block in blocks]) - 1
    max_x = max([block[0] for block in blocks]) + 1
    max_y = max([block[1] for block in blocks]) + 1
    print(min_x, min_y, max_x, max_y)
    return None


def main():
    grid = get_input('test_input.txt')


main()
