import numpy as np


DIRECTIONS = {
    'up': {
        'vector': np.array((-1, 0), dtype='int'),
        'L': 'left',
        'R': 'right'
    },
    'down': {
        'vector': np.array((1, 0), dtype='int'),
        'L': 'right',
        'R': 'left'
    },
    'left': {
        'vector': np.array((0, -1), dtype='int'),
        'L': 'down',
        'R': 'up'
    },
    'right': {
        'vector': np.array((0, 1), dtype='int'),
        'L': 'up',
        'R': 'down'
    }
}


def rot_z(angle):
    angle = np.pi * angle / 180
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ], dtype='int')


def get_steps(word):
    steps = []
    number_str = ''
    for char in word:
        if char.isdigit():
            number_str = number_str + char
        else:
            steps.append(int(number_str))
            steps.append(char)
            number_str = ''
    if number_str.isdigit():
        steps.append(int(number_str))
    return steps


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = []
    steps = get_steps(lines.pop())
    lines.pop()
    max_width = max([len(line) for line in lines])

    for line in lines:
        row = []
        line = line + ' '*(max_width - len(line))
        for char in line:
            if char == '.':
                row.append(0)
            elif char == '#':
                row.append(1)
            elif char == ' ':
                row.append(2)
        grid.append(row)
    return np.array(grid, dtype='int'), steps


def determine_segment(grid, pos: (int, int), segment_size):
    r, c = pos
    rows, cols = grid.shape
    if r < segment_size:
        if c < 2*segment_size:
            return 1
        return 2
    if r < 2*segment_size:
        return 3
    if r < 3*segment_size:
        if c < segment_size:
            return 4
        return 5
    return 6


def get_next_pos(grid, pos, direction, size=50):
    next_pos = tuple(np.array(pos) + DIRECTIONS[direction]['vector'])
    _ = grid.shape
    next_direction = direction
    rows, cols = grid.shape
    if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= rows or next_pos[1] >= cols or grid[next_pos] == 2:
        current_segment = determine_segment(grid, pos, size)
        if current_segment == 1:
            # print(1)
            if direction == 'left': #(direction == np.array((0, -1))).all():
                # print('left to 4')
                next_pos = (3*size - 1 - pos[0], 0)
                next_direction = 'right' #np.array((0, 1)).T
            elif direction == 'up': #(direction == np.array((-1, 0))).all():
                # print('up to 6')
                next_pos = (2*size+pos[1], 0)
                next_direction = 'right' #np.array((0, 1)).T
        elif current_segment == 2:
            # print(2)
            if direction == 'up': #(direction == np.array((-1, 0))).all():
                # print('up to 6')
                next_pos = (4*size-1, pos[1] - 2*size)
                next_direction = 'up' #np.array((-1, 0)).T
            elif direction == 'right': #(direction == np.array((0, 1))).all():
                # print('right to 5')
                next_pos = (3*size - 1 - pos[0], 2*size - 1)
                next_direction = 'left' #np.array((0, -1)).T
            elif direction == 'down': #(direction == np.array((1, 0))).all():
                # print('down to 3')
                next_pos = (pos[1] - size, 2*size - 1)
                next_direction = 'left' #np.array((0, -1)).T
        elif current_segment == 3:
            # print(3)
            if direction == 'left': #(direction == np.array((0, -1))).all():
                # print('left to 4')
                next_pos = (2*size, pos[0]-size)
                next_direction = 'down' # np.array((1, 0)).T
            elif direction == 'right': # '(direction == np.array((0, 1))).all():
                # print('right to 2')
                next_pos = (size-1, pos[0]+size)
                next_direction = 'up' # np.array((-1, 0)).T
        elif current_segment == 4:
            # print(4)
            if direction == 'up': # '(direction == np.array((-1, 0))).all():
                # print('up to 3')
                next_pos = (pos[1]+size, size)
                next_direction = 'right' # np.array((0, 1)).T
            elif direction == 'left': # '(direction == np.array((0, -1))).all():
                # print('left to 1')
                next_pos = (3*size-1 - pos[0], size)
                next_direction = 'right' # np.array((0, 1)).T
        elif current_segment == 5:
            # print(5)
            if direction == 'right': # '(direction == np.array((0, 1))).all():
                # print('right to 2')
                next_pos = (3*size-1 - pos[0], 3*size-1)
                next_direction = 'left' # np.array((0, -1)).T
            elif direction == 'down': # '(direction == np.array((1, 0))).all():
                # print('down to 6')
                next_pos = (2*size + pos[1], size-1)
                next_direction = 'left' # np.array((0, -1)).T
        elif current_segment == 6:
            # print(6)
            if direction == 'right': # '(direction == np.array((0, 1))).all():
                # print('right to 5')
                next_pos = (3*size-1, pos[0]-2*size)
                next_direction = 'up' # np.array((-1, 0)).T
            elif direction == 'down': # '(direction == np.array((1, 0))).all():
                # print('down to 2')
                next_pos = (0, pos[1] + 2*size)
                next_direction = 'down' # np.array((1, 0)).T
            elif direction == 'left': # '(direction == np.array((0, -1))).all():
                # print('left to 1')
                next_pos = (0, pos[0] - 2*size)
                next_direction = 'down' # np.array((1, 0)).T
    # elif grid[next_pos] == 0:
    #     return next_pos, direction, blocked
    # if grid[next_pos] == 1:
    #     blocked = True
    #     return pos, direction, blocked
    return next_pos, next_direction


