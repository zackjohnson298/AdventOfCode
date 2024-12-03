from typing import *


def get_input(filename: str) -> List[str]:
    with open(filename) as file:
        lines = file.read().splitlines()
        return lines


def main():
    lines = get_input('input.txt')
    total = 0
    do = True
    for line in lines:
        while line:
            found = False
            if line[:4] == 'do()':
                do = True
                line = line[4:]
                continue
            elif line[:7] == "don't()":
                do = False
                line = line[7:]
                continue
            if line[:4] == 'mul(':
                comma_index = line.find(',')
                if comma_index > 4:
                    closing_index = line.find(')')
                    if closing_index > comma_index:
                        a = line[4:comma_index]
                        b = line[comma_index+1:closing_index]
                        if a.isdigit() and b.isdigit():
                            if do:
                                total += int(a) * int(b)
                            print(a, b, do)
                            line = line[closing_index:]
                            found = True
            if not found:
                line = line[1:]
    print(total)





main()
