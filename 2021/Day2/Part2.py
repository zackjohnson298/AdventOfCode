

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
    aim = 0
    for direction, value in steps:
        if direction == 'forward':
            pos += value
            depth += aim*value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    print(pos, depth, pos*depth)

main()
