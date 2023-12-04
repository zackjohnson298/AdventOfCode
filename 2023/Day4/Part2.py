import json
from typing import List, Tuple


class Card:
    def __init__(self, number: int, winning_numbers: List[int], hand: List[int]):
        self.winning_numbers = winning_numbers
        self.hand = hand
        self.number = number
        count = 0
        for number in self.hand:
            if number in self.winning_numbers:
                count += 1
        self.won_card_numbers = list(range(self.number+1, self.number+count+1))

    @staticmethod
    def from_line(line: str):
        card_id, line = line.split(': ')
        card_number = int(card_id.split()[1])
        winning_str, hand_str = line.split(' | ')
        winning_numbers = [int(number) for number in winning_str.split()]
        hand = [int(number) for number in hand_str.split()]
        return Card(card_number, winning_numbers, hand)


def get_input(filename) -> List[Card]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [Card.from_line(line) for line in lines]


def main():
    cards = get_input('input.txt')
    card_counts = {card.number: 1 for card in cards}
    for card in cards:
        for number in card.won_card_numbers:
            card_counts[number] += card_counts[card.number]
    print(json.dumps(card_counts, indent=4))
    print(sum(card_counts.values()))




main()
