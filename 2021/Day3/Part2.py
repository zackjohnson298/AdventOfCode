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
    return [[int(value) for value in line] for line in lines]


def find_ogr(old_data):
    data = old_data.copy()
    for col in range(len(data[0])):
        zero_count = [row[col] for row in data].count(0)
        one_count = [row[col] for row in data].count(1)
        if zero_count > one_count:
            value = 0
        elif one_count > zero_count:
            value = 1
        else:
            value = 1
        invalid_rows = [row for row in range(len(data)) if data[row][col] != value]
        for ii in reversed(invalid_rows):
            data.pop(ii)
        if len(data) == 1:
            row = data[0]
            return sum([row[ii] * (2 ** (len(row) - ii - 1)) for ii in range(len(row))])
    return None


def find_co2(old_data):
    data = old_data.copy()
    for col in range(len(data[0])):
        zero_count = [row[col] for row in data].count(0)
        one_count = [row[col] for row in data].count(1)
        if zero_count > one_count:
            value = 1
        elif one_count > zero_count:
            value = 0
        else:
            value = 0
        invalid_rows = [row for row in range(len(data)) if data[row][col] != value]
        for ii in reversed(invalid_rows):
            data.pop(ii)
        if len(data) == 1:
            row = data[0]
            return sum([row[ii] * (2 ** (len(row) - ii - 1)) for ii in range(len(row))])
    return None

def main():
    raw_data = get_input()
    ogr = find_ogr(raw_data)
    co2 = find_co2(raw_data)
    print(ogr, co2, ogr*co2)


main()
