from typing import *


def get_input(filename: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    rules = []
    line = lines.pop(0)
    while line:
        a, b = line.split('|')
        rules.append((int(a), int(b)))
        line = lines.pop(0)
    updates = [[int(value) for value in line.split(',')] for line in lines]
    return rules, updates


def is_valid(update: List[int], rules: List[Tuple[int, int]]):
    for a, b in rules:
        if a not in update or b not in update:
            continue
        a_index = update.index(a)
        b_index = update.index(b)
        if a_index > b_index:
            return False
    return True


def main():
    rules, updates = get_input('input.txt')
    # for rule in rules:
    #     print(rule)
    # print()
    total = 0
    for update in updates:
        if is_valid(update, rules):
            total += update[int(len(update)/2)]
    print(total)


main()
