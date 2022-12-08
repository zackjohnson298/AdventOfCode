import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[word for word in line.split()] for line in lines]


def are_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in set(word1):
        if word1.count(char) != word2.count(char):
            return False
    return True


def main():
    passphrases = get_input('input.txt')
    total = 0
    for passphrase in passphrases:
        valid = False
        if len(set(passphrase)) == len(passphrase):
            valid = True
            for ii, word1 in enumerate(passphrase[:-1]):
                for word2 in passphrase[ii+1:]:
                    if are_anagrams(word1, word2):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                total += 1
        print(passphrase, valid)
    print()
    print(total)


main()
