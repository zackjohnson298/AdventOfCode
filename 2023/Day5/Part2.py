from typing import List, Tuple, Dict
import matplotlib.pyplot as plt


class Map:
    def __init__(self):
        # List of all ranges within the mapping: ((start, end), delta), where delta is the actual mapping itself
        self.ranges: List[Tuple[Tuple[int, int], int]] = []

    def add_range_from_line(self, line: str):
        destination_start, source_start, count = [int(value) for value in line.split()]
        source_range = (source_start, source_start + count-1)
        change = destination_start - source_start
        self.ranges.append((source_range, change))
        self.ranges = sorted(self.ranges, key=lambda item: item[0])

    def get_value_and_spacing(self, input_value: int) -> Tuple[int, float]:
        # for a given range, the output values will increase linearly up to the upper range bound, so there is
        #   no need to check them
        for ii, ((source_a, source_b), change) in enumerate(self.ranges):
            if source_a <= input_value <= source_b:
                # input is within the range, so spacing is the distance between input_value and upper bound
                return input_value + change, source_b - input_value
            elif source_a > input_value and ii < len(self.ranges):
                # input is outside of range but less than lower bound of next range, spacing is the distance between
                #   input_value and lower bound of next range (output value will also increase linearly here
                return input_value, self.ranges[ii + 1][0][0] - input_value
        # input value is outside all ranges and greater than all values. The spacing of this map should not be
        #   used to shrink the input space
        return input_value, float('inf')


def get_input(filename) -> Tuple[List[Tuple[int, int]], List[Map]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    seeds = [int(value) for value in lines.pop(0).strip('seeds:').split()]
    seed_output = []
    for ii in range(0, len(seeds), 2):
        start = seeds[ii]
        count = seeds[ii+1]
        seed_output.append((start, start+count))
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
    return seed_output, maps


def main():
    seed_ranges, maps = get_input('input.txt')
    min_location = float('inf')
    for seed_start, seed_end in seed_ranges:
        seed = seed_start
        while seed_start <= seed < seed_end:
            spacings = []
            current_value = seed
            for mapping in maps:
                current_value, spacing = mapping.get_value_and_spacing(current_value)
                spacings.append(spacing)
            min_spacing = min(spacings)
            seed += min_spacing + 1
            if current_value < min_location:
                min_location = current_value
    print(min_location)


main()
