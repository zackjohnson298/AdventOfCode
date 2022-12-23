import numpy as np


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


def rotate_matrix_counterclockwise(m, count=1):
    for _ in range(count):
        m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
    return m


''' Specific to Test Input '''
def get_test_mapping():
    size = 4
    mapping = {
        'facing': {
            1: np.eye(2),
            2: np.eye(2),
            3: np.eye(2),
            4: rot_z(-90),
            5: np.eye(2),
            6: rot_z(180)
        }
    }
    position_map = {}   # New grid position to original grid position
    # Face 1, 3, and 5 (3 is 4 on original)
    for r in range(3*size):
        for c in range(size):
            position_map[(r, c+size)] = (r, c+2*size)
    # Face 2 (3 on original)
    for r in range(size):
        for c in range(size):
            position_map[(r+size, c)] = (r+size, c+size)
    # Face 4 (6 on original)
    original_face_6 = [[(r+2*size, c+3*size) for c in range(size)] for r in range(size)]
    rotated_face_6 = rotate_matrix_counterclockwise(original_face_6)
    for r in range(size):
        for c in range(size):
            position_map[(r+size, c+2*size)] = rotated_face_6[r][c]
    # Face 6 (2 on original)
    original_face_2 = [[(r+size, c) for c in range(size)] for r in range(size)]
    rotated_face_2 = rotate_matrix_counterclockwise(original_face_2, count=2)
    for r in range(size):
        for c in range(size):
            position_map[(r+3*size, c+size)] = rotated_face_2[r][c]
    mapping['positions'] = position_map
    return mapping


def get_net_from_test_grid(grid):
    test_mapping = get_test_mapping()
    new_grid = 2*np.ones((16, 12))
    for new, old in test_mapping['positions'].items():
        new_grid[new] = grid[old]
    return new_grid, test_mapping


'''Specific to Actual Input'''
def get_mapping():
    size = 50
    mapping = {
        'facing': {
            1: np.eye(2),
            2: rot_z(90),
            3: np.eye(2),
            4: rot_z(90),
            5: np.eye(2),
            6: rot_z(-90)
        }
    }
    position_map = {}   # New grid position to original grid position
    # Face 1, 3, and 5
    for r in range(3*size):
        for c in range(size):
            position_map[(r, c+size)] = (r, c+size)
    # Face 2
    original_face_2 = [[(r+2*size, c) for c in range(size)] for r in range(size)]
    rotated_face_2 = rotate_matrix_counterclockwise(original_face_2, count=3)
    for r in range(size):
        for c in range(size):
            position_map[(r+size, c)] = rotated_face_2[r][c]
    # Face 4 (6 on original)
    original_face_4 = [[(r, c+2*size) for c in range(size)] for r in range(size)]
    rotated_face_4 = rotate_matrix_counterclockwise(original_face_4, count=3)
    for r in range(size):
        for c in range(size):
            position_map[(r+size, c+2*size)] = rotated_face_4[r][c]
    # Face 6 (2 on original)
    original_face_6 = [[(r+3*size, c) for c in range(size)] for r in range(size)]
    rotated_face_6 = rotate_matrix_counterclockwise(original_face_6)
    for r in range(size):
        for c in range(size):
            position_map[(r+3*size, c+size)] = rotated_face_6[r][c]
    mapping['positions'] = position_map
    return mapping


def get_net_from_grid(grid):
    mapping = get_mapping()
    new_grid = 2*np.ones((4*50, 3*50))
    for new, old in mapping['positions'].items():
        new_grid[new] = grid[old]
    return new_grid, mapping


def determine_segment(grid, pos: (int, int), segment_size):
    r, c = pos
    rows, cols = grid.shape
    if r < segment_size:
        return 1
    if r < 2*segment_size:
        if c < segment_size:
            return 2
        if c < 2*segment_size:
            return 3
        if c < 3*segment_size:
            return 4
    if r < 3*segment_size:
        return 5
    return 6