def draw_grid(grid):
    for row in grid:
        for value in row:
            if value == 0:
                print('.', end='')
            if value == 1:
                print('#', end='')
            if value == 2:
                print(' ', end='')
        print()
    print()


def get_facing(direction):
    if direction == 'right': #(direction == np.array((0, 1)).T).all():
        return 0
    if direction == 'down': #'(direction == np.array((1, 0)).T).all():
        return 1
    if direction == 'left': #'(direction == np.array((0, -1)).T).all():
        return 2
    if direction == 'up': #'(direction == np.array((-1, 0)).T).all():
        return 3
    return None


def validate_test():
    grid, steps = get_input('test_input_2.txt')

    # print(get_next_pos(grid, (0, 14), 'right'))
    print()
    print('Running Validation...')
    expected = {
        1: {
            ((4, 5), 'left'): ((10, 0), 'right', False),
            ((0, 5), 'left'): ((14, 0), 'right', False),
            ((0, 5),   'up'): ((15, 0), 'right', False),
            ((0, 9),   'up'): ((19, 0), 'right', False),
            ((4, 6), 'down'): ((5, 6), 'down', False),
            ((1, 6),   'up'): ((0, 6), 'up', False),
            ((3, 5), 'left'): ((3, 5), 'left', True),
            ((0, 8),   'up'): ((0, 8), 'up', True),
        },
        2: {
            ((0, 10), 'up'): ((19, 0), 'up', False),
            ((0, 14), 'up'): ((19, 4), 'up', False),
            ((0, 14), 'right'): ((14, 9), 'left', False),
            ((4, 14), 'right'): ((10, 9), 'left', False),
            ((4, 14), 'down'): ((9, 9), 'left', False),
            ((4, 10), 'down'): ((5, 9), 'left', False),
            ((0, 11), 'up'): ((0, 11), 'up', True),
            ((3, 14), 'right'): ((3, 14), 'right', True),
            ((4, 13), 'down'): ((4, 13), 'down', True),
        },
        3: {
            ((5,  5), 'left'): ((10, 0), 'down', False),
            ((9,  5), 'left'): ((10, 4), 'down', False),
            ((9, 9), 'right'): ((4, 14), 'up', False),
            ((5, 9), 'right'): ((4, 10), 'up', False),
            ((7, 5), 'left'): ((7,  5), 'left', True),
            ((7, 9), 'right'): ((7, 9), 'right', True),
        },
        4: {
            ((14, 0), 'left'): ((0, 5), 'right', False),
            ((10, 0), 'left'): ((4, 5), 'right', False),
            ((10, 0), 'up'): ((5, 5), 'right', False),
            ((10, 4), 'up'): ((9, 5), 'right', False),
            ((12, 0), 'left'): ((12, 0), 'left', True),
            ((10, 3), 'up'): ((10, 3), 'up', True),
        },
        5: {
            ((10, 9), 'right'): ((4, 14), 'left', False),
            ((14, 9), 'right'): ((0, 14), 'left', False),
            ((14, 9), 'down'): ((19, 4), 'left', False),
            ((14, 5), 'down'): ((15, 4), 'left', False),
            ((12, 9), 'right'): ((12, 9), 'right', True),
            ((14, 8), 'down'): ((14, 8), 'down', True),
        },
        6: {
            ((15, 0), 'left'): ((0, 5), 'down', False),
            ((19, 0), 'left'): ((0, 9), 'down', False),
            ((19, 0), 'down'): ((0, 10), 'down', False),
            ((19, 4), 'down'): ((0, 14), 'down', False),
            ((19, 4), 'right'): ((14, 9), 'up', False),
            ((15, 4), 'right'): ((14, 5), 'up', False),
            ((17, 0), 'left'): ((17, 0), 'left', True),
            ((19, 2), 'down'): ((19, 2), 'down', True),
            ((17, 4), 'right'): ((17, 4), 'right', True),
        },

    }
    for face, test in expected.items():
        print()
        print(f'Face {face}:')
        for state, expected_output in test.items():
            pos = state[0]
            direction = state[1]
            output = get_next_pos(grid, pos, direction)
            if output != expected_output:
                print(f'\tFailed')
                print(f'\t\t   Input: {state}')
                print(f'\t\tExpected: {expected_output}')
                print(f'\t\t  Actual: {output}')
                return
            else:
                print(f'\tPass: {state} -> {output}')


