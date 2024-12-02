from typing import *


# class Rock:
#     def __init__(self, grid: List[str]):
#


def get_input(filename: str) -> str:
    with open(filename) as file:
        return file.readline()


def main():
    steps = get_input('test_input.txt')
    print(steps)


main()
