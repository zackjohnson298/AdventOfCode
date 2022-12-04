

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    groups = []
    for ii in range(0, len(lines), 3):
        group = [set(line) for line in lines[ii:ii + 3]]
        groups.append(group)
    return groups


def get_score(letter: str):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


def main():
    groups = get_input('input.txt')
    total = 0
    for a, b, c in groups:
        shared = list(a.intersection(b).intersection(c))[0]
        total += get_score(shared)
    print(total)

main()
