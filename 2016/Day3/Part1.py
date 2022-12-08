
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[int(value) for value in line.split()] for line in lines]


def main():
    triangles = get_input('input.txt')
    total = 0
    for a, b, c in triangles:
        if a < b + c and b < a + c and c < a + b:
            total += 1
    print(total)


main()
