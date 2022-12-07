import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    tree = {'/': {}}
    current_path = ['/']
    for line in lines:
        if '$' in line:
            if ' cd ' in line:      # This is suspicious. If I check for ls instead it no longer works (key error at vmvpf)
                if '..' in line:
                    current_path.pop()
                elif '/' in line:
                    current_path = ['/']
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


def get_size(tree, sizes, current_path):
    total = 0
    for name, value in tree.items():
        if type(value) == int:
            total += value
        else:
            new_path = current_path + [name]
            new_value = get_size(value, sizes, new_path)
            total += new_value
            key = tuple(new_path)
            if key in sizes:
                sizes[key] += new_value
            else:
                sizes[key] = new_value
    return total


def main():
    tree = get_input('input.txt')
    print(json.dumps(tree, indent=4))
    sizes = {('/',): 0}
    current_path = ['/']
    get_size(tree, sizes, current_path)
    # print(json.dumps(sizes, indent=4))
    total = 0
    for key, value in sizes.items():
        if value <= 100000:
            total += value
    print(total)


main()
