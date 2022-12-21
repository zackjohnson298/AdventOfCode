import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    reindeer = {}
    for line in lines:
        line = line.split()
        name = line[0]
        speed = int(line[3])
        max_flight_time = int(line[6])
        max_rest_time = int(line[-2])
        reindeer[name] = {
            'name': name,
            'speed': speed,
            'distance': 0,
            'time_flying': 0,
            'time_resting': 0,
            'points': 0,
            'max_flight_time': max_flight_time,
            'max_rest_time': max_rest_time,
            'is_flying': True
        }
    return reindeer


def award_points(reindeer):
    max_distance = max([deer['distance'] for deer in reindeer.values()])
    for deer in reindeer.values():
        if deer['distance'] == max_distance:
            deer['points'] += 1


def simulate(reindeer, max_time):
    for ii in range(max_time):
        for name, deer in reindeer.items():
            if deer['is_flying']:
                deer['distance'] += deer['speed']
                deer['time_flying'] += 1
                if deer['time_flying'] == deer['max_flight_time']:
                    deer['is_flying'] = False
                    deer['time_flying'] = 0
            else:
                deer['time_resting'] += 1
                if deer['time_resting'] == deer['max_rest_time']:
                    deer['is_flying'] = True
                    deer['time_resting'] = 0
        award_points(reindeer)


def main():
    reindeer = get_input('input.txt')
    simulate(reindeer, 2503)
    # print(json.dumps(reindeer, indent=4))
    max_points = max([deer['points'] for deer in reindeer.values()])
    print(max_points)


main()
