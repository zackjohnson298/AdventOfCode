

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    instructions = []
    for line in lines:
        lst = line.split()
        instruction = [lst[0], int(lst[1]) if len(lst) > 1 else None]
        instructions.append(instruction)
    return instructions


def main():
    instructions = get_input('input.txt')
    reg_x = 1
    cycle = 0
    pointer = 0
    pause = False
    new_reg_x = 0
    total = 0
    while pointer < len(instructions):
        cycle += 1
        if pause:
            pause = False
            reg_x = new_reg_x
            pointer += 1
        else:
            command, value = instructions[pointer]
            if command == 'noop':
                pointer += 1
            else:
                new_reg_x = reg_x + value
                pause = True
        if cycle+1 in [20, 60, 100, 140, 180, 220]:
            print(cycle+1, reg_x, (cycle+1)*reg_x)
            total += (cycle+1)*reg_x
    print()
    print(total)



main()
