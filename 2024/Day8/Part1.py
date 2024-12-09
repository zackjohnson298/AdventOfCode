from typing import *


def get_input(filename: str) -> Tuple[Dict[str, List[Tuple[int, int]]], Tuple[int, int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = {}
    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char == '.':
                continue
            if char in output:
                output[char].append((r, c))
            else:
                output[char] = [(r, c)]
    return output, (len(lines), len(lines[0]))


def get_pair_antinodes(a: Tuple[int, int], b: Tuple[int, int]) -> List[Tuple[int, int]]:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return [(a[0] + dx, a[1] + dy), (b[0] - dx, b[1] - dy)]


def get_all_antinodes(nodes: List[Tuple[int, int]], size: Tuple[int, int]) -> Set[Tuple[int, int]]:
    points = set()
    pairs = [(a, b) for idx, a in enumerate(nodes) for b in nodes[idx + 1:]]
    for a, b in pairs:
        antinodes = get_pair_antinodes(a, b)
        for antinode in antinodes:
            if 0 <= antinode[0] < size[0] and 0 <= antinode[1] < size[1]:
                points.add(antinode)
    return points


def main():
    nodes, size = get_input('input.txt')
    points = set()
    for frequency, node_list in nodes.items():
        points.update(get_all_antinodes(node_list, size))
    print(len(points))

main()
