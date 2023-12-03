

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def get_calibration_value(line: str) -> int:
    a = None
    b = None
    options = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]
    a_positions = [float('inf') for number in options]
    b_positions = [-float('inf') for number in options]
    for number, word in enumerate(options):
        if str(number) in line:
            a_position = line.index(str(number))
            b_position = line.rindex(str(number))
            if a_position < a_positions[number]:
                a_positions[number] = a_position
            if b_position > b_positions[number]:
                b_positions[number] = b_position
        if word in line:
            a_position = line.index(word)
            b_position = line.rindex(word)
            if a_position < a_positions[number]:
                a_positions[number] = a_position
            if b_position > b_positions[number]:
                b_positions[number] = b_position
    min_a_position = min(a_positions)
    max_b_position = max(b_positions)
    a = a_positions.index(min_a_position)
    b = b_positions.index(max_b_position)
    return 10*a + b


def main():
    lines = get_input('input.txt')
    total = 0
    for line in lines:
        value = get_calibration_value(line)
        total += value
        print(value, line)
    print(total)


main()
