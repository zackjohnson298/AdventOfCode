
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


def main():
    monkeys = get_input('input.txt')
    print(find_value(monkeys, 'root'))


main()
