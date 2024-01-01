from typing import List, Tuple, Dict, Optional, Set, Union


class Path:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos
        self.history: Set[Tuple[int, int]] = set()

    def move(self, pos: Tuple[int, int]):
        self.history.add(self.pos)
        self.pos = pos

    def copy(self) -> 'Path':
        new_path = Path(self.pos)
        new_path.history = set(self.history)
        return new_path

    def __len__(self):
        return len(self.history)

    def __contains__(self, item):
        return item in self.history or item == self.pos


class Grid:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = (0, 1)
        self.end = (self.height-1, self.width-2)
        self.deltas = {
            '>': (0, 1),
            '<': (0, -1),
            'v': (1, 0),
            '^': (-1, 0)
        }

    def neighbors(self, pos: Tuple[int, int], path: Path) -> List[Tuple[int, int]]:
        r, c = pos
        char = self.grid[r][c]
        if char == '.':
            points = [
                (r-1, c),
                (r+1, c),
                (r, c-1),
                (r, c+1)
            ]
            output = []
            for nr, nc in points:
                if 0 < nr < self.height and 0 < nc < self.width and self.grid[nr][nc] != '#' and (nr, nc) not in path:
                    output.append((nr, nc))
            return output
        delta = self.deltas.get(char)
        if delta is None:
            raise Exception(f'Invalid character: {char} at {pos}')
        dr, dc = delta
        nr, nc = r+dr, c+dc
        if 0 < nr < self.height and 0 < nc < self.width and (nr, nc) not in path:
            return [(nr, nc)]
        return []

    def print(self):
        for r in range(self.height):
            line = ''
            for c in range(self.width):
                if (r, c) == self.start:
                    char = 'S'
                elif (r, c) == self.end:
                    char = 'E'
                else:
                    char = self.grid[r][c]
                line = line + char
            print(line)
        print()

    def find_longest_path(self) -> Path:
        def paths_compete(path_list: List[Path]) -> bool:
            return len(path_list) == 1 and path_list[0].pos == self.end

        paths: List[Path] = [Path(self.start)]
        while not paths_compete(paths):
            new_paths = []
            ended_paths = []
            for path in paths:
                pos = path.pos
                neighbors = self.neighbors(pos, path)
                if pos == self.end or len(neighbors) == 0:
                    ended_paths.append(path)
                elif len(neighbors) == 1:
                    path.move(neighbors[0])
                else:
                    for neighbor in neighbors[1:]:
                        new_path = path.copy()
                        new_path.move(neighbor)
                        new_paths.append(new_path)
                    path.move(neighbors[0])
            for ended_path in ended_paths:
                paths.remove(ended_path)
            for new_path in new_paths:
                paths.append(new_path)
        return paths[0]


def get_input(filename) -> Grid:
    with open(filename) as file:
        lines = file.read().splitlines()
    return Grid(lines)


def main():
    grid = get_input('input.txt')
    path = grid.find_longest_path()
    print(len(path))


main()
