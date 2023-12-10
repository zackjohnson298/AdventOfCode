from typing import List, Optional, Tuple


class Grid:
    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def get_value(self, pos: Tuple[int, int]) -> Optional[str]:
        r, c = pos
        if not (0 <= r < self.height) or not (0 <= c < self.width):
            return None
        return self.grid[r][c]

    def neighbors(self, pos: Tuple[int, int]) -> List[str]:
        r, c = pos
        neighbors = []
        for nr in (r-1, r, r+1):
            for nc in (c-1, c, c+1):
                if (nr, nc) == (r, c):
                    continue
                val = self.get_value((nr, nc))
                if val is not None:
                    neighbors.append(val)
        return neighbors

    @property
    def occupied_seats(self) -> int:
        return sum([sum([1 if val == '#' else 0 for val in row]) for row in self.grid])

    def print(self):
        for row in self.grid:
            print(''.join(char for char in row))
        print()

    def compare(self, grid: List[List[str]]) -> bool:
        if len(grid) != self.height or len(grid[0]) != self.width:
            raise Exception('Grid sizes do not mathc!')
        for row, new_row in zip(self.grid, grid):
            for val, new_val in zip(row, new_row):
                if val != new_val:
                    return False
        return True

    def update(self) -> bool:
        new_grid = [[char for char in row] for row in self.grid]
        for r in range(self.height):
            for c in range(self.width):
                val = self.get_value((r, c))
                if val == '.':
                    continue
                neighbors = self.neighbors((r, c))
                if val == 'L' and neighbors.count('#') == 0:
                    new_grid[r][c] = '#'
                elif val == '#' and neighbors.count('#') >= 4:
                    new_grid[r][c] = 'L'
        output = self.compare(new_grid)
        self.grid = new_grid
        return output


def get_input(filename) -> List[List[str]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[char for char in line] for line in lines]


def main():
    lines = get_input('input.txt')
    grid = Grid(lines)
    while not grid.update():
        pass
    print(grid.occupied_seats)


main()
