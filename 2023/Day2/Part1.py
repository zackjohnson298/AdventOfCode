from typing import List


class Roll:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __le__(self, other):
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue

    @staticmethod
    def from_line(line: str):
        counts_dict = {'red': 0, 'green': 0, 'blue': 0}
        for count_str in line.split(', '):
            count, color = count_str.split()
            counts_dict[color] += int(count)
        roll = Roll(**counts_dict)
        return roll


class Game:
    def __init__(self):
        self.id = -1
        self.rolls: List[Roll] = []

    def is_valid(self, max_roll: Roll) -> bool:
        for roll in self.rolls:
            if not roll <= max_roll:
                return False
        return True

    @staticmethod
    def from_line(line: str):
        game = Game()
        game_str, rolls_str = line.split(': ')
        game.id = int(game_str.split()[1])
        roll_strings = rolls_str.split('; ')
        game.rolls = [Roll.from_line(roll_line) for roll_line in roll_strings]
        return game


def get_input(filename) -> List[Game]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [Game.from_line(line) for line in lines]


def main():
    games = get_input('input.txt')
    max_roll = Roll(12, 13, 14)
    total = 0
    for game in games:
        if game.is_valid(max_roll):
            total += game.id
    print(total)


main()
