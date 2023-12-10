from typing import List, Tuple, Dict, Optional


class Node:
    def __init__(self, position: Tuple[int, int], kind: str):
        if kind not in '|-LJ7F':
            raise Exception(f'Invalid Kind: {kind}')
        self.kind = kind
        self.position = position
        self.openings: Optional[Tuple[Tuple[int, int], Tuple[int, int]]] = None
        r, c = self.position
        if self.kind == '|':
            self.openings = ((r-1, c), (r+1, c))
        if self.kind == '-':
            self.openings = ((r, c-1), (r, c+1))
        if self.kind == 'L':
            self.openings = ((r-1, c), (r, c+1))
        if self.kind == 'J':
            self.openings = ((r-1, c), (r, c-1))
        if self.kind == '7':
            self.openings = ((r, c-1), (r+1, c))
        if self.kind == 'F':
            self.openings = ((r, c+1), (r+1, c))

    def next_opening(self, entry_position: Tuple[int, int]) -> Tuple[int, int]:
        if entry_position not in self.openings:
            raise Exception(f'Invalid Entry position for node {self.kind}\nentry: {entry_position}\nopenings: {self.openings}')
        a, b = self.openings
        return a if b == entry_position else b

    def __eq__(self, other):
        return self.position == other.position and self.kind == other.kind


class Grid:
    def __init__(self, lines: List[str]):
        self.nodes: Dict[Tuple[int, int], Node] = {}
        self.width = len(lines[0])
        self.height = len(lines)
        self.starting_node: Optional[Node] = None
        self.starting_pos: Optional[Tuple[int, int]] = None
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char in '|-LJF7':
                    pos = (r, c)
                    self.nodes[pos] = Node(pos, char)
                elif char == 'S':
                    self.starting_pos = (r, c)
        self._determine_start_node_kind()

    def _determine_start_node_kind(self):
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
        directions = {up: False, down: False, left: False, right: False}
        r, c = self.starting_pos
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            node = self.nodes.get((nr, nc))
            if node and self.starting_pos in node.openings:
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
        self.starting_node = Node(self.starting_pos, kind)
        self.nodes[self.starting_pos] = self.starting_node

    def print(self):
        for r in range(self.height):
            row_str = ''
            for c in range(self.width):
                if (r, c) == self.starting_pos:
                    row_str = row_str + 'S'
                    continue
                node = self.nodes.get((r, c))
                if node:
                    row_str = row_str + node.kind
                else:
                    row_str = row_str + '.'
            print(row_str)
        print()

    # def find_loop(self, path_so_far: List[Node]):
    #     if not path_so_far:
    #         node = self.starting_node
    #     else:
    #         node = path_so_far[-1]
    #     for new_node_position in node.openings:
    #         new_node = self.nodes.get(new_node_position)
    #         if new_node == self.starting_node:
    #
    #         if new_node and new_node not in path_so_far:
    #


def get_input(filename) -> Grid:
    with open(filename) as file:
        lines = file.read().splitlines()
    return Grid(lines)


def main():
    grid = get_input('input.txt')
    # grid.print()
    node = grid.starting_node
    position = node.position
    next_position = node.openings[0]
    count = 0
    while True:
        count += 1
        node = grid.nodes.get(next_position)
        if node == grid.starting_node:
            break
        if node:
            next_position = node.next_opening(position)
            position = node.position
        else:
            raise Exception('Failed to find next node')
    print(count // 2)

main()
