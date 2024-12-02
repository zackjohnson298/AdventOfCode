from typing import *


def get_input(filename: str) -> Tuple[Dict[int, List[str]], List[Tuple[int, int, int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    line = lines.pop(0)
    crates = {}
    while line:
        line = line[1:]
        crates_this_row = [line[ii] for ii in range(0, len(line), 4)]
        for ii, crate in enumerate(crates_this_row, start=1):
            if crate == ' ':
                continue
            if ii not in crates:
                crates[ii] = []
            crates[ii].insert(0, crate)
        line = lines.pop(0)
        if line[1].isdigit():
            line = lines.pop(0)
    steps = []
    for line in lines:
        line = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',')
        a, b, c = [int(value) for value in line.split(',')]
        steps.append((a, b, c))
    return crates, steps


def main():
    crates, steps = get_input('input.txt')
    for num, s, d in steps:
        source = crates[s]
        dest = crates[d]
        stack = [source.pop() for _ in range(num)]
        dest.extend(list(reversed(stack)))
    print(''.join([stack[-1] for _, stack in sorted(crates.items())]))


main()
