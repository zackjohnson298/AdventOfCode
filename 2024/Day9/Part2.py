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


def generate(disk_map: List[int]) -> Tuple[Dict[int, Block], Dict[int, Block]]:
    file_id = 0
    blocks = {}
    spaces = {}
    free_space = False
    position = 0
    disk_map = [value for value in disk_map]
    while disk_map:
        value = disk_map.pop(0)
        if free_space:
            spaces[position] = Block(None, position, value)
            free_space = False
        else:
            blocks[position] = Block(file_id, position, value)
            file_id += 1
            free_space = True
        position += value
    return blocks, spaces


def main():
    disk_map = get_input('input.txt')
    blocks, spaces = generate(disk_map)
    space_positions = list(spaces)
    for ii, block in enumerate(reversed(blocks.values())):
        if ii % 1000 == 0:
            print(ii, len(blocks))
        for space_pos in space_positions:
            if space_pos >= block.position:
                break
            space = spaces[space_pos]
            if space.could_fit(block):
                new_space = Block(None, block.position, block.size)
                spaces[new_space.position] = new_space
                block.position = space.position
                space.size -= block.size
                space.position += block.size
                spaces.pop(space_pos)
                if space.size:
                    spaces[space.position] = space
                space_positions = sorted(spaces)
                break
            # all_items = sorted(blocks + spaces, key=lambda b: b.position)
            # print(''.join(block.to_str() for block in all_items))
    print(sum([block.checksum for block in blocks.values()]))


main()
