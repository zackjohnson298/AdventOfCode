import json


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return json.loads(line)


def populate_values(dictionary, values, ignore_value=None):
    if type(dictionary) == list:
        for value in dictionary:
            populate_values(value, values, ignore_value=ignore_value)
    elif type(dictionary) == dict:
        new_values = []
        ignore = False
        for key, value in dictionary.items():
            if ignore_value in (key, value):
                ignore = True
                break
            populate_values(key, new_values, ignore_value=ignore_value)
            populate_values(value, new_values, ignore_value=ignore_value)
        if not ignore:
            values.extend(new_values)
    elif type(dictionary) == int:
        values.append(dictionary)


def main():
    dictionary = get_input('input.txt')
    # dictionary = [1,"red",5]
    values = []
    populate_values(dictionary, values, ignore_value='red')
    print(values)
    print(sum(values))


main()
