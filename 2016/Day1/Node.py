
class Node:
    def __init__(self, from_line=None):
        self.pos = None
        self.avail = None
        self.used = None
        self.size = None
        self.use_percent = None
        if from_line:
            self.from_line(from_line)

    def from_line(self, line):
        items = line.split()
        pos_strings = items[0].split('-')[1:]
        self.pos = [int(string[1:]) for string in pos_strings]
        self.size = int(items[1][:-1])
        self.used = int(items[2][:-1])
        self.avail = int(items[3][:-1])
        self.use_percent = int(items[4][:-1])


if __name__ == '__main__':
    import json
    node = Node(from_line='/dev/grid/node-x0-y14    93T   71T    22T   76%')
    print(json.dumps(node.__dict__, indent=4))
