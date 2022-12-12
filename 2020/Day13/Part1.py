

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return int(lines[0]), [int(value) for value in lines[1].split(',') if value.isdigit()]


def main():
    earliest, codes = get_input('input.txt')
    delta = max(codes)
    mods = [code - earliest % code for code in codes]
    best = codes[mods.index(min(mods))]
    print(best * min(mods))
    # value = codes[]
    # print(codes)


main()
