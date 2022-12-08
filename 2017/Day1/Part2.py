
def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [int(value) for value in line]


def main():
    line = get_input('input.txt')
    total = 0
    for ii in range(len(line)):
        a = line[ii]
        b = line[ii-int(len(line)/2)]
        if a == b:
            total += a
    print(total)


main()
