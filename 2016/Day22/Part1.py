from Grid import Grid
from Node import Node


def is_valid(node_a: Node, node_b: Node):
    if node_a.used == 0:
        return False
    if node_a.pos == node_b.pos:
        return False
    if node_a.used > node_b.avail:
        return False
    return True


def find_pairs(grid: Grid):
    count = 0
    for x, row in enumerate(grid.nodes):
        for y, node_a in enumerate(row):
            for nx, row_b in enumerate(grid.nodes):
                for ny, node_b in enumerate(row_b):
                    if is_valid(node_a, node_b):
                        count += 1
    return count


def main():
    grid = Grid(from_file='input.txt')
    print(find_pairs(grid))


main()
