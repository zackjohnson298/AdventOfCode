import numpy as np


def get_power(x, y, serial_number):
    rack_id = x + 10
    power = rack_id * y
    power += serial_number
    power *= rack_id
    power = int((power % 1000 - power % 100) / 100)
    return power - 5


def main():
    serial_number = 8772
    max_x = 300 + 1
    max_y = 300 + 1
    grid = np.zeros((max_x, max_y))
    for x in range(1, max_x):
        for y in range(1, max_y):
            grid[x, y] = get_power(x, y, serial_number)

    power_conv = {}
    for x in range(1, max_x - 2):
        for y in range(1, max_y - 2):
            sub_grid = grid[x:x+3, y:y+3]
            total = 0
            for row in sub_grid:
                for value in row:
                    total += value
            power_conv[total] = (x, y)
    print(max(power_conv), power_conv[max(power_conv)])





main()
