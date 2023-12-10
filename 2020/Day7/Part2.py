from typing import List, Optional, Tuple, Dict, Set


class Bag:
    def __init__(self, line: str):
        self.contents: Dict[str, int] = {}
        self.kind: str = ''
        self.raw_line_string = line
        self._parse_input_line()

    @property
    def is_empty(self):
        return len(self.contents) == 0

    def _parse_input_line(self):
        line = self.raw_line_string
        self.kind, line = line.split(' bags contain ')
        if 'no other bags' in line:
            return
        line = line.replace('.', '')
        line = line.replace(' bags', '')
        line = line.replace(' bag', '')
        contents = line.split(', ')
        for child in contents:
            self.contents[child[child.index(' ')+1:]] = int(child[:child.index(' ')])


def get_input(filename) -> Dict[str, Bag]:
    with open(filename) as file:
        lines = file.read().splitlines()
    bags = [Bag(line) for line in lines]
    return {bag.kind: bag for bag in bags}


def count_children(bag_kind: str, bags: Dict[str, Bag]) -> int:
    bag = bags[bag_kind]
    total = 0
    for child_kind, child_count in bag.contents.items():
        new_count = 1 + count_children(child_kind, bags)
        total += child_count * new_count
    return total


def main():
    bags = get_input('input.txt')
    bag = 'shiny gold'
    print(count_children(bag, bags))


main()
