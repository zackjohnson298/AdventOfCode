
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def reverse_string(string):
    output = ''
    for char in reversed(string):
        output += char
    return output


def has_abba(string: str):
    for ii in range(len(string)-4+1):
        if string[ii: ii+2] == reverse_string(string[ii+2: ii+4]) and string[ii] != string[ii+1]:
            return True
    return False


def split_code(code):
    inside_strings = []
    outside_strings = []
    current = ''
    for char in code:
        if char == '[':
            inside_strings.append(current)
            current = ''
        elif char == ']':
            outside_strings.append(current)
            current = ''
        else:
            current = current + char
    if len(current) > 0:
        inside_strings.append(current)
    return inside_strings, outside_strings


def supports_TLS(code):
    inside_strings, outside_strings = split_code(code)
    for string in outside_strings:
        if has_abba(string):
            return False
    for string in inside_strings:
        if has_abba(string):
            return True
    return False


def main():
    codes = get_input('input.txt')
    count = 0
    for code in codes:
        if supports_TLS(code):
            count += 1
    print(count)


main()
