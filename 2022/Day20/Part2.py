
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


def mix(numbers: [int], codes) -> [int]:
    for number_id, value in enumerate(numbers):
        # if value == 0:
        #     continue
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
    return numbers, codes


def main():
    numbers = get_input('input.txt')
    key = 811589153
    numbers = [number*key for number in numbers]
    codes = [{'id': ii, 'value': v} for ii, v in enumerate(numbers)]
    new_numbers = numbers
    for ii in range(10):
        print(ii+1, '/', 10)
        new_numbers, codes = mix(numbers, codes)

    index = new_numbers.index(0)
    a = new_numbers[(index + 1000) % len(numbers)]
    b = new_numbers[(index + 2000) % len(numbers)]
    c = new_numbers[(index + 3000) % len(numbers)]
    print()
    print(a, b, c)
    print()
    print(a + b + c)


main()
