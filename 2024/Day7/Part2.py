from typing import *


def get_input(filename: str) -> List[Tuple[int, List[int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    output = []
    for line in lines:
        a, b = line.split(': ')
        numbers = b.split()
        output.append((int(a), [int(value) for value in numbers]))
    return output


def num_to_3_bit(n: int) -> str:
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 3) + result
        n //= 3
    return result


def execute(numbers: List[int], operators: int) -> int:
    nums = [value for value in numbers]
    output = nums.pop(0)
    op_str = num_to_3_bit(operators)
    op_str = '0'*(len(numbers) - len(op_str) - 1) + op_str
    for index, op in enumerate(op_str):
        if op == '0':
            output += nums[index]
        elif op == '1':
            output *= nums[index]
        else:
            output = int(str(output) + str(nums[index]))
    return output


def validate(line: Tuple[int, List[int]]) -> int:
    answer, numbers = line
    options = 3**(len(numbers)-1)
    count = 0
    for operators in range(options):
        if execute(numbers, operators) == answer:
            count += 1
    return count


def main():
    lines = get_input('input.txt')
    total = 0
    for ii, line in enumerate(lines):
        print(ii, len(lines))
        if validate(line):
            total += line[0]
    print(total)


main()
