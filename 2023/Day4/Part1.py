from typing import List, Tuple


def get_input(filename) -> List[Tuple[List[int], List[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        line = line.split(': ')[1]
        winning_str, hand_str = line.split(' | ')
        winning = [int(number) for number in winning_str.split()]
        hand = [int(number) for number in hand_str.split()]
        output.append((winning, hand))
    return output


def main():
    cards = get_input('input.txt')
    total = 0
    for winning, hand in cards:
        score = 0
        for number in hand:
            if number in winning:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        print(score, winning, hand)
        total += score
    print(total)


main()
