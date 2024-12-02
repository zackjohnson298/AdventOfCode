from typing import *


def get_input(filename: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        pa, pb = line.split(',')
        a1, a2 = [int(value) for value in pa.split('-')]
        b1, b2 = [int(value) for value in pb.split('-')]
        output.append(((a1, a2), (b1, b2)))
    return output


def main():
    pairs = get_input('input.txt')
    total = 0
    for (a1, a2), (b1, b2) in pairs:
        a_set = set(list(range(a1, a2 + 1)))
        b_set = set(list(range(b1, b2 + 1)))
        shared = a_set.intersection(b_set)
        if shared:
            total += 1
    print(total)


main()
