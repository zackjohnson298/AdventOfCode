
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    pairs = []
    for line in lines:
        pair_1, pair_2 = line.split(',')
        pair_1 = [int(value) for value in pair_1.split('-')]
        pair_2 = [int(value) for value in pair_2.split('-')]
        pairs.append([pair_1, pair_2])
    return pairs


def is_valid(set_1, set_2):
    return (set_1[0] <= set_2[0] and set_1[1] >= set_2[1]) or (set_2[0] <= set_1[0] and set_2[1] >= set_1[1])


def main():
    pairs = get_input('input.txt')
    count = 0
    for set_1, set_2 in pairs:
        if is_valid(set_1, set_2):
            count += 1
    print(count)


main()
