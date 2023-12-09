from typing import List, Optional, Tuple


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(value) for value in lines]


def two_sum(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    differences = {}
    for number in numbers:
        difference = target - number
        reminder = differences.get(number)
        if reminder:
            return number, reminder
        differences[difference] = number
    return None


def main():
    values = get_input('input.txt')
    values = two_sum(values, 2020)
    if values:
        print(values, values[0]*values[1])
    else:
        print('None')

main()
