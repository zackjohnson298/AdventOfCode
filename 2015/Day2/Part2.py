
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    boxes = []
    for line in lines:
        dims = [int(value) for value in line.split('x')]
        boxes.append(tuple(dims))
    return boxes


def get_ribbon(dims: (int, int, int)):
    a, b, c = sorted(dims)
    ribbon = 2*a + 2*b + a*b*c
    return ribbon


def main():
    boxes = get_input('input.txt')
    print(sum([get_ribbon(box) for box in boxes]))


main()
