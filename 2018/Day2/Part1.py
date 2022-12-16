
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def main():
    codes = get_input('input.txt')
    two_count = []
    three_count = []
    for code in codes:
        for letter in set(code):
            if code.count(letter) == 2 and code not in two_count:
                two_count.append(code)
            elif code.count(letter) == 3 and code not in three_count:
                three_count.append(code)
    print(len(two_count)*len(three_count))

main()
