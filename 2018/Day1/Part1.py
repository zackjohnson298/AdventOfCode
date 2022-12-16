
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(line) for line in lines]


def main():
    values = get_input('input.txt')
    print(sum(values))


main()
