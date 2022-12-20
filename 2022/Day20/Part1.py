
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(value) for value in lines]


def sign(number):
    return 1 if number > 0 else -1 if number < 0 else None


def find_code(code_id, codes):
    for code in codes:
        if code['id'] == code_id:
            return code
    return None


def mix(numbers: [int]) -> [int]:
    codes = [{'id': ii, 'value': v} for ii, v in enumerate(numbers)]
    for number_id, value in enumerate(numbers):
        code = find_code(number_id, codes)
        if code is None:
            print('Could not find code')
            return
        index = codes.index(code)
        new_index = (index + value) % (len(codes) - 1)
        _ = codes[new_index]
        codes.pop(index)
        codes.insert(new_index, code)
    numbers = [code['value'] for code in codes]
    return numbers


def main():
    numbers = get_input('input.txt')
    numbers = mix(numbers)
    index = numbers.index(0)
    a = numbers[(index + 1000) % len(numbers)]
    b = numbers[(index + 2000) % len(numbers)]
    c = numbers[(index + 3000) % len(numbers)]
    print(a, b, c)
    print(a + b + c)


main()
