from Node import Node


class Grid:
    def __init__(self, from_file=None):
        self.nodes = []

        if from_file:
            self.from_file(from_file)

    def from_file(self, filepath):
        with open(filepath) as file:
            lines = file.read().splitlines()[2:]
        row = []
        for line in lines:
            node = Node(from_line=line)
            if node.pos[0] == len(self.nodes):
                row.append(node)
            else:
                self.nodes.append(row)
                row = [node]
        self.nodes.append(row)

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        for neighbor in neighbors.copy():
            nx, ny = neighbor
            if nx >= 0 and ny >= 0:
                try:
                    _ = self.nodes[nx][ny]
                except IndexError:
                    neighbors.remove(neighbor)
            else:
                neighbors.remove(neighbor)

        return neighbors


if __name__ == '__main__':
    grid = Grid(from_file='input.txt')
    print(grid.get_neighbors([13, 25]))

