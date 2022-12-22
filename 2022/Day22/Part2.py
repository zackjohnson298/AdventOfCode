
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    monkeys = {}
    for line in lines:
        name, str_2 = line.split(': ')
        if str_2.isdigit():
            children = []
            op = None
            value = int(str_2)
        else:
            child1, op, child2 = str_2.split()
            children = (child1, child2)
            value = None
        monkey = {
            'name': name,
            'value': value,
            'op': op,
            'children': children
        }
        monkeys[name] = monkey
    return monkeys


def evaluate(values: [int, int], op: str):
    a, b = values
    string = f'{a} {op} {b}'
    return int(eval(string))


def find_value(monkeys, monkey_name):
    monkey = monkeys[monkey_name]
    if monkey['value'] is not None:
        return monkey['value']
    children_values = [find_value(monkeys, child_name) for child_name in monkey['children']]
    return evaluate(children_values, monkey['op'])


def get_path(monkeys, desired_monkey, path_so_far):
    monkey = monkeys[path_so_far[-1]]
    if desired_monkey in monkey['children']:
        return path_so_far + [desired_monkey], True
    for child in monkey['children']:
        new_path = path_so_far + [child]
        desired_path, found = get_path(monkeys, desired_monkey, new_path)
        if found:
            return desired_path, True
    return None, False


def main():
    monkeys = get_input('input.txt')
    path, found = get_path(monkeys, 'humn', ['root'])
    child_not_in_path = [monkey for monkey in monkeys['root']['children'] if monkey != path[1]][0]
    value = find_value(monkeys, child_not_in_path)

    for ii in range(1, len(path)-1):
        parent = path[ii]
        child_in_path = path[ii+1]
        child_not_in_path = monkeys[parent]['children'][1 - monkeys[parent]['children'].index(child_in_path)]
        value_not_in_path = find_value(monkeys, child_not_in_path)
        op = monkeys[parent]['op']
        if op == '/':
            if monkeys[parent]['children'].index(child_in_path) == 0:   # The one we're solving for
                value = value * value_not_in_path
            else:
                value = int(value_not_in_path / value)
        elif op == '+':
            value = value - value_not_in_path
        elif op == '-':
            if monkeys[parent]['children'].index(child_in_path) == 0:  # The one we're solving for
                value = value + value_not_in_path
            else:
                value = value_not_in_path - value
        else:
            value = int(value / value_not_in_path)
    print(value)


main()
