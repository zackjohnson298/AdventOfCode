from typing import List


class Roll:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __le__(self, other):
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue

    def __getitem__(self, key):
        return self.__dict__[key]

    @property
    def power(self) -> int:
        return self.red * self.blue * self.green

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


def find_min_roll(game: Game) -> Roll:
    min_roll = {'red': 0, 'green': 0, 'blue': 0}
    for color in min_roll:
        for roll in game.rolls:
            if roll[color] > min_roll[color]:
                min_roll[color] = roll[color]
    return Roll(**min_roll)


def main():
    games = get_input('input.txt')
    total = 0
    for game in games:
        min_roll = find_min_roll(game)
        total += min_roll.power
    print(total)


main()
