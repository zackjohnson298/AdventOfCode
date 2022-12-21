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
        start += len(substring) # use start += 1 to find overlapping matches


def main():
    replacements, word = get_input('input.txt')
    unique_words = []

    for old, new in replacements:
        for index in find_all(word, old):
            new_word = word[:index] + new + word[index+len(old):]
            if new_word not in unique_words:
                unique_words.append(new_word)
    print(len(unique_words))


main()
