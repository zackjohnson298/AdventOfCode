
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


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def search(sensors_with_distances: {(int, int): int}, x_window: (int, int), y_window: (int, int)):
    for y in range(y_window[0], y_window[1]+1):
        print(round(100*y/y_window[1], 3), '%')
        x = x_window[0]
        while x < x_window[1]:
            for sensor, min_distance in sorted(sensors_with_distances.items()):
                distance = get_distance((x, y), sensor)
                if distance <= min_distance:
                    x = sensor[0] + min_distance - abs(sensor[1] - y) + 1
                    break
            else:
                return x, y
    return None, None


def validate(sensors_with_distance, pos, debug=False):
    for sensor, min_distance in sensors_with_distance.items():
        distance = get_distance(sensor, pos)
        if distance <= min_distance:
            if debug:
                print(f'Invalid, Sensor: {sensor}, Min Distance: {min_distance}, Distance: {distance}')
            return False
    if debug:
        print('Valid')
    return True


def main():
    sensors, beacons = get_input('input.txt')
    sensors_with_distance = {sensor: get_distance(sensor, beacon) for sensor, beacon in zip(sensors, beacons)}
    x_window = (0, 4000000)
    y_window = (0, 4000000)

    pos = search(sensors_with_distance, x_window, y_window)
    print()
    if pos != (None, None):
        print(validate(sensors_with_distance, pos))
        print(pos, 4000000*pos[0] + pos[1])
    else:
        print('Position not found')


main()
