from typing import *


def get_input(filename: str) -> List[List[str]]:
    with open(filename) as file:
        lines = file.read().splitlines()
        return [[char for char in line] for line in lines]


def get_positions(pos: Tuple[int, int], size: Tuple[int, int]) -> List[List[Tuple[int, int]]]:
    r, c = pos
    rows, cols = size
    if 0 < r < rows-1 and 0 < c < cols-1:
        return [[(nr, nc) for nr, nc in zip(range(r-1, r+2), range(c-1, c+2))], [(nr, nc) for nr, nc in zip(reversed(range(r-1, r+2)), range(c-1, c+2))]]
    return []


def main():
    lines = get_input('input.txt')
    size = len(lines), len(lines[0])
    count = 0
    for r in range(1, size[0]-1):
        for c in range(1, size[1]-1):
            if lines[r][c] != 'A':
                continue
            sets = get_positions((r, c), size)
            valid = False
            for positions in sets:
                word = ''.join(lines[nr][nc] for nr, nc in positions)
                if word not in ('MAS', 'SAM'):
                    break
            else:
                valid = True
            if valid:
                count += 1
    print(count)


main()
