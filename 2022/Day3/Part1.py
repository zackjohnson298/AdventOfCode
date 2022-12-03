
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    compartment_1 = [set(line[:int(len(line) / 2)]) for line in lines]
    compartment_2 = [set(line[int(len(line) / 2):]) for line in lines]
    rucksacks = zip(compartment_1, compartment_2)
    return rucksacks


def get_score(letter: str):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


if __name__ == '__main__':
    rucksacks = get_input('input.txt')
    total = 0
    for compartment_1, compartment_2 in rucksacks:
        shared = list(compartment_1.intersection(compartment_2))[0]
        total += get_score(shared)
    print(total)
