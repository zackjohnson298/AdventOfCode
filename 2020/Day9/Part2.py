from typing import List, Optional, Tuple


def get_input(filename) -> List[int]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [int(value) for value in lines]


def two_sum(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    differences = {}
    for number in numbers:
        difference = target - number
        reminder = differences.get(number)
        if reminder:
            return number, reminder
        differences[difference] = number
    return None


def find_invalid_number(values: List[int], size: int) -> Optional[int]:
    for ii in range(size, len(values)):
        subset = values[ii-size:ii]
        value = values[ii]
        result = two_sum(subset, value)
        if result is None:
            return value
    return None


def find_contiguous_set(values: List[int], target: int) -> List[int]:
    for ii in range(len(values)-1):
        for jj in range(ii+1, len(values)):
            total = sum(values[ii:jj])
            if total == target:
                return values[ii:jj]
            if total > target:
                break
    return []


def main():
    values = get_input('input.txt')
    size = 25
    target = find_invalid_number(values, size)
    subset = sorted(find_contiguous_set(values, target))
    if subset:
        print(subset)
        print(subset[-1] + subset[0])
    else:
        print('Failed')

main()
