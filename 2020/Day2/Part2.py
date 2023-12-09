from typing import List, Optional, Tuple


class Password:
    def __init__(self, line: str):
        rule, word = line.split(': ')
        criteria, letter = rule.split()
        a, b = criteria.split('-')
        self.word = word
        self.letter = letter
        self.position_a = int(a) - 1
        self.position_b = int(b) - 1
        assert 0 <= self.position_a < len(self.word)
        assert 0 <= self.position_b < len(self.word)

    @property
    def is_valid(self) -> bool:
        letters = (self.word[self.position_a], self.word[self.position_b])
        return letters.count(self.letter) == 1


def get_input(filename) -> List[Password]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [Password(line) for line in lines]


def main():
    passwords = get_input('input.txt')
    print(sum([1 if password.is_valid else 0 for password in passwords]))


main()
