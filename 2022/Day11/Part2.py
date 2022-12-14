import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    monkeys = {}
    monkey = {}
    for ii, line in enumerate(lines):
        if ii % 7 == 0:
            lst = line.split()
            monkey = {'count': 0}
            monkeys[int(lst[1][:-1])] = monkey
        elif (ii - 1) % 7 == 0:
            items = [int(value) for value in line.split(': ')[1].split(', ') if value.isdigit()]
            monkey['items'] = items
        elif (ii - 2) % 7 == 0:
            a = line.split('= ')[1]
            operation = {}
            if '+' in a:
                operation['op'] = 'add'
                operation['value'] = int(a.split('+')[1])
            else:
                if a.count('old') == 1:
                    operation['op'] = 'mult'
                    operation['value'] = int(a.split('*')[1])
                else:
                    operation['op'] = 'square'
            monkey['operation'] = operation
        elif (ii - 3) % 7 == 0:
            monkey['test'] = {'value': int(line.split()[-1])}
        elif (ii - 4) % 7 == 0:
            monkey['test'][True] = int(line.split()[-1])
        elif (ii - 5) % 7 == 0:
            monkey['test'][False] = int(line.split()[-1])
    return monkeys


def find_lcm(monkeys):
    lcm = 1
    for value in [monkey['test']['value'] for monkey in monkeys.values()]:
        lcm *= value
    return lcm


def main():
    monkeys = get_input('input.txt')
    turns = 10000
    lcm = find_lcm(monkeys)
    for turn in range(turns):
        for monkey_key, monkey in sorted(monkeys.items()):
            for ii, item in enumerate(monkey['items']):
                monkey['count'] += 1
                operation = monkey['operation']
                if operation['op'] == 'add':
                    monkey['items'][ii] += operation['value']
                elif operation['op'] == 'mult':
                    monkey['items'][ii] *= operation['value']
                else:
                    monkey['items'][ii] *= monkey['items'][ii]
                if monkey['items'][ii] % monkey['test']['value'] == 0:
                    next_monkey = monkey['test'][True]
                else:
                    next_monkey = monkey['test'][False]
                monkeys[next_monkey]['items'].append(monkey['items'][ii] % lcm)
            monkey['items'] = []
        print(f'Round {turn}:')
        for key, monkey in sorted(monkeys.items()):
            print(key, monkey['items'])
        print()
        # _ = input()
    print('Counts:')
    for key, monkey in sorted(monkeys.items()):
        print(key, monkey['count'])
    print()

    counts = [monkey['count'] for monkey in monkeys.values()]
    a, b = sorted(counts)[-2:]
    print(a * b)


main()
