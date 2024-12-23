from typing import List, Tuple, Dict, Optional, Set
import numpy as np


class Beam:
    def __init__(self, start_pos: Tuple[int, int], direction: Tuple[int, int], max_r: int, max_c: int):
        # self.points: List[Tuple[int, int]] = [start_pos]
        self.pos = start_pos
        self.last_pos = None
        self.direction = direction
        self.max_r = max_r
        self.max_c = max_c

    def move(self) -> bool:
        r, c = self.pos
        dr, dc = self.direction
        nr = r + dr
        nc = c + dc
        if 0 <= nr < self.max_r and 0 <= nc < self.max_c:
            self.last_pos = self.pos
            self.pos = (nr, nc)
            return True
        return False

    def set_direction(self, new_direction: Tuple[int, int]):
        self.direction = new_direction


class Mirror:
    def __init__(self, kind: str, pos: Tuple[int, int]):
        self.kind = kind
        self.pos = pos

    def interact(self, beam: Beam):
        assert beam.pos == self.pos
        if beam.direction == (0, 1):    # right
            new_direction = (-1, 0) if self.kind == '/' else (1, 0)
            beam.set_direction(new_direction)
        elif beam.direction == (0, -1):   # left
            new_direction = (1, 0) if self.kind == '/' else (-1, 0)
            beam.set_direction(new_direction)
        elif beam.direction == (-1, 0):   # up
            new_direction = (0, 1) if self.kind == '/' else (0, -1)
            beam.set_direction(new_direction)
        elif beam.direction == (1, 0):    # down
            new_direction = (0, -1) if self.kind == '/' else (0, 1)
            beam.set_direction(new_direction)


class Splitter:
    def __init__(self, kind: str, pos: Tuple[int, int]):
        self.kind = kind
        self.pos = pos

    def interact(self, beam: Beam) -> Optional[Beam]:
        assert beam.pos == self.pos
        if beam.direction in ((0, 1), (0, -1)):    # right/left
            if self.kind == '|':
                beam.set_direction((-1, 0))
                new_beam = Beam(self.pos, (1, 0), beam.max_r, beam.max_c)
                return new_beam
        elif beam.direction in ((1, 0), (-1, 0)):  # down/up
            if self.kind == '-':
                beam.set_direction((0, -1))
                new_beam = Beam(self.pos, (0, 1), beam.max_r, beam.max_c)
                return new_beam
        else:
            raise Exception(f'Unhandled Splitter direction: {beam.direction}')


class Grid:
    def __init__(self, lines: List[str]):
        self.height = len(lines)
        self.width = len(lines[0])
        self.beams: List[Beam] = [Beam((0, -1), (0, 1), self.height, self.width)]
        self.history: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        self.energized_points: Set[Tuple[int, int]] = set()
        self.mirrors: Dict[Tuple[int, int], Mirror] = {}
        self.splitters: Dict[Tuple[int, int], Splitter] = {}
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == '.':
                    continue
                elif char in '-|':
                    self.splitters[(r, c)] = Splitter(char, (r, c))
                else:
                    self.mirrors[(r, c)] = Mirror(char, (r, c))

    def update(self):
        new_beams: List[Beam] = []
        beams_to_remove = []
        for beam in self.beams:
            if beam.move():
                mirror = self.mirrors.get(beam.pos)
                splitter = self.splitters.get(beam.pos)
                if mirror:
                    mirror.interact(beam)
                elif splitter:
                    new_beam = splitter.interact(beam)
                    if new_beam and (new_beam.pos, new_beam.direction) not in self.history:
                        new_beams.append(new_beam)
                        self.energized_points.add(new_beam.pos)
                self.energized_points.add(beam.pos)
                if (beam.pos, beam.direction) in self.history:
                    beams_to_remove.append(beam)
                else:
                    self.history.append((beam.pos, beam.direction))
            else:
                beams_to_remove.append(beam)
        for beam in beams_to_remove:
            self.beams.remove(beam)
        self.beams.extend(new_beams)

    def print(self):
        for r in range(self.height):
            line = ''
            for c in range(self.width):
                if (r, c) in self.energized_points:
                    line = line + '#'
                else:
                    mirror = self.mirrors.get((r, c))
                    if mirror:
                        line = line + mirror.kind
                        continue
                    splitter = self.splitters.get((r, c))
                    if splitter:
                        line = line + splitter.kind
                        continue
                    line = line + '.'
            print(line)
        print()


def get_input(filename) -> Grid:
    with open(filename) as file:
        lines = file.read().splitlines()
    return Grid(lines)


def main():
    grid = get_input('input.txt')
    while grid.beams:
        grid.update()
    print(len(grid.energized_points))


main()
