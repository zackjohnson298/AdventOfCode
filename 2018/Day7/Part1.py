import json
from typing import Dict, List, Tuple, Set


def get_input(filename) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    parent_rules = {}
    child_rules = {}
    for line in lines:
        parent_str, child_str = line.split(' must be finished before step ')
        parent = parent_str.replace('Step ', '')
        child = child_str.replace(' can begin.', '')
        existing_children = parent_rules.get(parent, set())
        existing_children.add(child)
        parent_rules[parent] = existing_children
        existing_parents = child_rules.get(child, set())
        existing_parents.add(parent)
        child_rules[child] = existing_parents
    parent_rules = {parent: list(children) for parent, children in parent_rules.items()}
    child_rules = {child: list(parents) for child, parents in child_rules.items()}
    return parent_rules, child_rules


def main():
    parent_rules, child_rules = get_input('input.txt')
    available = sorted(list(set(parent_rules).difference(child_rules)))
    end = sorted(list(set(child_rules).difference(parent_rules)))
    code = ''
    while available != end:
        next_letter = ''
        for candidate in available:
            if candidate in end:
                continue
            for required_parent in child_rules.get(candidate, []):
                if required_parent not in code:
                    break
            else:
                next_letter = candidate
                break
        if next_letter == '':
            break
        code = code + next_letter
        available.remove(next_letter)
        available = sorted(set(available + parent_rules[next_letter]))
    code = code + ''.join(letter for letter in sorted(end))
    print(code)


main()
