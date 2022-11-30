

def get_input():
    with open('input.txt') as file:
        lines = file.read().splitlines()
#     lines = '''forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2'''.splitlines()
    steps = []
    for line in lines:
        direction, value = line.split()
        steps.append([direction, int(value)])
    return steps


def main():
    steps = get_input()
    pos = 0
    depth = 0
    for direction, value in steps:
        if direction == 'forward':
            pos += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value
    print(pos, depth, pos*depth)

main()
