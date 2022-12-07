import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    tree = {'/': {}}
    current_path = ['/']
    state = 'adding files'
    for line in lines[2:]:
        if '$' in line:
            if ' cd ' in line:      # This is suspicious. If I check for ls instead it no longer works (key error at vmvpf)
                if '..' in line:
                    current_path.pop()
                else:
                    current_path.append(line.split()[-1])
        else:
            cwd = tree
            for directory in current_path:
                cwd = cwd[directory]
            type_or_size, name = line.split()
            if type_or_size == 'dir' and name not in cwd:
                cwd[name] = {}
            else:
                cwd[name] = int(type_or_size)

    return tree


def get_size(tree, sizes):
    total = 0
    for name, value in tree.items():
        if type(value) == int:
            total += value
        else:
            new_value = get_size(value, sizes)
            total += new_value
            if name in sizes:
                sizes[name] += new_value
            else:
                sizes[name] = new_value
    return total


def main():
    tree = get_input('input.txt')
    print(json.dumps(tree, indent=4))
    sizes = {'/': 0}
    get_size(tree, sizes)
    print(json.dumps(sizes, indent=4))
    total = 0
    for key, value in sizes.items():
        if value <= 100000:
            total += value
    print(total)

main()
