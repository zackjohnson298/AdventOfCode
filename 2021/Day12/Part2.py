import json
import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    connections = {}
    for line in lines:
        a, b = line.split('-')
        connections[a] = connections[a] + [b] if a in connections else [b]
        connections[b] = connections[b] + [a] if b in connections else [a]
    for cave, options in connections.items():
        if 'end' in options:
            options.remove('end')
            options.append('end')
            connections[cave] = options
    return connections


def can_go_to_cave(next_cave, current_path):
    if next_cave != 'start':
        new_path = current_path + [next_cave]
        small_cave_counts = {cave: new_path.count(cave) for cave in set(new_path) if cave.islower()}
        if sum(np.array(list(small_cave_counts.values())) >= 2) <= 1 and max(small_cave_counts.values()) <= 2:
            return True
    return False


def navigate(paths, current_path, connections):
    options = connections[current_path[-1]]
    for next_cave in options:
        if can_go_to_cave(next_cave, current_path):
            new_path = current_path + [next_cave]
            if next_cave == 'end':
                paths.append(new_path)
                return
            navigate(paths, new_path, connections)


def main():
    connections = get_input('input.txt')
    paths = []
    navigate(paths, ['start'], connections)
    # for path in paths:
    #     print(path)
    # print()
    print(len(paths))


main()
