from typing import List, Tuple, Dict, Optional


class Grid:
    def __init__(self, lines: List[str]):
        self.points: List[Tuple[int, int]] = []
        self.height = len(lines)
        self.width = len(lines[0])
        self.hor_refs: List[int] = []
        self.vert_refs: List[int] = []
        for r in range(self.height):
            for c in range(self.width):
                if lines[r][c] == '#':
                    self.points.append((r, c))

    def reflect_points(self, index: int, axis: int) -> List[Tuple[int, int]]:
        assert axis in (0, 1)
        points = []
        # Vertical
        if axis == 1:
            assert 0 < index < self.width
            for r, c in self.points:
                delta = 2*(c - index) + 1
                new_c = c - delta
                if 0 <= new_c < self.width:
                    points.append((r, new_c))
        # Horizontal
        else:
            assert 0 < index < self.height
            for r, c in self.points:
                delta = 2*(r - index) + 1
                new_r = r - delta
                if 0 <= new_r < self.height:
                    points.append((new_r, c))
        return points

    @property
    def score(self) -> int:
        return sum([100*c for c in self.hor_refs]) + sum(self.vert_refs)

    def find_reflection(self) -> Tuple[Optional[int], Optional[int]]:
        # Vertical
        for c in range(1, self.width):
            new_points = self.reflect_points(c, axis=1)
            if all([point in self.points for point in new_points]):
                return None, c
        # Horizontal
        for r in range(1, self.height):
            new_points = self.reflect_points(r, axis=0)
            if all([point in self.points for point in new_points]):
                return r, None

    def print(self):
        print(self.find_reflection())
        for r in range(self.height):
            line = ''
            for c in range(self.width):
                line = line + ('#' if (r, c) in self.points else '.')
            print(line)
        print('---------------')
        print()


def get_input(filename) -> List[Grid]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    group = []
    for line in lines:
        if line:
            group.append(line)
        else:
            output.append(Grid(group))
            group = []
    if group:
        output.append(Grid(group))
    return output


def main():
    grids = get_input('input.txt')
    total = 0
    for grid in grids:
        # grid.print()
        r, c = grid.find_reflection()
        total += 100*r if r else c
    print(total)

main()
