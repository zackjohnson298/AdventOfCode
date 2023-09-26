import numpy as np
from Graph import Graph


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return np.array([[value for value in line] for line in lines])


def main():
    grid = get_input('input.txt')
    graph = Graph(grid)
    start = graph.find_value('S')[0]
    goal = graph.find_value('E')[0]

    graph.set_value(start, 'a')
    graph.set_value(start, 'z')

    path = graph.find_path_A_star(start, goal)

    print(len(path))


main()
