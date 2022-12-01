

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    current = []
    for line in lines:
        if len(line) == 0:
            output.append(current)
            current = []
        else:
            current.append(int(line))
    output.append(current)
    return output


def main():
    data = get_input('input.txt')
    print(max([sum(group) for group in data]))
    

main()
