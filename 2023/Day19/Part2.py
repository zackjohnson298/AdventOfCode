from typing import List, Tuple, Dict, Optional, Set, Union

XMASRange = Dict[str, Tuple[int, int]]


class Workflow:
    def __init__(self, name: str, rules_str: str):
        self.name = name
        self.rules = rules_str.replace('{', '').replace('}', '').split(',')

    def apply_range(self, input_range: XMASRange) -> Dict[str, List[XMASRange]]:
        current_range = {letter: (start, stop) for letter, (start, stop) in input_range.items()}
        output = {}
        for rule in self.rules[:-1]:
            criteria, destination = rule.split(':')
            letter = criteria[0]
            op = criteria[1]
            value = int(criteria[2:])
            a, b = current_range[letter]
            if not a <= value <= b:
                raise Exception(f'ERROR: {rule} {current_range[letter]}')
            new_range = {letter: (start, stop) for letter, (start, stop) in current_range.items()}
            if op == '>':
                new_range[letter] = (value+1, b)
                current_range[letter] = (a, value)
            else:
                new_range[letter] = (a, value-1)
                current_range[letter] = (value, b)
            if destination not in output:
                output[destination] = [new_range]
            else:
                output[destination].append(new_range)
        if self.rules[-1] not in output:
            output[self.rules[-1]] = [current_range]
        else:
            output[self.rules[-1]].append(current_range)
        return output


def get_input(filename) -> Dict[str, Workflow]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = {}
    while True:
        line = lines.pop(0)
        if line == '':
            break
        name, rules_str = line.split('{')
        workflow = Workflow(name, rules_str)
        output[name] = workflow
    return output


def evaluate(name: str, workflows: Dict[str, Workflow], input_range: XMASRange, a_ranges: List[XMASRange], r_ranges: List[XMASRange]):
    workflow = workflows[name]
    new_ranges = workflow.apply_range(input_range)
    new_accepted = new_ranges.get('A')
    if new_accepted:
        a_ranges.extend(new_accepted)
        new_ranges.pop('A')
    new_rejected = new_ranges.get('R')
    if new_rejected:
        r_ranges.extend(new_rejected)
        new_ranges.pop('R')
    for destination, next_range_list in new_ranges.items():
        for next_range in next_range_list:
            evaluate(destination, workflows, next_range, a_ranges, r_ranges)


def main():
    workflows = get_input('input.txt')
    start = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    accepted = []
    rejected = []
    evaluate('in', workflows, start, accepted, rejected)
    total = 0
    for a_range in accepted:
        current = 1
        for letter, (a, b) in a_range.items():
            current *= (b+1-a)
        total += current
    print(total)


main()

