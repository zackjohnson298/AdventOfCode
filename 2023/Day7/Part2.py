from typing import List, Tuple, Dict


CARDS = 'AKQT98765432J'


def calculate_5card_strength(cards: List[str]) -> int:
    assert len(cards) == 5
    card_set = set(cards)
    if len(card_set) == 1:
        strength = 7
    elif len(card_set) == 2:
        if cards.count(cards[0]) in (4, 1):
            strength = 6
        elif cards.count(cards[0]) in (3, 2):
            strength = 5
        else:
            raise Exception(f'Unhandled state len 2: {cards}')
    elif len(card_set) == 3:
        a, b, c = [card for card in sorted(card_set, key=lambda card: cards.count(card))]
        if cards.count(a) == 1 and cards.count(b) == 1 and cards.count(c) == 3:
            strength = 4
        elif cards.count(a) == 1 and cards.count(b) == 2 and cards.count(c) == 2:
            strength = 3
        else:
            raise Exception(f'Unhandled state len 3: {cards}')
    elif len(card_set) == 4:
        strength = 2
    else:
        strength = 1
    return strength


def calculate_4card_strength(cards: List[str]) -> int:
    assert len(cards) == 4
    card_set = set(cards)
    if len(card_set) == 1:
        strength = 7
    elif len(card_set) == 2:
        if cards.count(cards[0]) in (3, 1):
            strength = 6
        elif cards.count(cards[0]) == 2:
            strength = 5
        else:
            raise Exception(f'Unhandled state 1J len 2: {cards}')
    elif len(card_set) == 3:
        a, b, c = [card for card in sorted(card_set, key=lambda card: cards.count(card))]
        if cards.count(a) == 1 and cards.count(b) == 1 and cards.count(c) == 2:
            strength = 4
        else:
            raise Exception(f'Unhandled state 1J len 3: {cards}')
    elif len(card_set) == 4:
        strength = 2
    else:
        raise Exception(f'Unhandled final state 1J: {cards}')
    return strength


def calculate_3card_strength(cards: List[str]) -> int:
    assert len(cards) == 3
    card_set = set(cards)
    if len(card_set) == 1:
        strength = 7
    elif len(card_set) == 2:
        strength = 6
    elif len(card_set) == 3:
        strength = 4
    else:
        raise Exception(f'Unhandled final state 2J: {cards}')
    return strength


def calculate_2card_strength(cards: List[str]) -> int:
    assert len(cards) == 2
    card_set = set(cards)
    if len(card_set) == 1:
        strength = 7
    elif len(card_set) == 2:
        strength = 6
    else:
        raise Exception(f'Unhandled final state 3J: {cards}')
    return strength


class Hand:
    def __init__(self, line: str):
        cards, bid = line.split()
        self.cards = [card for card in cards]
        self.bid = int(bid)
        self.strength = -1
        self.calculate_strength()

    def calculate_strength(self):
        j_count = self.cards.count('J')
        cards = [card for card in self.cards if card != 'J']
        if j_count == 0:
            self.strength = calculate_5card_strength(cards)
        elif j_count == 1:
            self.strength = calculate_4card_strength(cards)
        elif j_count == 2:
            self.strength = calculate_3card_strength(cards)
        elif j_count == 3:
            self.strength = calculate_2card_strength(cards)
        else:
            self.strength = 7

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
