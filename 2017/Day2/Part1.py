
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[int(value) for value in line.split()] for line in lines]


def main():
    lines = get_input('input.txt')
    total = 0
    for line in lines:
        total += max(line) - min(line)
    print(total)


main()
