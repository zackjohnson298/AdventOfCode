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
        value = passport.get(field)
        if value is None:
            return False
        elif field == 'byr' and not (value.isdigit() and 1920 <= int(value) <= 2002):
            return False
        elif field == 'iyr' and not (value.isdigit() and 2010 <= int(value) <= 2020):
            return False
        elif field == 'eyr' and not (value.isdigit() and 2020 <= int(value) <= 2030):
            return False
        elif field == 'hgt':
            if value[-2:] not in ('in', 'cm') or not value[:-2].isdigit():
                return False
            height = int(value[:-2])
            if (value[-2:] == 'cm' and not (150 <= height <= 193)) or (value[-2:] == 'in' and not (59 <= height <= 76)):
                return False
        elif field == 'hcl' and not (value[0] == '#' and len(value) == 7 and all([c in '0123456789abcdef' for c in value[1:]])):
            return False
        elif field == 'ecl' and not (value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')):
            return False
        elif field == 'pid' and not (len(value) == 9 and value.isdigit()):
            return False
    return True


def main():
    passports = get_input('input.txt')
    count = 0
    for passport in passports:
        if is_valid(passport):
            count += 1
            is_valid(passport)
        else:
            is_valid(passport)
    print(count)


main()
