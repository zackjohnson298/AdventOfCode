
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def find_abas(string):
    abas = []
    babs = []
    for ii in range(len(string)-3+1):
        if string[ii] == string[ii+2] and string[ii] != string[ii+1]:
            abas.append(string[ii:ii+3])
            babs.append(f'{string[ii+1]}{string[ii]}{string[ii+1]}')
    return abas, babs


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


def supports_SSL(code):
    inside_strings, outside_strings = split_code(code)
    for inside_string in inside_strings:
        abas, babs = find_abas(inside_string)
        for bab in babs:
            for outside_string in outside_strings:
                if bab in outside_string:
                    return True
    return False


def main():
    codes = get_input('input.txt')
    count = 0
    for code in codes:
        # print(code, supports_SSL(code))
        if supports_SSL(code):
            count += 1
    print(count)


main()
