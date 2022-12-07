import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    current_path = []
    sizes = {('/',): 0}
    for line in lines:
        if line[0] == '$':
            if line[2:4] == 'cd':
                destination = line.split()[-1]
                if destination == '..':
                    current_path.pop()
                elif destination == '/':
                    current_path = ['/']
                else:
                    current_path.append(destination)
        else:
            size_or_type, name = line.split()
            if size_or_type == 'dir':
                new_path = current_path + [name]
                sizes[tuple(new_path)] = 0
            else:
                for ii in range(len(current_path)):
                    path = current_path[:ii+1]
                    sizes[tuple(path)] += int(size_or_type)
    return sizes


def main():
    sizes = get_input('input.txt')
    for key, value in sizes.items():
        print(key, value)
    total = 0
    for size in sizes.values():
        if size <= 100000:
            total += size
    print(total)


main()
