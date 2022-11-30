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

    def cost(self, current, next_pos):
        r, c = current
        nr, nc = next_pos
        return self.grid[nr, nc]
