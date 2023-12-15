from typing import List, Tuple, Dict, Optional


def get_input(filename) -> List[str]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines[0].split(',')


def hash_str(value: str) -> int:
    current = 0
    for char in value:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def main():
    codes = get_input('input.txt')
    print(sum([hash_str(code) for code in codes]))


main()
