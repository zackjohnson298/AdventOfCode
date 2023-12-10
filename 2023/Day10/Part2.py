from typing import List, Tuple, Dict


def get_input(filename) -> List[List[int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[int(char) for char in line.split()] for line in lines]


def get_next_value(sequence: List[int]) -> int:
    new_sequence = []
    for ii in range(1, len(sequence)):
        new_sequence.append(sequence[ii] - sequence[ii-1])
    if all([val == 0 for val in new_sequence]):
        return sequence[0]
    return sequence[0] - get_next_value(new_sequence)


def main():
    histories = get_input('input.txt')
    print(sum([get_next_value(hist) for hist in histories]))


main()
