from typing import *


def get_input(filename: str) -> str:
    with open(filename) as file:
        return file.readline()


def main():
    string = get_input('input.txt')
    # string = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    length = 14
    for ii in range(length, len(string)):
        if len(set([char for char in string[ii-length:ii]])) == length:
            print(ii, string[ii-length:ii])
            break


main()
