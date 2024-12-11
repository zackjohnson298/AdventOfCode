from typing import *


def get_input(filename: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = [[int(value) for value in line] for line in lines]
    zeros = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]
    return zeros, [[int(value) for value in line] for line in lines]


def neighbors(pos: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    r, c = pos
    output = []
    if r < rows-1:
        output.append((r+1, c))
    if 0 < r:
        output.append((r-1, c))
    if c < cols-1:
        output.append((r, c+1))
    if 0 < c:
        output.append((r, c-1))
    return output


def navigate(pos: Tuple[int, int], grid: List[List[int]], paths: List[List[Tuple[int, int]]], current_path: Optional[List[Tuple[int, int]]] = None):
    if current_path is None:
        current_path = [pos]
    r, c = pos
    value = grid[r][c]
    if value == 9:
        paths.append(current_path)
        return
    for nr, nc in neighbors(pos, grid):
        new_value = grid[nr][nc]
        if new_value == value + 1:
            new_path = current_path + [(nr, nc)]
            navigate((nr, nc), grid, paths, new_path)


def main():
    zeros, grid = get_input('input.txt')
    total = 0
    for zero in zeros:
        paths = []
        navigate(zero, grid, paths)
        total += len(paths)
    print(total)


main()
