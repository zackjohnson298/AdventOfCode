import json
import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return None


def main():
    _ = get_input('input.txt')


main()
