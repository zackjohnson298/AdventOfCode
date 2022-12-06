
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def main():
    lines = get_input('input.txt')
    length = 4
    for line in lines:
        for ii in range(length, len(line)):
            if len(set(line[ii-length:ii])) == length:
                print(ii)
                break


main()
