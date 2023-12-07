from typing import Tuple


def get_input(filename) -> Tuple[int, int]:
    with open(filename) as file:
        lines = file.read().splitlines()
    max_time = int(lines[0].split(':')[1].replace(' ', ''))
    record = int(lines[1].split(':')[1].replace(' ', ''))
    return max_time, record


def main():
    max_time, record = get_input('input.txt')
    total = 0
    for ii in range(max_time+1):
        speed = ii
        time_remaining = max_time - ii
        distance = speed * time_remaining
        if distance > record:
            total += 1
    print(total)


main()
