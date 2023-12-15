from typing import List, Tuple, Dict
import functools


def get_input(filename) -> List[Tuple[str, Tuple[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        springs, rule = line.split()
        output.append((springs, tuple([int(char) for char in rule.split(',')])))
    return output


def unfold(springs: str, rules: Tuple[int], count=5) -> Tuple[str, Tuple[int]]:
    new_rules = rules*count
    new_springs = '?'.join(springs for _ in range(count))
    return new_springs, new_rules


@functools.cache
def find_arrangements(springs: str, rules: Tuple[int]) -> int:
    if len(springs) == 0 and len(rules) != 0:
        return 0
    elif len(rules) == 0:
        return 1 if '#' not in springs else 0
    char = springs[0]
    rule = rules[0]
    assert char in '.#?'
    if rule > len(springs) or len(rules) > 2*len(springs):
        return 0
    elif char == '#':
        current_group = springs[:rule]
        if not all([c in '#?' for c in current_group]):
            return 0
        if len(springs) == rule:
            return 1 if len(rules) == 1 else 0
        if springs[rule] in '.?':
            return find_arrangements(springs[rule+1:], rules[1:])
        return 0
    elif char == '.':
        return find_arrangements(springs[1:], rules)
    else:
        dot_spring = '.' + springs[1:]
        pound_spring = '#' + springs[1:]
        return find_arrangements(dot_spring, rules) + find_arrangements(pound_spring, rules)


def main():
    data = get_input('input.txt')
    total = 0
    for springs, rules in data:
        new = find_arrangements(*unfold(springs, rules))
        # print(springs, new)
        total += new
    print(total)


main()
