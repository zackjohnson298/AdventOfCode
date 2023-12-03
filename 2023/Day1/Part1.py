

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def get_calibration_value(line: str) -> int:
    a = None
    b = None
    for char in line:
        if char.isdigit():
            a = int(char)
            break
    else:
        raise Exception(f'Could not find value A: {line}')
    for char in reversed(line):
        if char.isdigit():
            b = int(char)
            break
    else:
        raise Exception(f'Could not find value B: {line}')
    return 10*a + b


def main():
    lines = get_input('input.txt')
    values = [get_calibration_value(line) for line in lines]
    print(sum(values))


main()
