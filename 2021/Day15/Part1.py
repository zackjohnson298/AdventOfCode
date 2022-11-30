import numpy as np
from Graph import Graph
from PriorityQueue import PriorityQueue


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return np.array([[int(value) for value in line] for line in lines])


def heuristic(goal, pos):
    return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])


def main():
    grid = get_input('input.txt')
    graph = Graph(grid)
    start = (0, 0)
    goal_r, goal_c = graph.grid.shape
    goal_r -= 1
    goal_c -= 1
    goal = (goal_r, goal_c)

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

    total_risk = sum([graph.get_value(point) for point in path])
    print(total_risk)


main()
