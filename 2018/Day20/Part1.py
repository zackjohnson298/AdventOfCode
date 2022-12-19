import numpy as np
'''
Incomplete
'''


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return line[1:]


# def navigate(code: str, pos: (int, int), doors: [(int, int)], rooms: [(int, int)]):
#     # if code == '$':
#     #     return pos
#     for char in code:
#         if char in '|)':
#             return pos
#         if char == '(':
#
#
#         if char in 'NSEW':
#             room = None
#             door = None
#             if char == 'N':
#                 door = (pos[0], pos[1] + 1)
#                 room = (pos[0], pos[1] + 2)
#             elif char == 'S':
#                 door = (pos[0], pos[1] - 1)
#                 room = (pos[0], pos[1] - 2)
#             elif char == 'E':
#                 door = (pos[0] + 1, pos[1])
#                 room = (pos[0] + 2, pos[1])
#             elif char == 'S':
#                 door = (pos[0] - 1, pos[1])
#                 room = (pos[0] - 2, pos[1])
#             pos = room
#             doors.append(door)
#             rooms.append(room)
#     return pos




def main():
    code = get_input('input.txt')
    doors = []
    rooms = []
    navigate(code, (0, 0), doors, rooms)


main()
