import numpy as np
from statistics import mode


def get_input():
    with open('input.txt') as file:
        lines = file.read().splitlines()
#     lines = '''00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010'''.splitlines()
    return np.array([[int(value) for value in line] for line in lines])


def main():
    data = get_input()
    gamma = 0
    eps = 0
    rows, cols = data.shape
    for col in range(cols):
        value = mode(data[:, col])
        gamma += value * 2 ** (cols - col - 1)
        eps += (1 - value) * 2 ** (cols - col - 1)
    print(gamma, eps, gamma*eps)

main()
