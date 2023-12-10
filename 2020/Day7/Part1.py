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


def find_valid_bags(target_bag: str, bags: Dict[str, Bag], valid_bags: Optional[Set[str]] = None) -> Set[str]:
    valid_bags = set(valid_bags) if valid_bags else set()
    new_bags = set([kind for kind, bag in bags.items() if target_bag in bag.contents and kind not in valid_bags])
    valid_bags.update(new_bags)
    new_valid_bags = valid_bags.union(new_bags)
    for new_kind in new_bags:
        new_valid_bags.update(find_valid_bags(new_kind, bags, valid_bags=new_valid_bags))
    return new_valid_bags


def main():
    bags = get_input('input.txt')
    target = 'shiny gold'
    valid_bags = find_valid_bags(target, bags)
    print(len(valid_bags))


main()
