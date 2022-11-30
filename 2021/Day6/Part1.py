import numpy as np


def get_input():
    with open('input.txt') as file:
        line = file.readline()
    return [int(value) for value in line.split(',')]


def main():
    fish = get_input()
    timers = [fish.count(ii) for ii in range(9)]
    days = 80
    for day in range(days):
        new_fish = timers.pop(0)
        timers.append(new_fish)
        timers[6] += new_fish
    print(sum(timers))


main()
