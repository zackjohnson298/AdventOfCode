import json
from typing import List, Optional, Tuple, Dict


def get_input(filename) -> List[Dict[str, str]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    passports = []
    passport = {}
    for line in lines:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            for substr in line.split():
                key, value = substr.split(':')
                passport[key] = value
    if passport:
        passports.append(passport)
    return passports


def is_valid(passport: Dict[str, str]) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport:
            return False
    return True


def main():
    passports = get_input('input.txt')
    count = 0
    for passport in passports:
        if is_valid(passport):
            count += 1
    print(count)


main()
