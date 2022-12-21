import json
import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    wires = {}
    for line in lines:
        op_str, name = line.split(' -> ')
        if op_str.isdigit():
            wires[name] = {
                'name': name,
                'children': None,
                'op': None,
                'value': int(op_str)
            }
            continue
        op_list = op_str.split()
        if op_list[0] == 'NOT':
            wires[name] = {
                'name': name,
                'children': [int(op_list[1]) if op_list[1].isdigit() else op_list[1]],
                'op': 'NOT',
                'value': None
            }
            continue
        if len(op_list) == 1:
            wires[name] = {
                'name': name,
                'children': [op_list[0]],
                'op': None,
                'value': None
            }
            continue
        children = [op_list[0], op_list[2]]
        children = [int(child) if child.isdigit() else child for child in children]
        op = op_list[1]
        wires[name] = {
            'name': name,
            'children': children,
            'op': op,
            'value': None
        }
    return wires


def evaluate(values, op):
    if op is None:
        return values[0]
    if op == 'NOT':
        return np.uint16(~values[0])
    if op == 'AND':
        return np.uint16(values[0] & values[1])
    if op == 'OR':
        return np.uint16(values[0] | values[1])
    if op == 'RSHIFT':
        return np.uint16(values[0] >> values[1])
    if op == 'LSHIFT':
        return np.uint16(values[0] << values[1])
    raise TypeError(f'Unhandled Operator: {op}')


def get_value(wires, desired):
    if type(desired) == int:
        return desired
    wire = wires[desired]
    if wire['value'] is not None:
        return wire['value']
    child_values = [get_value(wires, child) for child in wire['children']]
    value = evaluate(child_values, wire['op'])
    wire['value'] = value
    return value


def main():
    wires = get_input('input.txt')
    print(get_value(wires, 'a'))


main()
