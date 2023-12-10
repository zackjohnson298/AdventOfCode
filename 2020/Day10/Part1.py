from typing import List, Optional, Tuple


def get_input(filename) -> List[int]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(value) for value in lines]


def main():
    adapters = sorted(get_input('input.txt'))
    adapters = [0] + adapters + [max(adapters) + 3]
    differences = [adapters[ii]-adapters[ii-1] for ii in range(1, len(adapters))]
    one_count = differences.count(1)
    three_count = differences.count(3)
    print(one_count, three_count, one_count * three_count)


main()
