from typing import List, Tuple, Dict


CARDS = 'AKQJT98765432'


class Hand:
    def __init__(self, line: str):
        cards, bid = line.split()
        self.cards = [card for card in cards]
        self.bid = int(bid)
        self.strength = -1
        self.calculate_strength()

    def calculate_strength(self):
        card_set = set(self.cards)
        if len(card_set) == 1:
            self.strength = 7
        elif len(card_set) == 2:
            if self.cards.count(self.cards[0]) in (4, 1):
                self.strength = 6
            elif self.cards.count(self.cards[0]) in (3, 2):
                self.strength = 5
            else:
                raise Exception(f'Unhandled state len 2: {self.cards}')
        elif len(card_set) == 3:
            a, b, c = [card for card in sorted(card_set, key=lambda card: self.cards.count(card))]
            if self.cards.count(a) == 1 and self.cards.count(b) == 1 and self.cards.count(c) == 3:
                self.strength = 4
            elif self.cards.count(a) == 1 and self.cards.count(b) == 2 and self.cards.count(c) == 2:
                self.strength = 3
            else:
                raise Exception(f'Unhandled state len 3: {self.cards}')
        elif len(card_set) == 4:
            self.strength = 2
        else:
            self.strength = 1

    def __lt__(self, other):
        if self.strength != other.strength:
            return self.strength < other.strength
        for a, b in zip(self.cards, other.cards):
            index_a = CARDS.index(a)
            index_b = CARDS.index(b)
            if index_a != index_b:
                return index_a > index_b
        raise Exception(f'Count not compare cards: {self.cards}, {other.cards}')


def get_input(filename) -> List[Hand]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [Hand(line) for line in lines]


def main():
    hands = get_input('input.txt')
    print(sum([ii*hand.bid for ii, hand in enumerate(sorted(hands), start=1)]))


main()