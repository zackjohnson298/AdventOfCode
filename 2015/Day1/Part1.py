
def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [char for char in line]


def main():
    steps = get_input('input.txt')
    floor = 0
    for step in steps:
        floor += 1 if step == '(' else -1
    print(floor)


main()
