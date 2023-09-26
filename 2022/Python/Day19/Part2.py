import json
from random import choice, shuffle, uniform


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    blueprints = {}
    for ii, line in enumerate(lines, start=1):
        line = line.split(': ')[1]
        ore_str, clay_str, obs_str, geo_str = line.split('. ')
        ore_cost_list = [int(char) for char in ore_str.split() if char.isdigit()]
        clay_cost_list = [int(char) for char in clay_str.split() if char.isdigit()]
        obs_cost_list = [int(char) for char in obs_str.split() if char.isdigit()]
        geo_cost_list = [int(char) for char in geo_str.split() if char.isdigit()]
        blueprint = {
            'ore': {
                'ore': ore_cost_list[0]
            },
            'clay': {
                'ore': clay_cost_list[0]
            },
            'obs': {
                'ore': obs_cost_list[0],
                'clay': obs_cost_list[1]
            },
            'geo': {
                'ore': geo_cost_list[0],
                'obs': geo_cost_list[1]
            }
        }
        blueprints[ii] = blueprint
    return blueprints


def can_build(robot_type, inventory, blueprint):
    cost = blueprint[robot_type]
    for key, value in cost.items():
        if inventory[key] < value:
            return False
    return True


def build_robot(robot_type, inventory, blueprint):
    cost = blueprint[robot_type]
    for key, value in cost.items():
        inventory[key] -= value


def update_inventory(robots, inventory):
    for key, value in robots.items():
        inventory[key] += value


def get_max_geodes(blueprint, minutes=24, iterations=20):
    max_geodes = 0
    count = 0
    for ii in range(iterations):
        geodes = simulate(blueprint, minutes)
        if geodes == max_geodes:
            count += 1
        elif geodes > max_geodes:
            max_geodes = geodes
            count = 1
    return max_geodes, count


def simulate(blueprint: {}, minutes=24) -> int:
    inventory = {'ore': 0, 'clay': 0, 'obs': 0, 'geo': 0}
    robots = {'ore': 1, 'clay': 0, 'obs': 0, 'geo': 0}
    prioritised_options = ['geo', 'obs', 'clay', 'ore']
    shuffle(prioritised_options)
    if uniform(0, 1) > 0.5:
        prioritised_options.remove('geo')
        prioritised_options.insert(0, 'geo')
    for minute in range(minutes):
        robots_being_built = {key: 0 for key in robots}
        # Randomly prioritize a certain robot:
        for robot in prioritised_options:
            if can_build(robot, inventory, blueprint) and uniform(0, 1) > 0.05:
                build_robot(robot, inventory, blueprint)
                robots_being_built[robot] += 1
                break
        update_inventory(robots, inventory)
        for key, value in robots_being_built.items():
            robots[key] += value
    return inventory['geo']


def main():
    blueprints = get_input('input.txt')
    max_geodes_1, count = get_max_geodes(blueprints[1], minutes=32, iterations=100000)
    print('1: ', max_geodes_1, count)
    max_geodes_2, count = get_max_geodes(blueprints[2], minutes=32, iterations=100000)
    print('2: ', max_geodes_2, count)
    max_geodes_3, count = get_max_geodes(blueprints[3], minutes=32, iterations=100000)
    print('3: ', max_geodes_3, count)
    print()
    print(max_geodes_1 * max_geodes_2 * max_geodes_3)


main()
