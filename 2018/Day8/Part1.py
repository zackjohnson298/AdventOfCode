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


def calculate_metadata_sum(tree):
    total = sum(tree['Metadata'])
    for child in tree['children']:
        total += calculate_metadata_sum(tree['children'][child])
    return total


def main():
    numbers = get_input('test_input.txt')
    tree = construct_tree(numbers)
    print(json.dumps(tree, indent=4))
    metadata_sum = calculate_metadata_sum(tree)
    print(metadata_sum)


main()
