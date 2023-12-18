from typing import List, Tuple, Optional, Dict, Union
from PriorityQueue import PriorityQueue


def validate_path(sub_path: Union[Tuple[Tuple[int, int], ...], List[Tuple[int, int]]]) -> bool:
    if len(set(sub_path)) != len(sub_path):
        return False
    if len(sub_path) < 5:
        return True
    direction = None
    for ii in range(1, len(sub_path)):
        new_direction = (sub_path[ii][0] - sub_path[ii - 1][0], sub_path[ii][0] - sub_path[ii - 1][0])
        if direction and new_direction != direction:
            return True
        direction = new_direction
    return False


def heuristic(desired: Tuple[int, int], pos: Tuple[int, int]) -> float:
    return abs(desired[0] - pos[0]) + abs(desired[1] - pos[1])


class Graph:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_value(self, point: Tuple[int, int]):
        r, c = point
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c]
        return None

    def neighbors(self, point: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []
        r, c = point
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if nr not in (-1, self.rows) and nc not in (-1, self.cols):
                neighbors.append((nr, nc))
        return neighbors

    def cost(self, next_pos: Tuple[int, int]) -> int:
        return self.get_value(next_pos)

    def find_path_a_star(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        frontier = PriorityQueue()
        frontier.put(tuple([start]), 0)
        came_from: Dict[Tuple[Tuple[int, int]], Optional[Tuple[Tuple[int, int]]]] = {tuple([start]): None}
        cost_so_far: Dict[Tuple[Tuple[int, int]], int] = {tuple([start]): 0}
        sub_paths_to_end: List[Tuple[Tuple[int, int]]] = []

        while not frontier.empty():
            current_sub_path = frontier.get()
            current_pos = current_sub_path[-1]
            print('Frontier Size:', frontier.count)
            for neighbor_pos in self.neighbors(current_pos):
                new_sub_path = current_sub_path[-4:] + tuple([neighbor_pos])
                if not validate_path(new_sub_path):
                    continue
                if neighbor_pos == goal:
                    sub_paths_to_end.append(new_sub_path)
                new_cost = cost_so_far[current_sub_path] + self.cost(neighbor_pos)
                if new_sub_path not in cost_so_far or new_cost < cost_so_far[new_sub_path]:
                    cost_so_far[new_sub_path] = new_cost
                    priority = new_cost + heuristic(goal, neighbor_pos)
                    frontier.put(new_sub_path, priority)
                    came_from[new_sub_path] = current_sub_path
        min_score = float('inf')
        min_path = []
        for end_sub_path in sub_paths_to_end:
            sub_path = end_sub_path
            path = []
            while sub_path != tuple([start]):
                path.insert(0, sub_path[-1])
                sub_path = came_from.get(sub_path)
            score = sum([self.get_value(point) for point in path])
            if score < min_score:
                min_score = score
                min_path = path
        return min_path

    def print(self, path: Optional[List[Tuple[int, int]]] = None):
        if path is None:
            path = []
        for r in range(self.rows):
            line = ''
            for c in range(self.cols):
                if (r, c) in path:
                    char = '#'
                    previous_index = path.index((r, c)) - 1
                    if previous_index >= 0:
                        pr, pc = path[previous_index]
                        direction = (r - pr, c - pc)
                        if direction == (1, 0):
                            char = 'v'
                        elif direction == (-1, 0):
                            char = '^'
                        elif direction == (0, 1):
                            char = '>'
                        elif direction == (0, -1):
                            char = '<'
                    line = line + char
                else:
                    line = line + str(self.get_value((r, c)))
            print(line)
        print()


def get_input(filename: str) -> Graph:
    with open(filename) as file:
        lines = file.read().splitlines()
    lines = [[int(value) for value in line] for line in lines]
    return Graph(lines)


def main():
    grid = get_input('test_input.txt')
    start = (0, 0)
    goal = (grid.rows-1, grid.cols-1)
    path = grid.find_path_a_star(start, goal)
    path.insert(0, start)
    print('----------')
    grid.print(path=path)
    print('----------')
    print('Path Valid:', validate_path(path))
    print(sum([grid.get_value(point) for point in path[1:]]))


main()
