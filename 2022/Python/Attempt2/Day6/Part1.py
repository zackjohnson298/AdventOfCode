from typing import *


def get_input(filename: str) -> str:
    with open(filename) as file:
        return file.readline()


def main():
    string = get_input('input.txt')
    # string = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    for ii in range(4, len(string)):
        if len(set([char for char in string[ii-4:ii]])) == 4:
            print(ii, string[ii-4:ii])
            break


main()
