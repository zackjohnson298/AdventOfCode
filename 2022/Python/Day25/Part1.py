
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def snafu_to_number_list(snafu):
    number = []
    for char in snafu:
        if char.isdigit():
            number.append(int(char))
        elif char == '-':
            number.append(-1)
        elif char == '=':
            number.append(-2)
    return number


def snafu_to_base_10(snafu):
    number_list = snafu_to_number_list(snafu)
    total = 0
    for ii, value in enumerate(reversed(number_list)):
        total += value * 5 ** ii
    return total


def base_10_to_snafu(number):
    output = ''
    while True:
        remainder = number % 5
        if remainder == 0:
            output = '0' + output
            number //= 5
        if remainder == 1:
            output = '1' + output
            # number -= 1
            number //= 5
        if remainder == 2:
            output = '2' + output
            # number -= 2
            number //= 5
        if remainder == 3:
            output = '=' + output
            number += 2
            number //= 5
        if remainder == 4:
            output = '-' + output
            number += 1
            number //= 5
        if number == 0:
            return output


def main():
    snafu_numbers = get_input('input.txt')
    total = sum([snafu_to_base_10(snafu) for snafu in snafu_numbers])
    print(total)
    print(base_10_to_snafu(total))

main()
