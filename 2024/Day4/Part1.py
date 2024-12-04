from typing import *


def get_input(filename: str) -> List[List[str]]:
    with open(filename) as file:
        lines = file.read().splitlines()
        return [[char for char in line] for line in lines]


def get_positions(pos: Tuple[int, int], size: Tuple[int, int]) -> List[List[Tuple[int, int]]]:
    output = []
    r, c = pos
    rows, cols = size
    # Right
    if c < cols - 3:
        output.append([(r, nc) for nc in range(c, c+4)])
        # Up Diag
        if r >= 3:
            output.append([(nr, nc) for nr, nc in zip(reversed(range(r-3, r+1)), range(c, c+4))])
        # Down Diag
        if r < rows-3:
            output.append([(nr, nc) for nr, nc in zip(range(r, r+4), range(c, c + 4))])
    # Left
    if c >= 3:
        output.append([(r, nc) for nc in range(c-3, c+1)])
        # Up Diag
        if r >= 3:
            output.append([(nr, nc) for nr, nc in zip(range(r-3, r+1), range(c-3, c+1))])
        # Down Diag
        if r < rows-3:
            output.append([(nr, nc) for nr, nc in zip(reversed(range(r, r+4)), range(c-3, c+1))])
    # Up
    if r >= 3:
        output.append([(nr, c) for nr in range(r - 3, r + 1)])
    # Down
    if r < rows - 3:
        output.append([(nr, c) for nr in range(r, r+4)])
    return output


def main():
    lines = get_input('input.txt')
    size = len(lines), len(lines[0])
    count = 0
    found_words = set()
    for r in range(size[0]):
        for c in range(size[1]):
            if lines[r][c] != 'X':
                continue
            sets = get_positions((r, c), size)
            for positions in sets:
                word = ''.join(lines[nr][nc] for nr, nc in positions)
                if word == 'XMAS':
                    found_words.add(tuple(positions))
                elif word == 'SAMX':
                    found_words.add(tuple(reversed(positions)))
    print(len(found_words))


main()
