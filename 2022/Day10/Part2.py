

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    instructions = []
    for line in lines:
        lst = line.split()
        instruction = [lst[0], int(lst[1]) if len(lst) > 1 else None]
        instructions.append(instruction)
    return instructions


def print_sprite(pos, width):
    for ii in range(40):
        if abs(pos - ii) <= width:
            print('#', end='')
        else:
            print('.',end='')
    print()


def print_screen(screen):
    for ii, char in enumerate(screen):
        print(2*char, end='')
        if (ii+1) % 40 == 0:
            print()


def main():
    instructions = get_input('input.txt')
    reg_x = 1
    cycle = 0
    pointer = 0
    pause = False
    new_reg_x = 0
    screen = []
    while pointer < len(instructions):
        cycle += 1
        if abs((cycle-1) % 40 - reg_x) <= 1:
            screen.append('#')
        else:
            screen.append('.')
        # print(cycle, reg_x)
        # print_sprite(reg_x, 1)
        # print_sprite(cycle-1, 0)
        # print_screen(screen)
        # _ = input()
        # print()
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
    print_screen(screen)


main()
