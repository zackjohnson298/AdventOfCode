import numpy as np


def roty(vec, angle):
    vec = np.array(vec, dtype='int').T
    angle = np.pi * angle / 180
    m = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ], dtype='int')
    vec = m @ vec
    return tuple(vec)


class Cart:
    def __init__(self, char: str, pos: (int, int), cart_id: int):
        self.pos = pos
        self.intersection_count = 0
        self.id = cart_id
        if char == '>':
            self.dir = (0, 1)
        elif char == '<':
            self.dir = (0, -1)
        elif char == '^':
            self.dir = (-1, 0)
        elif char == 'v':
            self.dir = (1, 0)
        self.next_pos = tuple(np.array(self.pos, dtype='int') + np.array(self.dir, dtype='int'))

    def move(self):
        self.pos = self.next_pos

    def update(self, next_track_type):
        self.move()
        if next_track_type == '\\':
            if self.dir == (1, 0):      # From Top
                self.dir = (0, 1)
            elif self.dir == (0, 1):    # From Left
                self.dir = (1, 0)
            elif self.dir == (-1, 0):    # From Bottom
                self.dir = (0, -1)
            elif self.dir == (0, -1):    # From Right
                self.dir = (-1, 0)
            else:
                raise ValueError(f'Unhandled direction change: pos: {self.pos}, dir: {self.dir}, type: {next_track_type}')
        elif next_track_type == '/':
            if self.dir == (1, 0):      # From Top
                self.dir = (0, -1)
            elif self.dir == (0, 1):    # From Left
                self.dir = (-1, 0)
            elif self.dir == (-1, 0):    # From Bottom
                self.dir = (0, 1)
            elif self.dir == (0, -1):    # From Right
                self.dir = (1, 0)
            else:
                raise ValueError(f'Unhandled direction change: pos: {self.pos}, dir: {self.dir}, type: {next_track_type}')
        elif next_track_type == '+':
            if self.intersection_count == 0:
                self.dir = roty(self.dir, 90)
            elif self.intersection_count == 2:
                self.dir = roty(self.dir, -90)
            self.intersection_count = (self.intersection_count + 1) % 3
        self.next_pos = tuple(np.array(self.pos, dtype='int') + np.array(self.dir, dtype='int'))



class Track:
    def __init__(self, char, pos):
        self.type = char
        self.pos = pos
