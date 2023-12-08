from typing import List, Tuple, Dict
import json


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
    current_node = 'AAA'
    destination = 'ZZZ'
    count = 0
    while current_node != destination:
        for step in steps:
            count += 1
            current_node = nodes[current_node][0 if step == 'L' else 1]
            if current_node == destination:
                break
    print(count)


main()
