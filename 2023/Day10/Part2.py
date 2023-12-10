from typing import List, Tuple, Dict, Optional, Union


PRINTCHARS = {
    '|': '|',
    'F': '┌',
    '-': '─',
    '7': '┐',
    'J': '┘',
    'L': '└'
}


class Node:
    def __init__(self, position: Tuple[int, int], kind: str):
        if kind not in '|-LJ7F':
            raise Exception(f'Invalid Kind: {kind}')
        self.kind = kind
        self.print_char = PRINTCHARS[self.kind]
        self.position = position

    @property
    def openings(self) -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
        r, c = self.position
        if self.kind == '|':
            return (r-1, c), (r+1, c)
        if self.kind == '-':
            return (r, c-1), (r, c+1)
        if self.kind == 'L':
            return (r-1, c), (r, c+1)
        if self.kind == 'J':
            return (r-1, c), (r, c-1)
        if self.kind == '7':
            return (r, c-1), (r+1, c)
        if self.kind == 'F':
            return (r, c+1), (r+1, c)
        return None

    def next_opening(self, entry_position: Tuple[int, int]) -> Tuple[int, int]:
        if entry_position not in self.openings:
            raise Exception(f'Invalid Entry position for node {self.kind}\nentry: {entry_position}\nopenings: {self.openings}')
        a, b = self.openings
        return a if b == entry_position else b

    def __eq__(self, other):
        if type(other) == Node:
            return self.position == other.position and self.kind == other.kind
        elif type(other) == tuple:
            return self.position == other
        else:
            raise Exception(f'Cannot compare object of type {type(other)} to Node')


class Grid:
    def __init__(self, lines: List[str]):
        # self.grid: List[List[Union[None, Node]]] = [[None for _ in line] for line in lines]
        self.nodes: Dict[Tuple[int, int], Node] = {}
        self.loop_nodes: List[Node] = []
        self.filler_positions: List[Tuple[int, int]] = []
        self.width = len(lines[0])
        self.height = len(lines)
        self.starting_node: Optional[Node] = None
        starting_pos: Optional[Tuple[int, int]] = None
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char in '|-LJF7':
                    pos = (r, c)
                    # self.grid[r][c] = Node(pos, char)
                    self.nodes[pos] = Node(pos, char)
                elif char == 'S':
                    starting_pos = (r, c)
        if starting_pos is None:
            raise Exception('Failed to find starting position')
        self._determine_start_node_kind(starting_pos)

    def _determine_start_node_kind(self, starting_pos: Tuple[int, int]):
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
        directions = {up: False, down: False, left: False, right: False}
        r, c = starting_pos
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            node = self.get_node((nr, nc))
            if node is not None and starting_pos in node.openings:
                directions[(dr, dc)] = True
        if directions[up] and directions[down]:
            kind = '|'
        elif directions[right] and directions[left]:
            kind = '-'
        elif directions[up] and directions[right]:
            kind = 'L'
        elif directions[up] and directions[left]:
            kind = 'J'
        elif directions[down] and directions[right]:
            kind = 'F'
        elif directions[down] and directions[left]:
            kind = '7'
        else:
            raise Exception('Could not determine starting node type')
        self.starting_node = Node(starting_pos, kind)
        self.nodes[starting_pos] = self.starting_node
        # self.grid[r][c] = self.starting_node

    def get_node(self, pos: Tuple[int, int]) -> Optional[Node]:
        return self.nodes.get(pos)
        # r, c = pos
        # if not 0 <= r < self.height or not 0 <= c < self.width:
        #     return None
        # return self.grid[r][c]

    def print(self):
        for r in range(self.height):
            row_str = ''
            for c in range(self.width):
                if self.starting_node and (r, c) == self.starting_node.position:
                    row_str = row_str + 'S'
                    continue
                node = self.get_node((r, c))
                if node and node in self.loop_nodes:
                    row_str = row_str + node.print_char
                elif (r, c) in self.filler_positions:
                    row_str = row_str + '*'
                else:
                    row_str = row_str + '.'
            print(row_str)
        print()

    def find_loop(self):
        node = self.starting_node
        position = node.position
        next_position = node.openings[0]
        while True:
            self.loop_nodes.append(node)
            node = self.get_node(next_position)
            if node == self.starting_node:
                break
            if node:
                next_position = node.next_opening(position)
                position = node.position
            else:
                raise Exception('Failed to find next node')

    def double(self):
        # self.print()
        if not self.loop_nodes:
            self.find_loop()
        self.width = 2*self.width
        self.height = 2*self.height
        new_nodes: Dict[Tuple[int, int], Node] = {}
        for node in self.nodes.values():
            r, c = node.position
            node.position = (2*r, 2*c)
            new_nodes[node.position] = node
        self.nodes = new_nodes
        for node in self.loop_nodes:
            for neighbor in node.openings:
                if neighbor not in self.filler_positions:
                    self.filler_positions.append(neighbor)
        # self.print()

    def neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        output = []
        r, c = pos
        for nr in [r-1, r, r+1]:
            for nc in [c-1, c, c+1]:
                if (nr, nc) != pos and 0 <= nr < self.height and 0 <= nc < self.width:
                    output.append((nr, nc))
        return output

    def find_enclosed_position_count(self) -> int:
        print('doubling')
        self.double()
        visited_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        print('searching')
        node_positions = [node.position for node in self.loop_nodes]
        # In case the loop reaches the edge of the grid somehow, we should make sure to start flood-fill from all edges
        edges = [(0, c) for c in range(0, self.width, 2)] + \
                [(self.height-1, c) for c in range(0, self.width, 2)] + \
                [(r, 0) for r in range(0, self.height, 2)] + \
                [(r, self.width-1) for r in range(0, self.height, 2)]
        for ii, edge in enumerate(edges):
            iterations = 0
            r, c = edge
            if visited_grid[r][r] or edge in node_positions + self.filler_positions:
                continue
            queue = [edge]
            while queue:
                if iterations % 100 == 0:
                    print(f'\tEdge: {ii},\tQueue: {len(queue)},\tIter: {iterations}')
                iterations += 1
                r, c = queue.pop(0)
                visited_grid[r][c] = True
                for neighbor in self.neighbors((r, c)):
                    nr, nc = neighbor
                    if not visited_grid[nr][nc] and neighbor not in node_positions + self.filler_positions + queue:
                        queue.append(neighbor)
        print('Counting enclosed positions')
        count = 0
        for r in range(0, self.height, 2):
            for c in range(0, self.width, 2):
                pos = (r, c)
                if not visited_grid[r][c] and pos not in self.filler_positions + node_positions:
                    count += 1
        return count


def get_input(filename) -> Grid:
    with open(filename) as file:
        lines = file.read().splitlines()
    return Grid(lines)


def main():
    grid = get_input('input.txt')
    print(grid.find_enclosed_position_count())


main()
