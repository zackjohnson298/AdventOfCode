import json
from typing import List, Optional, Tuple, Dict


def get_input(filename) -> List[int]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(value) for value in lines]


def arrangement_is_valid(adapters: List[int]) -> bool:
    if len(adapters) <= 2:
        return False
    differences = [adapters[ii] - adapters[ii - 1] for ii in range(1, len(adapters))]
    min_value = min(differences)
    max_value = max(differences)
    print(differences)
    if 1 <= min_value <= max_value <= 3:
        # print(adapters)
        return True
    return False


def find_valid_arrangements(adapters: List[int]) -> int:
    path_counts: Dict[int, int] = {adapter: 0 for adapter in adapters}
    path_counts[adapters[-1]] = 1
    pairs = []
    for ii in reversed(range(len(adapters)-1)):
        for jj in range(ii+1, ii+4):
            if jj >= len(adapters):
                break
            a = adapters[ii]
            b = adapters[jj]
            if b - a <= 3:
                path_counts[a] += path_counts[b]
                pairs.append((a, b))
    return path_counts[adapters[0]]


def main():
    adapters = sorted(get_input('input.txt'))
    adapters = [0] + adapters + [max(adapters) + 3]
    print(find_valid_arrangements(adapters))

main()
