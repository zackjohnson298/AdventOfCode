import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    ingredients = {}
    for line in lines:
        line = line.split()
        name = line[0][:-1]
        capacity = int(line[2][:-1])
        durability = int(line[4][:-1])
        flavor = int(line[6][:-1])
        texture = int(line[8][:-1])
        calories = int(line[-1])
        ingredients[name] = {
            'name': name,
            'count': 0,
            'properties': {
                'capacity': capacity,
                'durability': durability,
                'flavor': flavor,
                'texture': texture,
                'calories': calories
            }
        }
    return ingredients


def sums(length, total_sum):
    if length == 1:
        yield total_sum,
    else:
        for value in range(total_sum + 1):
            if value != 0:
                for permutation in sums(length - 1, total_sum - value):
                    if 0 not in permutation:
                        yield (value,) + permutation


def prod(array):
    output = 1
    for value in array:
        output *= value
    return output


def get_total_score(ingredients, counts, ignore=None):
    totals = {}
    for ii, (name, ingredient) in enumerate(sorted(ingredients.items())):
        count = counts[ii]
        for prop_name, value in ingredient['properties'].items():
            if prop_name == ignore:
                continue
            if prop_name in totals:
                totals[prop_name] += count*value
            else:
                totals[prop_name] = count*value
    for value in totals.values():
        if value <= 0:
            return 0
    return prod(totals.values())


def main():
    ingredients = get_input('input.txt')
    max_value = 0
    for counts in sums(len(ingredients), 100):
        value = get_total_score(ingredients, counts, ignore='calories')
        print(counts, value)
        if value > max_value:
            max_value = value
    print()
    print(max_value)

main()
