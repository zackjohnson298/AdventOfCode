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


def get_total_score(ingredients, counts):
    totals = {}
    for ii, (name, ingredient) in enumerate(sorted(ingredients.items())):
        count = counts[ii]
        for prop_name, value in ingredient['properties'].items():
            if prop_name in totals:
                totals[prop_name] += count*value
            else:
                totals[prop_name] = count*value

    return prod([value for key, value in totals.items() if key != 'calories']), totals['calories']


def main():
    ingredients = get_input('input.txt')
    desired_calories = 500
    max_score = 0
    for counts in sums(len(ingredients), 100):
        score, calories = get_total_score(ingredients, counts)
        print(counts, score, calories)
        if score > max_score and calories == desired_calories:
            max_score = score
    print()
    print(max_score)


main()
