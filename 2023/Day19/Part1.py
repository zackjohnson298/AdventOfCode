from typing import List, Tuple, Dict, Optional, Set, Union


class Rule:
    def __init__(self, line: str):
        assert line[1] in ('>', '<')
        self.category = line[0]
        self.operation = line[1]
        value_str, self.destination = line[2:].split(':')
        self.threshold = int(value_str)

    def evaluate(self, part: Dict[str, int]) -> Tuple[Optional[str], Optional[bool]]:
        # Returns Destination, pass/fail
        value = part[self.category]
        if self.operation == '>':
            if value > self.threshold:
                return self.destination, True
            return None, False
        if value < self.threshold:
            return self.destination, True
        return None, False


def get_input(filename) -> Tuple[Dict[str, List[Union[Rule, str]]], List[Dict[str, int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    rules = {}
    while True:
        line = lines.pop(0)
        if line == '':
            break
        name, rules_str = line.split('{')
        rules_str = rules_str.replace('}', '')
        rule_strings = rules_str.split(',')
        rules[name] = [Rule(rule_str) for rule_str in rule_strings[:-1]] + [rule_strings[-1]]
    parts = []
    for line in lines:
        line = line[1:-1]
        sub_strings = line.split(',')
        part = {}
        for sub_string in sub_strings:
            name, value_str = sub_string.split('=')
            part[name] = int(value_str)
        parts.append(part)
    return rules, parts


def evaluate(workflows: Dict[str, List[Union[Rule, str]]], part: Dict[str, int]) -> bool:
    workflow_id = 'in'
    while True:
        workflow = workflows[workflow_id]
        for rule in workflow[:-1]:
            destination, passed = rule.evaluate(part)
            if passed:
                if destination in 'AR':
                    return destination == 'A'
                workflow_id = destination
                break
        else:
            destination = workflow[-1]
            if destination in 'AR':
                return destination == 'A'
            workflow_id = destination


def main():
    workflows, parts = get_input('input.txt')
    total = 0
    for part in parts:
        if evaluate(workflows, part):
            total += sum(part.values())
    print(total)


main()

