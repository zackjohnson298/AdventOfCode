import json
from random import choice


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


def get_max_geodes(blueprint, minutes=24, max_build_attempts=10, iterations=20):
    geodes = [simulate(blueprint, minutes, max_build_attempts) for _ in range(iterations)]
    return geodes


def simulate(blueprint: {}, minutes=24, max_build_attempts=10) -> int:
    inventory = {'ore': 0, 'clay': 0, 'obs': 0, 'geo': 0}
    robots = {'ore': 1, 'clay': 0, 'obs': 0, 'geo': 0}
    for minute in range(minutes):
        robots_being_built = {key: 0 for key in robots}
        # Randomly prioritize a certain robot:
        for robot in ['geo', 'obs', 'clay', 'ore']:
            if can_build(robot, inventory, blueprint) and choice([0, 1, 1]) == 1:
                build_robot(robot, inventory, blueprint)
                robots_being_built[robot] += 1
                break
        update_inventory(robots, inventory)
        for key, value in robots_being_built.items():
            robots[key] += value
    return inventory['geo']


def main():
    blueprints = get_input('input.txt')
    total = 0
    for print_id, blueprint in blueprints.items():
        print(print_id)
        total += print_id * max(get_max_geodes(blueprint, iterations=10000))
    print()
    print(total)


main()
