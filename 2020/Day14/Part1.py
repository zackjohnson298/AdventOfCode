import json
from typing import Dict, List, Tuple, Union


def get_input(filename) -> List[Tuple[str, Union[str, Tuple[int, int]]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        if 'mask = ' in line:
            output.append(('mask', line.replace('mask = ', '')))
        else:
            mem_str, val_str = line.split(' = ')
            mem_str = mem_str.replace('mem[', '')
            mem_str = mem_str.replace(']', '')
            output.append(('mem', (int(mem_str), int(val_str))))
    return output


def apply_mask(value: int, mask: str):
    output = 0
    for ii, max_bit in enumerate(reversed(mask)):
        if max_bit == 'X':
            output += (1 << ii) & value
        elif max_bit == '0':
            continue
        else:
            output += (1 << ii)
    return output


def main():
    lines = get_input('input.txt')
    memory = {}
    mask = ''
    for kind, value in lines:
        if kind == 'mask':
            mask = value
        else:
            address, val = value
            new_val = apply_mask(val, mask)
            print(val, new_val)
            memory[address] = new_val
    print(sum(memory.values()))

main()
