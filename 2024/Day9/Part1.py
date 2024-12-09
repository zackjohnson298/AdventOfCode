from typing import *


def get_input(filename: str) -> List[int]:
    with open(filename) as file:
        return [int(char) for char in file.readline()]


def generate(disk_map: List[int]) -> List[Optional[int]]:
    file_id = 0
    output = []
    free_space = False
    disk_map = [value for value in disk_map]
    while disk_map:
        value = disk_map.pop(0)
        if free_space:
            output.extend([None]*value)
            free_space = False
        else:
            output.extend([file_id]*value)
            file_id += 1
            free_space = True
    return output


def main():
    disk_map = get_input('input.txt')
    # disk_map = [1,2,3,4,5]
    disk_map = generate(disk_map)
    line = ''
    for value in disk_map:
        line = line + ('.' if value is None else str(value))
    # end = None
    while None in disk_map:
        # print(''.join((str(value) if value is not None else '.') for value in disk_map))
        index = disk_map.index(None)
        end = disk_map.pop()
        print(index, len(disk_map))
        if index >= len(disk_map):
            break
        disk_map[index] = end
        while disk_map[-1] is None:
            disk_map.pop()
    # print(''.join((str(value) if value is not None else '.') for value in disk_map))
    print(sum([ii*value for ii, value in enumerate(disk_map)]))
    # print(line)

main()
