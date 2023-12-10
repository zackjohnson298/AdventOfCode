from typing import List, Optional, Tuple, Set


def get_input(filename) -> List[List[Set[str]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    current_group = []
    for line in lines:
        if line:
            current_group.append(set([char for char in line]))
        else:
            output.append(current_group)
            current_group = []
    if current_group:
        output.append(current_group)
    return output


def main():
    groups = get_input('input.txt')
    total = 0
    for group in groups:
        current_set = group[0]
        for new_set in group:
            current_set = current_set.intersection(new_set)
        total += len(current_set)
    print(total)


main()
