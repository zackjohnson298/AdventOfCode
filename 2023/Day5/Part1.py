from typing import List, Tuple, Dict


class Map:
    def __init__(self):
        self.ranges: List[Tuple[range, range]] = []

    def get_destination_value(self, source_value: int) -> int:
        for source_range, destination_range in self.ranges:
            if source_value in source_range:
                return destination_range[source_range.index(source_value)]
        return source_value

    def add_range_from_line(self, line: str):
        destination_start, source_start, count = [int(value) for value in line.split()]
        source_range = range(source_start, source_start + count)
        destination_range = range(destination_start, destination_start + count)
        self.ranges.append((source_range, destination_range))


def get_input(filename) -> Tuple[List[int], List[Map]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    seeds = [int(value) for value in lines.pop(0).strip('seeds:').split()]
    maps = []
    lines.pop(0)
    lines.pop(0)
    _map = Map()
    for ii, line in enumerate(lines):
        if not line:
            maps.append(_map)
            _map = Map()
        elif ':' in line:
            continue
        else:
            _map.add_range_from_line(line)
    maps.append(_map)
    return seeds, maps


def main():
    seeds, maps = get_input('input.txt')
    min_value = float('inf')
    for seed in seeds:
        value = seed
        for _map in maps:
            value = _map.get_destination_value(value)
        if value < min_value:
            min_value = value
    print(min_value)


main()
