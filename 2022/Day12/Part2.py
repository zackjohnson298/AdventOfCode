import numpy as np
from Graph import Graph


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return np.array([[value for value in line] for line in lines])


def get_valid_start_positions(graph: Graph, value, allowed_step_size=1):
    positions = graph.find_value(value)
    for position in reversed(positions):
        for neighbor in graph.neighbors(position):
            neighbor_value = graph.get_value(neighbor)
            if neighbor_value in [chr(ord(value) + step) for step in range(1, allowed_step_size+1)]:
                break
        else:
            positions.remove(position)
    return positions


def main():
    grid = get_input('input.txt')
    graph = Graph(grid)
    start = graph.find_value('S')[0]
    goal = graph.find_value('E')[0]

    graph.set_value(start, 'a')
    graph.set_value(start, 'z')
    starting_positions = get_valid_start_positions(graph, 'a')
    paths = {}

    for ii, starting_position in enumerate(starting_positions):
        print(f'{ii} / {len(starting_positions)}: {round(100*ii/len(starting_positions), 2)}%')
        paths[starting_position] = graph.find_path_A_star(starting_position, goal)

    for start_pos, path in paths.items():
        print(f'Start Pos: {start_pos}, length: {len(path)}')

    print()
    min_length = min([len(path) for path in paths.values()])
    print(min_length)


main()
