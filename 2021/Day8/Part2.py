import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    data = []
    for line in lines:
        inputs, outputs = line.split('|')
        data.append([inputs.split(), outputs.split()])
    return data


def find_display(samples):
    samples = samples.copy()
    display = {}
    display[1] = [sample for sample in samples if len(sample) == 2][0]
    display[4] = [sample for sample in samples if len(sample) == 4][0]
    display[7] = [sample for sample in samples if len(sample) == 3][0]
    display[8] = [sample for sample in samples if len(sample) == 7][0]
    display[9] = [sample for sample in samples if len(sample) == 6 and len(set(sample) - set(display[4])) == 2 and sample not in display.values()][0]
    display[6] = [sample for sample in samples if len(sample) == 6 and len(set(display[7]) - set(sample)) == 1 and sample not in display.values()][0]
    display[5] = [sample for sample in samples if len(sample) == 5 and len(set(sample) - set(display[6])) == 0 and sample not in display.values()][0]
    display[3] = [sample for sample in samples if len(sample) == 5 and len(set(sample) - set(display[9])) == 0 and sample not in display.values()][0]
    display[2] = [sample for sample in samples if len(sample) == 5 and sample not in display.values()][0]
    display[0] = [sample for sample in samples if len(sample) == 6 and sample not in display.values()][0]
    return display


def decode(inputs, outputs):
    display = find_display(inputs)
    output_value = ''
    for output in outputs:
        for key, value in display.items():
            if set(output) == set(value):
                output_value = output_value + str(key)
                break
    return int(output_value)


def main():
    data = get_input('input.txt')
    total = 0
    for inputs, outputs in data:
        total += decode(inputs, outputs)
    print(total)


main()
