
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    boxes = []
    for line in lines:
        dims = [int(value) for value in line.split('x')]
        boxes.append(tuple(dims))
    return boxes


def get_area(dims: (int, int, int)):
    a, b, c = sorted(dims)
    area = 2*a*b + 2*b*c + 2*a*c + a*b
    return area


def main():
    boxes = get_input('input.txt')
    print(sum([get_area(box) for box in boxes]))


main()
