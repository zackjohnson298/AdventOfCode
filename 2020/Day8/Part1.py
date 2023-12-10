from typing import List, Optional, Tuple


class Computer:
    def __init__(self, instructions: List[Tuple[str, int]]):
        self.accumulator = 0
        self.pointer = 0
        self.pointers = []
        self.instructions = instructions

    def update_pointer(self, value=1):
        self.pointers.append(self.pointer)
        self.pointer += value

    def execute(self, instruction: Tuple[str, int]):
        operation, value = instruction
        if operation == 'nop':
            self.update_pointer()
        elif operation == 'acc':
            self.accumulator += value
            self.update_pointer()
        elif operation == 'jmp':
            self.update_pointer(value)
        else:
            raise Exception(f'Unhandled Operation: {operation}')

    def run_until_loop(self):
        while self.pointer not in self.pointers:
            self.execute(self.instructions[self.pointer])


def get_input(filename) -> List[Tuple[str, int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    instructions = []
    for line in lines:
        operation, value_str = line.split()
        instructions.append((operation, int(value_str)))
    return instructions


def main():
    instructions = get_input('input.txt')
    comp = Computer(instructions)
    comp.run_until_loop()
    print(comp.accumulator)


main()
