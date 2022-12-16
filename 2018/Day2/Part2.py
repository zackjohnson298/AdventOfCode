
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines


def main():
    codes = get_input('input.txt')
    for ii, code_a in enumerate(codes[:-1]):
        for code_b in codes[ii+1:]:
            diff_count = [a != b for a, b in zip(code_a, code_b)]
            if sum(diff_count) == 1:
                same = ''.join(a for a, b in zip(code_a, code_b) if a == b)
                print(same)
                return
    print('None found')

main()
