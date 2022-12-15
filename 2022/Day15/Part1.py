import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    sensors = []    # (sensor_position, beacon_position)
    beacons = []
    for line in lines:
        string1, string2 = line.split(': ')
        string1_2 = string1.split('at ')[1]
        string1_x, string1_y = string1_2.split(', ')
        sensor_x = int(string1_x.split('=')[1])
        sensor_y = int(string1_y.split('=')[1])
        sensors.append((sensor_x, sensor_y))

        string2_2 = string2.split('at ')[1]
        string2_x, string2_y = string2_2.split(', ')
        beacon_x = int(string2_x.split('=')[1])
        beacon_y = int(string2_y.split('=')[1])
        beacons.append((beacon_x, beacon_y))
    return sensors, beacons


def get_row_width(sensors: list, beacons: list):
    min_x = float('inf')
    max_x = -float('inf')
    for x, _ in sensors + beacons:
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
    return min_x, max_x


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def main():
    sensors, beacons = get_input('test_input.txt')
    min_x, max_x = get_row_width(sensors, beacons)
    sensors_with_distance = [(sensor, get_distance(sensor, beacon)) for sensor, beacon in zip(sensors, beacons)]
    total = 0
    y = 10 #2000000
    for x in range(min_x, max_x + 1):
        pos = (x, y)
        print((x-min_x)/(max_x - min_x))
        for sensor, min_distance in sensors_with_distance:
            if get_distance(pos, sensor) <= min_distance and pos not in beacons:
                total += 1
                break
    print(total)
    # print(get_row_width(sensors))

main()
