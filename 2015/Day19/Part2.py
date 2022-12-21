import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    word = lines.pop()
    lines.pop()     # Remove extra newline
    replacements = [tuple(line.split(' => ')) for line in lines]
    return replacements, word


def find_all(string, substring):
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1: return
        yield start
        start += len(substring)


def find_count(replacements, start, current_word, count=0, invalid_words=[]):
    # print(count, current_word)
    if start == current_word:
        return count, True
    if len(current_word) < len(start):
        return None, False
    for old, new in replacements:
        for index in find_all(current_word, new):
            prev_word = current_word[:index] + old + current_word[index + len(new):]
            if prev_word in invalid_words:
                continue
            # print(prev_word)
            new_count, count_found = find_count(replacements, start, prev_word, count=count+1)
            if count_found:
                # print(count, current_word)
                return new_count, True
            else:
                invalid_words.append(prev_word)
    # print(len(invalid_words) == len(set(invalid_words)))
    return None, False


def main():
    replacements, word = get_input('input.txt')

    count, path_found = find_count(replacements, 'e', word)
    print(path_found)
    print()
    print(count)


main()
