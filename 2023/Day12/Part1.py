from typing import List, Tuple, Dict
import numpy as np


def get_input(filename) -> List[Tuple[str, List[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        springs, rule = line.split()
        output.append((springs, [int(char) for char in rule.split(',')]))
    return output


def validate_springs(springs: str, rules: List[int]):
    current = ''
    groups = []
    for char in springs:
        if char == '#':
            current = current + char
        elif current:
            groups.append(current)
            current = ''
    if current:
        groups.append(current)
    if len(groups) == len(rules):
        return all([len(group) == rule for group, rule in zip(groups, rules)])
    return False


def find_arrangements(springs: str, rules: List[int]):
    total = 0
    max_count = 2**springs.count('?')
    total_binary_len = len(bin(max_count-1)[2:])
    # print(springs)
    for ii in range(max_count):
        qm_count = 0
        bin_str = bin(ii)[2:]
        bin_str = '0'*(total_binary_len - len(bin_str)) + bin_str
        new_str = ''
        for char in springs:
            if char == '?':
                new_str = new_str + ('#' if int(bin_str[qm_count]) else '.')
                qm_count += 1
            else:
                new_str = new_str + char
        if validate_springs(new_str, rules):
            total += 1
    return total


def main():
    springs = get_input('input.txt')
    total = 0
    for spring, rules in springs:
        new = find_arrangements(spring, rules)
        print(spring, new)
        total += new
    print(total)


main()
