from typing import List, Tuple, Dict
import json
import numpy as np


def get_input(filename) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    steps = lines.pop(0)
    lines.pop(0)
    nodes = {}
    for line in lines:
        node, connection_str = line.split(' = ')
        connections = connection_str[1:-1].split(', ')
        nodes[node] = connections
    return steps, nodes


def main():
    steps, nodes = get_input('input.txt')
    paths = {node: node for node in nodes if node[-1] == 'A'}   # Dict of path states (starting_node: current_node)
    path_lengths = {node: 0 for node in paths}
    while paths:
        for step in steps:
            complete_nodes = []
            for starting_node, current_node in paths.items():
                path_lengths[starting_node] += 1
                next_node = nodes[current_node][0 if step == 'L' else 1]
                paths[starting_node] = next_node
                if next_node[-1] == 'Z':
                    complete_nodes.append(starting_node)
            for node in complete_nodes:
                paths.pop(node)
    print(np.lcm.reduce(list(path_lengths.values())))


main()
