
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [tuple([int(value) for value in line.split(',')]) for line in lines]


def are_neighbors(point_a: (int, int, int), point_b: (int, int, int)):
    equal_list = [a == b for a, b in zip(point_a, point_b)]
    if sum(equal_list) == 2:
        index = equal_list.index(False)
        if abs(point_a[index] - point_b[index]) == 1:
            return True
    return False


def populate_neighbors(points: [(int, int, int)]):
    neighbors = {point: [] for point in points}
    for point_a in points:
        for point_b in points:
            if point_a == point_b or point_a in neighbors[point_b]:
                continue
            if are_neighbors(point_a, point_b):
                neighbors[point_a].append(point_b)
                neighbors[point_b].append(point_a)
    return neighbors


def main():
    points = get_input('input.txt')
    neighbors = populate_neighbors(points)
    total = 6*len(points)
    for key, value in neighbors.items():
        total -= len(value)
    print(total)


main()
