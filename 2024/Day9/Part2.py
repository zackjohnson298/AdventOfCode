from typing import *


class Block:
    def __init__(self, file_id: Optional[int], position: int, size: int):
        self.file_id = file_id
        self.position = position
        self.size = size

    def to_str(self) -> str:
        return ''.join(('.' if self.file_id is None else str(self.file_id) for _ in range (self.size)))

    def could_fit(self, other: 'Block') -> bool:
        return self.size >= other.size

    @property
    def checksum(self) -> Optional[int]:
        if self.file_id is None:
            return None
        return sum([self.file_id * (self.position + ii) for ii in range(self.size)])


def get_input(filename: str) -> List[int]:
    with open(filename) as file:
        return [int(char) for char in file.readline()]


def generate(disk_map: List[int]) -> Tuple[List[Block], List[Block]]:
    file_id = 0
    blocks = []
    spaces = []
    free_space = False
    position = 0
    disk_map = [value for value in disk_map]
    while disk_map:
        value = disk_map.pop(0)
        if free_space:
            spaces.append(Block(None, position, value))
            free_space = False
        else:
            blocks.append(Block(file_id, position, value))
            file_id += 1
            free_space = True
        position += value
    return blocks, spaces


def main():
    disk_map = get_input('input.txt')
    blocks, spaces = generate(disk_map)
    for ii, block in enumerate(reversed(blocks)):
        if ii % 100 == 0:
            print(ii, len(blocks))
        new_space = None
        blank_space = None
        for space in spaces:
            if space.position >= block.position:
                break
            if space.could_fit(block):
                new_space = Block(None, block.position, block.size)
                block.position = space.position
                space.size -= block.size
                space.position += block.size
                if space.size == 0:
                    blank_space = space
                break
        if blank_space:
            spaces.remove(blank_space)
        if new_space:
            spaces.append(new_space)
            spaces = sorted(spaces, key=lambda s: s.position)
            # all_items = sorted(blocks + spaces, key=lambda b: b.position)
            # print(''.join(block.to_str() for block in all_items))
    print(sum([block.checksum for block in blocks]))
    # print(spaces)

    # end = None
    # while None in disk_map:
    #     # print(''.join((str(value) if value is not None else '.') for value in disk_map))
    #     index = disk_map.index(None)
    #     end = disk_map.pop()
    #     print(index, len(disk_map))
    #     if index >= len(disk_map):
    #         break
    #     disk_map[index] = end
    #     while disk_map[-1] is None:
    #         disk_map.pop()
    # print(''.join((str(value) if value is not None else '.') for value in disk_map))
    # print(sum([ii*value for ii, value in enumerate(disk_map)]))
    # print(line)

main()
