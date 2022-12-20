import json
from random import choice


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(value) for value in lines]


def sign(number):
    return 1 if number > 0 else -1 if number < 0 else None


def construct_numbers(codes) -> [int]:
    numbers = [None] * len(codes)
    for code in codes:
        index = code['index']
        if numbers[index] is not None:
            raise ValueError('invalid code list')
        numbers[index] = code['value']
    return numbers


def main():
    numbers = get_input('input.txt')
    codes = [{'value': value, 'index': index, 'id': index} for index, value in enumerate(numbers)]
    # print(construct_numbers(codes))
    # _ = input()
    for ii, number in enumerate(numbers):
        print(ii, len(numbers))
        index = codes[ii]['index']
        moved_code_id = codes[ii]['id']
        upper_index = (number % len(codes)) + 1
        if number >= 0:
            codes[ii]['index'] = (codes[ii]['index'] + number) % len(codes)
        else:
            codes[ii]['index'] = (codes[ii]['index'] + number - 1) % len(codes)
            upper_index = ((number - 1) % len(codes)) + 1
        for jj in range(1, upper_index):
            code_index = (index + jj) % len(codes)
            code_to_move = {}
            for code in codes:
                if code['id'] == moved_code_id:
                    continue
                if code['index'] == code_index:
                    code_to_move = code
                    break
            else:
                print('Could not find code')
                return
            code_to_move['index'] -= 1
        # print()
        # print(ii+1)
        # print(construct_numbers(codes))
        # # print(json.dumps(codes, indent=4))
        # _ = input('continue: ')
    numbers = construct_numbers(codes)
    index = numbers.index(0)
    a = numbers[(index + 1000) % len(numbers)]
    b = numbers[(index + 2000) % len(numbers)]
    c = numbers[(index + 3000) % len(numbers)]
    print(a, b, c)
    print(a + b + c)










main()
