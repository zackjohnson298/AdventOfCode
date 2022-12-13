import numpy as np
from PriorityQueue import PriorityQueue


class Graph:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.rows, self.cols = grid.shape

    def get_value(self, point):
        r, c = point
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r, c]
        return None

    def set_value(self, point, value):
        r, c = point
        if 0 <= r < self.rows and 0 <= c < self.cols:
            self.grid[r, c] = value

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
            return 1000000000
        elif next_value - current_value == 1:
            return 1
        else:
            return 1

    def find_path_A_star(self, start, goal):

        def heuristic(desired, pos):
            # return 0
            return abs(desired[0] - pos[0]) + abs(desired[1] - pos[1])

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {start: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break
            for next_pos in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, next_pos)
                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + heuristic(goal, next_pos)
                    frontier.put(next_pos, priority)
                    came_from[next_pos] = current

        path = []
        current = goal
        while current != start:
            path.insert(0, current)
            current = came_from[current]
        return path
