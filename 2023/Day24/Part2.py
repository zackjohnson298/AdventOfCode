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

    def neighbors(self, pos: Tuple[int, int], path: Path) -> List[Tuple[int, int]]:
        r, c = pos
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

    def print(self, paths: Optional[List[Path]] = None):
        for r in range(self.height):
            line = ''
            for c in range(self.width):
                if (r, c) == self.start:
                    char = 'S'
                elif (r, c) == self.end:
                    char = 'E'
                elif paths and any([(r, c) in path for path in paths]):
                    char = 'o'
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
            # self.print(paths)
            # _ = input(f'{len(paths)} continue: ')
            new_paths = []
            ended_paths = []
            for path in paths:
                pos = path.pos
                # if pos == (5, 3):
                #     print()
                neighbors = self.neighbors(pos, path)
                if pos == self.end or len(neighbors) == 0:
                    if pos == self.end:
                        print(len(paths), len(path))
                    ended_paths.append(path)
                elif len(neighbors) == 1:
                    path.move(neighbors[0])
                else:
                    for neighbor in neighbors[1:]:
                        new_path = path.copy()
                        new_path.move(neighbor)
                        new_paths.append(new_path)
                    path.move(neighbors[0])
            if len(paths) == 0:
                print('DONE --------------------')
                break
            for new_path in new_paths:
                paths.append(new_path)
            for ended_path in ended_paths:
                if not paths_compete(paths):
                    paths.remove(ended_path)
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
