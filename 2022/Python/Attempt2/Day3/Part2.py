from typing import *


def get_input(filename: str) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def get_priority(a: str, b: str, c: str) -> int:
    shared = set([char for char in a]).intersection(set([char for char in b])).intersection(set([char for char in c])).pop()
    return ord(shared) - (38 if shared.isupper() else 96)


def main():
    rucksacks = get_input('input.txt')
    print(sum([get_priority(*rucksacks[ii:ii+3]) for ii in range(0, len(rucksacks), 3)]))


main()
