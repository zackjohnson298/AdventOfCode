import json
from itertools import permutations


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    people = {}
    for line in lines:
        line = line.split()
        name = line[0]
        neighbor = line[-1][:-1]
        value = int(line[3]) * (-1 if line[2] == 'lose' else 1)
        if name in people:
            people[name]['neighbors'][neighbor] = value
        else:
            people[name] = {
                'name': name,
                'neighbors': {
                    neighbor: value
                }
            }
    return people


def find_happiness(people, arrangement):
    total = 0
    for ii in range(len(arrangement)):
        person_a = arrangement[ii]
        person_b = arrangement[ii - 1]
        total += people[person_a]['neighbors'][person_b]
        total += people[person_b]['neighbors'][person_a]
    return total


def main():
    people = get_input('input.txt')
    max_value = 0
    for arrangement in permutations(people.keys()):
        value = find_happiness(people, arrangement)
        if value > max_value:
            max_value = value
    print(max_value)

main()
