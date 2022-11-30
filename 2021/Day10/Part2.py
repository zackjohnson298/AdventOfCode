
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
                break
    return error


def complete_line(line, opening_chars, closing_chars):
    open_chunks = []
    error = None
    output = ''
    for ii, char in enumerate(line):
        if char in opening_chars:
            open_chunks.append(char)
        elif char in closing_chars:
            last_open_char = open_chunks.pop()
            correct_closing_char = closing_chars[opening_chars.find(last_open_char)]
            if char != correct_closing_char:
                error = f'Error at ii: expected {correct_closing_char}, found {char}'
                break
    if error is None:
        for opening_char in reversed(open_chunks):
            output = output + closing_chars[opening_chars.find(opening_char)]
    return output, error


def main():
    lines = get_input('input.txt')
    opening_chars = '[{(<'
    closing_chars = ']})>'
    point_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []
    for line in lines:
        error = find_error(line, opening_chars, closing_chars)
        if error is None:
            output, error = complete_line(line, opening_chars, closing_chars)
            if error is None:
                score = 0
                for char in output:
                    score *= 5
                    score += point_map[char]
                scores.append(score)
            else:
                print(line, ':', error)
                break
    print(sorted(scores)[int(len(scores) / 2)])


main()
