
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
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    return None


def find_value(monkeys, monkey_name):
    monkey = monkeys[monkey_name]
    if monkey['value'] is not None:
        return monkey['value']
    children_values = []
    if len(monkey['children']) == 0:
        raise ValueError(f'Error with monkey {monkey_name}')
    for child_name in monkey['children']:
        child_value = find_value(monkeys, child_name)
        children_values.append(child_value)
    return evaluate(children_values, monkey['op'])


def main():
    monkeys = get_input('input.txt')
    print(int(find_value(monkeys, 'root')))


main()
