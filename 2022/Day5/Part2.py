import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    stacks = {}
    instructions = []
    for line in lines:
        if '[' in line:
            stack_number = 1
            string_index = 1
            while string_index < len(line):
                if line[string_index] != ' ':
                    if stack_number in stacks:
                        stacks[stack_number].append(line[string_index])
                    else:
                        stacks[stack_number] = [line[string_index]]
                stack_number += 1
                string_index += 4
        elif 'move' in line:
            lst = line.split()
            instructions.append([int(lst[1]), int(lst[3]), int(lst[5])])
    return stacks, instructions


def main():
    stacks, instructions = get_input('input.txt')
    for number, stack_a, stack_b in instructions:
        crates_to_move = []
        for _ in range(number):
            crates_to_move.append(stacks[stack_a].pop(0))
        stacks[stack_b] = crates_to_move + stacks[stack_b]
    code = ''
    for stack in sorted(stacks):
        code = code + stacks[stack][0]
    print(code)


main()
