from typing import *
import json


def get_input(filename: str) -> dict:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = {'/': {}}
    filepath = []
    line = lines.pop(0)
    while True:
        if '$ cd' in line:
            dest = line.split()[-1]
            if dest == '/':
                filepath = ['/']
            elif dest == '..':
                filepath.pop()
            else:
                filepath.append(dest)
        elif '$ ls' in line:
            pass
        else:
            size, name = line.split()
            if size == 'dir':
                size = {}
            else:
                size = int(size)
            current = output
            for directory in filepath:
                current = current[directory]
            current[name] = size
        if lines:
            line = lines.pop(0)
        else:
            break
    return output


def process_sizes(file_tree: dict, filepath: Optional[List[str]] = None) -> Dict[Tuple[str], int]:
    if not filepath:
        filepath = ['/']
    current_size = 0
    current_dir = filepath[-1]
    sizes = {}
    directory = file_tree[current_dir]
    for filename, value in directory.items():
        if isinstance(value, int):
            # print(value)
            current_size += value
        else:
            new_filepath = filepath + [filename]
            new_sizes = process_sizes(directory, new_filepath)
            sizes.update(new_sizes)
            current_size += new_sizes[tuple(new_filepath)]
    sizes[tuple(filepath)] = current_size
    return sizes


def main():
    structure = get_input('input.txt')
    # print(json.dumps(structure, indent=4))
    sizes = process_sizes(structure)
    total_space = 70000000
    required_unused = 30000000
    current_unused = total_space - sizes[('/',)]
    deletion_size = required_unused - current_unused
    # print(deletion_size)
    sorted_sizes = sorted(sizes.items(), key=lambda item: item[1])
    for filepath, size in sorted_sizes:
        if size > deletion_size:
            print(filepath[-1], size)
            break
    # print(sum([value for value in sizes.values() if value <= 100000]))


main()
