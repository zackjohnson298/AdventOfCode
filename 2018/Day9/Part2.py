import json


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [int(value) for value in line.split()]


def construct_tree(numbers: [int]):
    child_node_count = numbers.pop(0)
    metadata_count = numbers.pop(0)
    tree = {
        'children': {},
        'Metadata': None
    }
    for ii in range(child_node_count):
        tree['children'][ii + 1] = construct_tree(numbers)
    tree['Metadata'] = [numbers.pop(0) for _ in range(metadata_count)]
    return tree


def calculate_node_value(node):
    if len(node['children']) == 0:
        return sum(node['Metadata'])
    total = 0
    for node_index in node['Metadata']:
        child_node = node['children'].get(node_index)
        if child_node is not None:
            total += calculate_node_value(child_node)
    return total


def main():
    numbers = get_input('input.txt')
    tree = construct_tree(numbers)
    node_value = calculate_node_value(tree)
    print(node_value)


main()
