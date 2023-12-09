from typing import List, Optional, Tuple


def get_input(filename) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def get_seat_id(boarding_pass: str) -> int:
    boarding_pass = boarding_pass.replace('B', '1')
    boarding_pass = boarding_pass.replace('F', '0')
    boarding_pass = boarding_pass.replace('R', '1')
    boarding_pass = boarding_pass.replace('L', '0')
    return int(boarding_pass, 2)


def main():
    passes = get_input('input.txt')
    seat_ids = sorted([get_seat_id(boarding_pass) for boarding_pass in passes])
    for ii, _id in enumerate(seat_ids, start=seat_ids[0]):
        if ii != _id:
            print(_id - 1)
            break



main()
