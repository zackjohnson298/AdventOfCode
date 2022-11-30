
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def find_error(line, opening_chars, closing_chars):
    open_chunks = []
    error = None
    for ii, char in enumerate(line):
        if char in opening_chars:
            open_chunks.append(char)
        elif char in closing_chars:
            last_open_char = open_chunks.pop()
            correct_closing_char = closing_chars[opening_chars.find(last_open_char)]
            if char != correct_closing_char:
                error = [correct_closing_char, char]
                # error = f'Error at {ii}: expected {correct_closing_char}, found {char}'
                break
    return error


def main():
    lines = get_input('input.txt')
    opening_chars = '[{(<'
    closing_chars = ']})>'
    penalty_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    total = 0
    for line in lines:
        error = find_error(line, opening_chars, closing_chars)
        if error is not None:
            total += penalty_map[error[1]]
    print(total)


main()