def get_next_pos(grid, pos, direction):
    next_pos = (pos + direction)
    next_direction = direction
    if (np.array((0, 0)).T > next_pos).any() or (np.array(grid.shape).T <= next_pos).any() or grid[tuple(next_pos)] == 2:
        rows, cols = grid.shape
        size = int(cols/3)
        current_segment = determine_segment(grid, pos, size)
        if current_segment == 1:
            print(1)
            if (direction == np.array((0, -1))).all():
                print('left')
                next_pos = np.array((size, pos[0])).T
                next_direction = np.array((1, 0)).T
            elif (direction == np.array((0, 1))).all():
                print('right')
                next_pos = np.array((size, 3*size - pos[0] - 1)).T
                next_direction = np.array((1, 0)).T
            elif (direction == np.array((-1, 0))).all():
                print('up')
                next_pos = np.array((4*size-1, pos[1])).T
                next_direction = np.array((-1, 0)).T
        elif current_segment == 2:
            print(2)
            if (direction == np.array((-1, 0))).all():
                print('up')
                next_pos = np.array((pos[1], size)).T
                next_direction = np.array((0, 1)).T
            elif (direction == np.array((0, -1))).all():
                print('left')
                next_pos = np.array((pos[0], 3*size - 1)).T
                next_direction = np.array((0, -1)).T
            elif (direction == np.array((1, 0))).all():
                print('down')
                next_pos = np.array((3*size - 1 - pos[1], size)).T
                next_direction = np.array((0, 1)).T
        elif current_segment == 4:
            print(4)
            if (direction == np.array((-1, 0))).all():
                print('up')
                next_pos = np.array((3*size-1 - pos[1], 2*size-1)).T
                next_direction = np.array((0, -1)).T
            elif (direction == np.array((1, 0))).all():
                print('down')
                next_pos = np.array((pos[1], 2*size-1)).T
                next_direction = np.array((0, -1)).T
            elif (direction == np.array((0, 1))).all():
                print('right')
                next_pos = np.array((pos[0], 0)).T
                next_direction = np.array((0, 1)).T
        elif current_segment == 5:
            print(5)
            if (direction == np.array((0, 1))).all():
                print('right')
                next_pos = np.array((2*size-1, pos[0])).T
                next_direction = np.array((-1, 0)).T
            elif (direction == np.array((0, -1))).all():
                print('left')
                next_pos = np.array((2*size-1, 3*size - 1 - pos[0])).T
                next_direction = np.array((-1, 0)).T
        elif current_segment == 6:
            print(6)
            if (direction == np.array((0, 1))).all():
                print('right')
                next_pos = np.array((5*size-1-pos[0], 3*size-1)).T
                next_direction = np.array((-1, 0)).T
            elif (direction == np.array((0, -1))).all():
                print('left')
                next_pos = np.array((5*size-1-pos[0], 0)).T
                next_direction = np.array((0, 1)).T
            elif (direction == np.array((1, 0))).all():
                print('down')
                next_pos = np.array((0, pos[1])).T
                next_direction = np.array((1, 0)).T
    elif grid[tuple(next_pos)] == 0:
        return next_pos, direction
    if grid[tuple(next_pos)] == 1:
        print('blocked')
        return pos, direction
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
    if (direction == np.array((0, 1)).T).all():
        return 0
    if (direction == np.array((1, 0)).T).all():
        return 1
    if (direction == np.array((0, -1)).T).all():
        return 2
    if (direction == np.array((-1, 0)).T).all():
        return 3
    return None


def validate():
    grid, steps = get_input('input.txt')
    grid, mapping = get_net_from_grid(grid)
    draw_grid(grid)


def main():
    grid, steps = get_input('input.txt')
    grid, mapping = get_net_from_grid(grid)
    pos = np.array((0, 0)).T
    rows, cols = grid.shape
    for c in range(cols):
        if grid[0, c] == 0:
            pos = np.array((0, c)).T
            break
    direction = np.array((0, 1)).T
    path = [tuple(pos)]
    for step in steps:
        if type(step) == int:
            for _ in range(step):
                pos, direction = get_next_pos(grid, pos, direction)
                path.append(tuple(pos))
        elif step == 'R':
            direction = rot_z(-90) @ direction
        elif step == 'L':
            direction = rot_z(90) @ direction
        else:
            print(f'unhandled step: {step}')
    print()
    mapped_position = np.array(mapping['positions'][tuple(pos)]) + np.array((1, 1))
    print('position:', mapped_position)
    final_segment = determine_segment(grid, pos, int(grid.shape[1]/3))
    print('segment:', final_segment)
    mapped_direction = mapping['facing'][final_segment]@direction
    facing = get_facing(mapped_direction)
    print('facing:', facing)
    print('Direction:', direction)
    print('mapped direction:', mapped_direction)

    print()

    a, b = mapped_position
    print(1000*a + 4*b + facing)
    # row, col = pos + np.array((1, 1)).T
    # if (direction == np.array((0, 1)).T).all():
    #     facing = 0
    # if (direction == np.array((1, 0)).T).all():
    #     facing = 1
    # if (direction == np.array((0, -1)).T).all():
    #     facing = 2
    # if (direction == np.array((-1, 0)).T).all():
    #     facing = 3
    #
    # print(row, col, facing)
    # print(1000 * row + 4 * col + facing)

main()

# validate()