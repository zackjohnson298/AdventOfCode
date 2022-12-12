import numpy as np
from Graph import Graph
from PriorityQueue import PriorityQueue
import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return np.array([[value for value in line] for line in lines])


def find_item(grid, value):
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == value:
                return r, c
    return None


def heuristic(goal, pos):
    return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])


def get_path(graph: Graph, start, goal):

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next_pos in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_pos)
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


def get_reduced_positions(graph: Graph, value):
    positions = graph.find_value(value)
    for position in reversed(positions):
        for neighbor in graph.neighbors(position):
            new_value = graph.get_value(neighbor)
            if new_value != value:
                break
        else:
            positions.remove(position)
    return positions


def main():
    grid = get_input('input.txt')
    start = find_item(grid, 'S')
    goal = find_item(grid, 'E')

    grid[start] = 'a'
    grid[goal] = 'z'
    graph = Graph(grid)
    starting_positions = get_reduced_positions(graph, 'a')
    paths = {}
    print(len(starting_positions))
    for ii, starting_position in enumerate(starting_positions):
        print(f'{ii} / {len(starting_positions)}: {round(100*ii/len(starting_positions), 4)}%')
        path = get_path(graph, starting_position, goal)
        paths[starting_position] = len(path)

    for key, value in paths.items():
        print(key, value)

    print()
    print(min(paths.values()))



main()
