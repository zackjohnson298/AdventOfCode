from typing import *


def get_input(filename: str) -> List[Tuple[str, str]]:
    with open(filename) as file:
        return [(line[:int(len(line)/2)], line[int(len(line)/2):]) for line in file.read().splitlines()]


def get_priority(a: str, b: str) -> int:
    shared = set([char for char in a]).intersection(set([char for char in b])).pop()
    return ord(shared) - (38 if shared.isupper() else 96)


def main():
    rucksacks = get_input('input.txt')
    print(sum([get_priority(*pair) for pair in rucksacks]))


main()
