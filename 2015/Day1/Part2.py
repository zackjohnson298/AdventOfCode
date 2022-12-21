
def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [char for char in line]


def main():
    steps = get_input('input.txt')
    floor = 0
    for position, step in enumerate(steps, start=1):
        floor += 1 if step == '(' else -1
        if floor < 0:
            print(position)
            break


main()
