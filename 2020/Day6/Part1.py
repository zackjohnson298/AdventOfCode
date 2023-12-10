from typing import List, Optional, Tuple


def get_input(filename) -> List[List[str]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    current = []
    for line in lines:
        if line:
            current.extend([char for char in line])
        else:
            output.append(current)
            current = []
    if current:
        output.append(current)
    return output


def main():
    groups = get_input('input.txt')
    print(sum([len(set(group)) for group in groups]))


main()
