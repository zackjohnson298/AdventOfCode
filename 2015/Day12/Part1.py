import json


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return json.loads(line)


def populate_values(dictionary, values):
    if type(dictionary) == list:
        for value in dictionary:
            populate_values(value, values)
    elif type(dictionary) == dict:
        for key, value in dictionary.items():
            populate_values(key, values)
            populate_values(value, values)
    elif type(dictionary) == int:
        values.append(dictionary)


def main():
    dictionary = get_input('input.txt')
    # dictionary = {}
    values = []
    populate_values(dictionary, values)
    print(values)
    print(sum(values))


main()