def validate_actual():
    grid, steps = get_input('input.txt')

    print(get_next_pos(grid, (100, 0), 'up'))
    print()
    print('Running Validation...')
    expected = {
        ((0, 149), 'right'): ((149, 99), 'left'),
        ((49, 149), 'right'): ((100, 99), 'left'),

        ((50, 99), 'right'): ((49, 100), 'up'),
        ((99, 99), 'right'): ((49, 149), 'up'),

        ((100, 99), 'right'): ((49, 149), 'left'),
        ((149, 99), 'right'): ((0, 149), 'left'),

        ((150, 49), 'right'): ((149, 50), 'up'),
        ((199, 49), 'right'): ((149, 99), 'up'),

        ((0, 50), 'left'): ((149, 0), 'right'),
        ((49, 50), 'left'): ((100, 0), 'right'),

        ((50, 50), 'left'): ((100, 0), 'down'),
        ((99, 50), 'left'): ((100, 49), 'down'),

        ((100, 0), 'left'): ((49, 50), 'right'),
        ((149, 0), 'left'): ((0, 50), 'right'),

        ((150, 0), 'left'): ((0, 50), 'down'),
        ((199, 0), 'left'): ((0, 99), 'down'),

        ((100, 0), 'up'): ((50, 50), 'right'),
        ((100, 49), 'up'): ((99, 50), 'right'),

        ((0, 50), 'up'): ((150, 0), 'right'),
        ((0, 99), 'up'): ((199, 0), 'right'),

        ((0, 100), 'up'): ((199, 0), 'up'),
        ((0, 149), 'up'): ((199, 49), 'up'),

        ((199, 0), 'down'): ((0, 100), 'down'),
        ((199, 49), 'down'): ((0, 149), 'down'),

        ((149, 50), 'down'): ((150, 49), 'left'),
        ((149, 99), 'down'): ((199, 49), 'left'),

        ((49, 100), 'down'): ((50, 99), 'left'),
        ((49, 149), 'down'): ((99, 99), 'left'),
    }
    for state, expected_output in expected.items():
        pos = state[0]
        direction = state[1]
        output = get_next_pos(grid, pos, direction)
        if output != expected_output:
            print(f'\tFailed')
            print(f'\t\t   Input: {state}')
            print(f'\t\tExpected: {expected_output}')
            print(f'\t\t  Actual: {output}')
            return
        else:
            print(f'\tPass: {state} -> {output}')


def main():
    grid, steps = get_input('input.txt')
    pos = np.array((0, 0)).T
    _, cols = grid.shape
    for c in range(cols):
        if grid[0, c] == 0:
            pos = np.array((0, c)).T
            break
    print(pos)
    direction = 'right' #np.array((0, 1)).T

    # _ = input(pos)
    for step in steps:
        if type(step) == int:
            for _ in range(step):
                next_pos, next_direction = get_next_pos(grid, pos, direction)
                if grid[next_pos] == 1:
                    print('stuck')
                    break
                pos, direction = next_pos, next_direction
                # print(pos, direction)
        elif step in 'LR':
            direction = DIRECTIONS[direction][step] #rot_z(-90) @ direction
        else:
            print(f'unhandled step: {step}')
    print()
    a, b = np.array(pos) + np.ones(np.array(pos).shape, dtype='int')
    facing = get_facing(direction)
    print(a, b, facing)
    print(1000*a + 4*b + facing)


# validate_actual()
main()
