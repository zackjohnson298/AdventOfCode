from typing import *
from random import randint


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


def find_next(rules: List[Tuple[int, int]]) -> Optional[int]:
    b_list = [rule[1] for rule in rules]
    for a, b in rules:
        if a not in b_list:
            return a
    return None


def fix(update: List[int], rules: List[Tuple[int, int]]) -> Optional[List[int]]:
    relevant_rules = [(a, b) for a, b in rules if a in update and b in update]
    new_update = []
    remaining = []
    while relevant_rules:
        next_number = find_next(relevant_rules)
        new_update.append(next_number)
        remaining = [value for value in update if value not in new_update]
        relevant_rules = [(a, b) for a, b in rules if a in remaining and b in remaining]
    new_update.append(remaining[0])
    return new_update


def main():
    rules, updates = get_input('input.txt')
    total = 0
    for update in updates:
        if not is_valid(update, rules):
            new_update = fix(update, rules)
            total += new_update[int(len(update)/2)]
        # if new_update is not None:
        # print(fix(update, rules))
        # if is_valid(update, rules):
        #     total += update[int(len(update)/2)]
    print(total)


main()
