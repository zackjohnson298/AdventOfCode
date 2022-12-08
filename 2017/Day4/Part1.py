import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[word for word in line.split()] for line in lines]


def main():
    passphrases = get_input('input.txt')
    total = 0
    for passphrase in passphrases:
        if len(set(passphrase)) == len(passphrase):
            total += 1
    print(total)


main()
