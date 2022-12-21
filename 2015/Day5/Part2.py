import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def is_nice(word):
    for pair in ['ab', 'cd', 'pq', 'xy']:
        if pair in word:
            return False
    if sum([word.count(vowel) for vowel in 'aeiou']) < 3:
        return False
    for ii in range(1, len(word)):
        if word[ii] == word[ii-1]:
            return True
    return False


def main():
    words = get_input('input.txt')
    print(sum([is_nice(word) for word in words]))


main()
