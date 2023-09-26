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
    total = 0
    used_space = sizes[('/',)]
    total_space = 70000000
    desired_space = 30000000
    unused_space = total_space - used_space
    space_to_free = desired_space - unused_space
    for size in sorted(sizes.values()):
        if size > space_to_free:
            print(size)
            break
    # print(total)


main()
