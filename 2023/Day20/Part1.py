from typing import List, Tuple, Dict, Optional, Set, Union


class Module:
    def __init__(self, name: str):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def react(self, parent_name: str, parent_state: bool) -> Optional[bool]:
        raise Exception('Cannot call "react" on base class')


class FlipFlop(Module):
    def __init__(self, *args):
        super(FlipFlop, self).__init__(*args)
        self.state = False

    def react(self, parent_name: str, parent_state: bool) -> Optional[bool]:
        if parent_state:
            return None
        self.state = not self.state
        return self.state


class Conjunction(Module):
    def __init__(self, *args):
        super(Conjunction, self).__init__(*args)
        self.memory: Dict[str, bool] = {}

    def add_input(self, name: str):
        self.memory[name] = False

    def react(self, parent_name: str, parent_state: bool):
        self.memory[parent_name] = parent_state
        return not all(self.memory.values())


class Broadcaster(Module):
    def __init__(self, *args):
        super(Broadcaster, self).__init__(*args)

    def react(self, parent_name: str, parent_state: bool) -> Optional[bool]:
        return parent_state


def get_input(filename) -> Tuple[Dict[str, Module], Dict[str, List[str]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    modules = {}
    connections = {}
    for line in lines:
        source, dest = line.split(' -> ')
        name = source[1:]
        if source == 'broadcaster':
            name = source
            module = Broadcaster(source)
        elif '%' in source:
            module = FlipFlop(source[1:])
        elif '&' in source:
            module = Conjunction(source[1:])
        else:
            raise Exception(f'Unhandled type: {source}')
        modules[name] = module
        children = dest.split(', ')
        connections[name] = children
        if type(module) == Conjunction:
            for child in children:
                module.add_input(child)
    return modules, connections


def main():
    modules, connections = get_input('test_input1.txt')
    high_count = 0
    low_count = 1
    pulsing = ['broadcaster']
    while pulsing:
        for name in pulsing:
            module =


main()
