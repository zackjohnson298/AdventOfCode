import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    triangles = []
    numbers = np.array([[int(value) for value in line.split()] for line in lines])
    rows, cols = numbers.shape
    for row in range(0, rows, 3):
        for col in range(cols):
            triangle = numbers[row:row+3, col]
            triangles.append(triangle.tolist())
    return triangles


def main():
    triangles = get_input('input.txt')
    total = 0
    for a, b, c in triangles:
        if a < b + c and b < a + c and c < a + b:
            total += 1
    print(total)


main()
