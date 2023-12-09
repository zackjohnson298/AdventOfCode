from typing import List, Optional, Tuple


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return sorted([int(value) for value in lines])


def two_sum(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    differences = {}
    for number in numbers:
        difference = target - number
        reminder = differences.get(number)
        if reminder:
            return number, reminder
        differences[difference] = number
    return None


def three_sum(numbers: List[int], target: int) -> Optional[Tuple[int, int, int]]:
    for number in numbers:
        new_target = target - number
        new_numbers = [num for num in numbers if num != number]
        result = two_sum(new_numbers, new_target)
        if result:
            return number, result[0], result[1]
    return None


def main():
    values = get_input('input.txt')
    values = three_sum(values, 2020)
    if values:
        print(values, values[0]*values[1]*values[2])
    else:
        print('None')

main()
