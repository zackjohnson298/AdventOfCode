

'''
INCOMPLETE
'''


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return int(lines[0]), [int(value) if value.isdigit() else 1 for value in lines[1].split(',')]

def gcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if (~a & 1) == 1:
        # b is odd
        if (b & 1) == 1:
            return gcd(a >> 1, b)
        else:
            # both a and b are even
            return gcd(a >> 1, b >> 1) << 1
    # a is odd, b is even
    if (~b & 1) == 1:
        return gcd(a, b >> 1)
    # reduce larger number
    if a > b:
        return gcd((a - b) >> 1, b)
    return gcd((b - a) >> 1, a)


def find_sync(a, b, offset):
    _, remainder = divmod(-offset, gcd(a, b))
    if remainder:
        return None
    N = 1

    while (N * (b - a) + offset) % a != 0:
        N += 1

    M = int((offset + N * b) / a)
    return M * a


def main():
    earliest, codes = get_input('test_input.txt')
    # print(product(codes))
    # lcm = product(codes)
    # timestamp = lcm
    # done = False
    # while not done:
    #     done = True
    #     for ii, code in enumerate(codes):
    #         if code != 1:
    #             if (timestamp + ii) % code != 0:
    #                 done = False
    #                 break

    # mods = [code - earliest % code for code in codes]
    # best = codes[mods.index(min(mods))]
    # print(best * min(mods))
    # value = codes[]
    # print(codes)


main()
