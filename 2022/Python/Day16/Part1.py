import json
from Valve import Valve


def get_input(filename, starting_valve='AA'):
    with open(filename) as file:
        lines = file.read().splitlines()
    valves = [Valve(line) for line in lines]
    for valve_a in valves:
        for valve_b in valves:
            if valve_b != valve_a and valve_a.name in valve_b.neighbors:
                current_distance = valve_b.neighbors[valve_a.name]
                for neighbor, distance in valve_a.neighbors.items():
                    if neighbor == valve_b.name:
                        continue
                    if neighbor not in valve_b.neighbors:
                        valve_b.neighbors[neighbor] = current_distance + distance
                    else:
                        valve_b.neighbors[neighbor] = min(valve_b.neighbors[neighbor], current_distance + distance)
                if valve_a.flow_rate == 0:
                    valve_b.neighbors.pop(valve_a.name)

    return {valve.name: valve for valve in valves if valve.name == starting_valve or valve.flow_rate != 0}


def get_max_score(valve_map: {str: Valve}, current_valve, path_so_far=None, current_time=0, max_time=30):
    if path_so_far is None:
        path_so_far = []
    if current_time >= max_time:
        return 0, path_so_far
    valve = valve_map[current_valve]
    score = valve.flow_rate * (max_time - current_time)
    new_path = path_so_far + [current_valve]

    child_scores_arr = []
    for neighbor, distance in valve_map[current_valve].neighbors.items():
        if neighbor not in path_so_far:
            child_score = get_max_score(valve_map, neighbor, new_path, current_time + distance + 1, max_time)
            child_scores_arr.append(child_score)
    child_scores = max(child_scores_arr)
    return score + child_scores[0], [current_valve] + child_scores[1]


def main():
    valve_map = get_input('input.txt')
    score, path = get_max_score(valve_map, 'AA')
    print(score)


main()
