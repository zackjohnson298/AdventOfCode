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

    def reflect_points(self, index: int, axis: int, smudge: Optional[Tuple[int, int]] = None) -> List[Tuple[int, int]]:
        assert axis in (0, 1)
        ref_points = []
        # Vertical
        points = list(self.points)
        if smudge:
            if smudge in self.points:
                points.remove(smudge)
            else:
                points.append(smudge)
        if axis == 1:
            assert 0 < index < self.width
            for r, c in points:
                delta = 2*(c - index) + 1
                new_c = c - delta
                if 0 <= new_c < self.width:
                    ref_points.append((r, new_c))
        # Horizontal
        else:
            assert 0 < index < self.height
            for r, c in points:
                delta = 2*(r - index) + 1
                new_r = r - delta
                if 0 <= new_r < self.height:
                    ref_points.append((new_r, c))
        return ref_points

    @property
    def score(self) -> int:
        return sum([100*c for c in self.hor_refs]) + sum(self.vert_refs)

    def find_reflection(self, smudge: Optional[Tuple[int, int]] = None) -> Tuple[List[int], List[int]]:
        # Vertical
        vertical = []
        horizontal = []
        for c in range(1, self.width):
            new_points = self.reflect_points(c, axis=1, smudge=smudge)
            if all([point in self.points for point in new_points]):
                vertical.append(c)
        # Horizontal
        for r in range(1, self.height):
            new_points = self.reflect_points(r, axis=0, smudge=smudge)
            if all([point in self.points for point in new_points]):
                horizontal.append(r)
        return vertical, horizontal

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
    original = [grid.find_reflection() for grid in grids]
    diff = []
    for ii, grid in enumerate(grids):
        done = False
        orig = original[ii]
        for r in range(grid.height):
            for c in range(grid.width):
                new = grid.find_reflection(smudge=(r, c))
                if new and any(new) and orig != new:
                    new_vert = set(new[1]).difference(orig[1])
                    new_hor = set(new[0]).difference(orig[0])
                    print(new_vert, new_hor)
                    original[ii] = (sum(new_vert), sum(new_hor))
                    done = True
                    break
            if done:
                break
        else:
            raise Exception('Failed to find new reflection')
    print(original)
    for r, c in original:
        total += 100*r + c
    print(total)


main()
