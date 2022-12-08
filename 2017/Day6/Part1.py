
def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [int(value) for value in line.split()]


def main():
    banks = get_input('input.txt')
    memory = []
    while banks not in memory:
        print(banks)
        memory.append(banks.copy())
        max_value = max(banks)
        index = banks.index(max_value)
        banks[index] = 0
        for ii in range(max_value):
            new_index = (ii + index + 1) % len(banks)
            banks[new_index] += 1
    print()
    print(len(memory) - memory.index(banks))


main()
