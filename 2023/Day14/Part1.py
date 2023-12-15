from typing import List, Tuple, Dict, Optional
import time


class Grid:
    def __init__(self, lines: List[str]):
        self.round_rocks: List[List[int, int]] = []
        self.fixed_rocks: List[List[int, int]] = []
        self.height = len(lines)
        self.width = len(lines[0])
        for r in range(self.height):
            for c in range(self.width):
                if lines[r][c] == '#':
                    self.fixed_rocks.append([r, c])
                elif lines[r][c] == 'O':
                    self.round_rocks.append([r, c])

    def tilt_north(self):
        for rock in sorted(self.round_rocks):
            while True:
                r, c = rock
                nr = r - 1
                if [nr, c] in self.round_rocks + self.fixed_rocks or nr < 0:
                    break
                rock[0] = nr

    @property
    def score(self) -> int:
        total = 0
        for r, c in self.round_rocks:
            total += self.height - r
        return total

    def print(self):
        for r in range(self.height):
            line = ''
            for c in range(self.width):
                line = line + ('#' if [r, c] in self.fixed_rocks else 'O' if [r, c] in self.round_rocks else '.')
            print(line)
        print()


def get_input(filename) -> Grid:
    with open(filename) as file:
        lines = file.read().splitlines()
    return Grid(lines)


def main():
    grid = get_input('input.txt')
    grid.tilt_north()
    print(grid.score)


main()
