
def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [int(value) for value in line]


def main():
    line = get_input('input.txt')
    total = 0
    for ii in range(len(line)):
        if line[ii-1] == line[ii]:
            total += line[ii-1]
    print(total)


main()
