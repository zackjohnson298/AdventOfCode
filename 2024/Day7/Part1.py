from typing import *


def get_input(filename: str) -> List[Tuple[int, List[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        a, b = line.split(': ')
        numbers = b.split()
        output.append((int(a), [int(value) for value in numbers]))
    return output


def execute(numbers: List[int], operators: int) -> int:
    output = numbers[0]
    for power in range(len(numbers)-1):
        if operators & (2**power):
            output *= numbers[power+1]
        else:
            output += numbers[power+1]
    return output


def validate(line: Tuple[int, List[int]]) -> int:
    answer, numbers = line
    options = 2**(len(numbers)-1)
    count = 0
    for operators in range(options):
        if execute(numbers, operators) == answer:
            count += 1
    return count


def main():
    lines = get_input('input.txt')
    total = 0
    for line in lines:
        if validate(line):
            total += line[0]
    print(total)


main()
