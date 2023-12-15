from typing import List, Tuple, Dict


class Grid:
    def __init__(self, lines: List[str]):
        self.state_map: Dict[Tuple, Tuple] = {}
        self.state_history: List[Tuple[Tuple, str]] = []
        self.round_rocks: List[Tuple[int, int]] = []
        self.fixed_rocks: List[Tuple[int, int]] = []
        self.height = len(lines)
        self.width = len(lines[0])
        for r in range(self.height):
            for c in range(self.width):
                if lines[r][c] == '#':
                    self.fixed_rocks.append((r, c))
                elif lines[r][c] == 'O':
                    self.round_rocks.append((r, c))

    @property
    def configuration(self) -> Tuple[Tuple[int, int]]:
        return tuple(sorted(rock for rock in self.round_rocks))

    def get_stacks(self, direction: str) -> List[Tuple[List[Tuple[int, int]], int]]:
        # Returns a list of (Stack, distance).
        #   A Stack is a contiguous grouping of rocks that would slide together.
        #   The distance is how far the Stack would slide.
        assert direction in 'nsew'

        def get_rock(a, b):
            if direction in 'ns':
                return b, a
            return a, b

        if direction == 'n':
            o_start, o_end, o_dir = 0, self.width, 1
            i_start, i_end, i_dir = 0, self.height, 1
        elif direction == 's':
            o_start, o_end, o_dir = 0, self.width, 1
            i_start, i_end, i_dir = self.height-1, -1, -1
        elif direction == 'e':
            o_start, o_end, o_dir = 0, self.height, 1
            i_start, i_end, i_dir = self.width-1, -1, -1
        else:
            o_start, o_end, o_dir = 0, self.height, 1
            i_start, i_end, i_dir = 0, self.width, 1

        output = []
        for o in range(o_start, o_end, o_dir):
            current_stack = []
            sliding_distance = 0
            sliding_rocks = 0
            for i in range(i_start, i_end, i_dir):
                rock = get_rock(o, i)
                if rock in self.round_rocks:
                    current_stack.append(rock)
                    sliding_rocks += 1
                    sliding_distance += 1
                elif rock not in self.fixed_rocks:
                    if current_stack:
                        distance = sliding_distance - sliding_rocks
                        output.append((current_stack, distance))
                        current_stack = []
                    sliding_distance += 1
                else:
                    if current_stack:
                        distance = sliding_distance - sliding_rocks
                        output.append((current_stack, distance))
                        current_stack = []
                    sliding_distance = 0
                    sliding_rocks = 0
            if current_stack:
                distance = sliding_distance - sliding_rocks
                output.append((current_stack, distance))
        return output

    def tilt(self, direction: str):
        assert direction in 'nsew'

        def get_new_rock(o_r, o_c, dist):
            if direction == 'n':
                return o_r - dist, o_c
            if direction == 's':
                return o_r + dist, o_c
            if direction == 'e':
                return o_r, o_c + dist
            if direction == 'w':
                return o_r, o_c - dist

        initial_state = (self.configuration, direction)
        new_configuration = self.state_map.get(initial_state)
        if new_configuration:
            self.round_rocks = list(new_configuration)
            return True
        for group, distance in self.get_stacks(direction):
            if distance == 0:
                continue
            for rock in group:
                index = self.round_rocks.index(rock)
                r, c = rock
                new_rock = get_new_rock(r, c, distance)
                self.round_rocks[index] = new_rock
        self.state_map[initial_state] = self.configuration
        self.state_history.append(initial_state)
        return False

    @property
    def score(self) -> int:
        total = 0
        for r, c in self.round_rocks:
            total += self.height - r
        return total

    def print(self):
        for r in range(self.height):
            line = ''
            for c in range(self.width):
                line = line + ('#' if (r, c) in self.fixed_rocks else 'O' if (r, c) in self.round_rocks else '.')
            print(line)
        print()

    def cycle(self) -> bool:
        loop_found = True
        for direction in 'nwse':
            loop_found &= self.tilt(direction)
        return loop_found

    def __eq__(self, other):
        return self.configuration == other.configuration


def get_input(filename) -> Grid:
    with open(filename) as file:
        lines = file.read().splitlines()
    return Grid(lines)


def main():
    grid = get_input('input.txt')
    count = 1000000000
    loop_indexes = []
    loop_scores = []
    first_index = None
    for ii in range(count):
        print(ii)
        loop_found = grid.cycle()
        if loop_found:
            if not loop_indexes:
                first_index = ii
                print(f'First index found: {first_index}')
            state = (grid.configuration, 'n')
            index = grid.state_history.index(state)
            if index not in loop_indexes:
                loop_scores.append(grid.score)
                loop_indexes.append(index)
            else:
                print(loop_scores[(count - (first_index + 1)) % len(loop_indexes)])
                return


main()
