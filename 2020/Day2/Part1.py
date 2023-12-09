from typing import List, Optional, Tuple


class Password:
    def __init__(self, line: str):
        rule, word = line.split(': ')
        criteria, letter = rule.split()
        min_count, max_count = criteria.split('-')
        self.word = word
        self.letter = letter
        self.min_count = int(min_count)
        self.max_count = int(max_count)

    @property
    def is_valid(self) -> bool:
        return self.min_count <= self.word.count(self.letter) <= self.max_count


def get_input(filename) -> List[Password]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [Password(line) for line in lines]


def main():
    passwords = get_input('input.txt')
    print(sum([1 if password.is_valid else 0 for password in passwords]))


main()
