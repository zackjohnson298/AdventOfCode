
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    bots = []
    for line in lines:
        pos_str, r_str = line.split(', ')
        pos_str = pos_str.replace('>', '')
        pos_str = pos_str.replace('pos=<', '')
        pos = tuple([int(value) for value in pos_str.split(',')])
        r = int(r_str.split('=')[1])
        bots.append((pos, r))
    return bots


def get_distance(point_a, point_b):
    return sum([abs(a - b) for a, b in zip(point_a, point_b)])


def main():
    bots = get_input('input.txt')
    max_r = max([bot[1] for bot in bots])
    max_bot = None
    for bot in bots:
        if bot[1] == max_r:
            max_bot = bot
            break
    count = 0
    for bot in bots:
        if get_distance(bot[0], max_bot[0]) <= max_r:
            count += 1
    print(count)


main()
