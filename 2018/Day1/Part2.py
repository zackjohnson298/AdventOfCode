
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(line) for line in lines]


def main():
    values = get_input('input.txt')
    # values = [+1, -1]
    frequency = 0
    frequencies = []
    for value in values:
        frequency += value
        frequencies.append(frequency)
    print(frequencies)
    delta = frequencies[-1]
    for n in range(1, 1000000):
        for frequency in frequencies:
            if frequency + n*delta in frequencies:
                print(frequency + n*delta)
                return


main()
