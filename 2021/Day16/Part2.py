import json


'''
UNFINISHED
'''
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    polymer = lines.pop(0)
    lines.pop(0)
    template = {}
    for line in lines:
        a, b = line.split(' -> ')
        template[a] = b
    return polymer, template


def main():
    polymer, template = get_input('input.txt')
    steps = 40
    counts = {}
    for ii in range(1, len(polymer)):
        pair = polymer[ii-1] + polymer[ii]
        counts[pair] = counts[pair] + 1 if pair in counts else 1
    for step in range(steps):
        new_pairs = {}
        for old_pair, old_value in counts.items():
            new_char = template[old_pair]
            new_pair_1 = old_pair[0] + new_char
            new_pair_2 = new_char + old_pair[1]
            new_pairs[new_pair_1] = new_pairs[new_pair_1] + old_value if new_pair_1 in new_pairs else old_value
            new_pairs[new_pair_2] = new_pairs[new_pair_2] + old_value if new_pair_2 in new_pairs else old_value
            counts[old_pair] -= old_value

        for new_pair, new_value in new_pairs.items():
            counts[new_pair] = counts[new_pair] + new_value if new_pair in counts else new_value
    #     print(step+1, ':', sum(counts.values()) + 1)
    # print()

    individual_counts = {}
    for pair, value in counts.items():
        for char in pair:
            individual_counts[char] = individual_counts[char] + value if char in individual_counts else value

    individual_counts[polymer[0]] += 1
    individual_counts[polymer[-1]] += 1

    for char in individual_counts:
        individual_counts[char] /= 2

    print(int(max(individual_counts.values()) - min(individual_counts.values())))

    # print(json.dumps(individual_counts, indent=4))




main()
