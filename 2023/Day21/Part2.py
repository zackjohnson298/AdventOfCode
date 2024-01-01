from typing import List, Tuple, Dict, Optional, Set, Union


Point = Tuple[int, int]


class Grid:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.start_pos: Optional[Point] = None
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == 'S':
                    self.start_pos = (r, c)
                    return
        raise Exception('Could not find starting position')

    def neighbors(self, point: Point) -> List[Point]:
        r, c = point
        new_points = [
            (r-1, c),
            (r+1, c),
            (r, c-1),
            (r, c+1)
        ]
        output = []
        for nr, nc in new_points:
            if self.grid[nr % self.height][nc % self.width] != '#':
                output.append((nr, nc))
        return output

    def print(self, o_points: List[Point] = ()):
        for r, row in enumerate(self.grid):
            string = ''
            for c, char in enumerate(row):
                string = string + ('O' if (r, c) in o_points else char)
            print(string)
        print()

    def find_spaces(self, max_length: int) -> int:
        queue: List[Point] = [self.start_pos]
        came_from: Dict[Point, Optional[Point]] = {self.start_pos: None}
        path_lengths: Dict[Point, int] = {self.start_pos: 0}
        valid_count = 0
        while queue:
            point = queue.pop(0)
            new_length = path_lengths[point] + 1
            if new_length > max_length:
                continue
            for neighbor in self.neighbors(point):
                if neighbor not in queue and neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = point
                    path_lengths[neighbor] = new_length
        return len([length for length in path_lengths.values() if length % 2 == max_length % 2])


def get_input(filename) -> List[str]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def main():
    lines = get_input('test_input.txt')
    grid = Grid(lines)
    max_count = 10
    print(grid.find_spaces(max_count))


main()