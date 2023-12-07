from typing import List, Tuple, Dict


def get_input(filename) -> Tuple[List[int], List[int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    times = [int(value) for value in lines[0].split(':')[1].split()]
    records = [int(value) for value in lines[1].split(':')[1].split()]
    return times, records


def main():
    times, records = get_input('input.txt')
    output = 1
    for max_time, record in zip(times, records):
        total = 0
        for ii in range(max_time+1):
            speed = ii
            time_remaining = max_time - ii
            distance = speed * time_remaining
            if distance > record:
                total += 1
        print(max_time, total)
        output *= total
    print(output)


main()
