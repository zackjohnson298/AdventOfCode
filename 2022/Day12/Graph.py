import numpy as np


class Graph:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.rows, self.cols = grid.shape

    def get_value(self, point):
        r, c = point
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r, c]
        return None

    def neighbors(self, point):
        neighbors = []
        r, c = point
        for nr, nc in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if nr not in [-1, self.rows] and nc not in [-1, self.cols]:
                neighbors.append((nr, nc))
        return neighbors

    def find_value(self, value):
        positions = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r, c] == value:
                    positions.append((r, c))
        return positions

    def cost(self, current, next_pos):
        current_value = ord(self.grid[current])
        next_value = ord(self.grid[next_pos])
        if next_value - current_value > 1:
            return 100000
        elif next_value - current_value == 1:
            return 1
        else:
            return 20
