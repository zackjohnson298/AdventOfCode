from typing import List, Tuple, Dict, Optional


def get_input(filename) -> List[str]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines[0].split(',')


def hash_str(value: str) -> int:
    current = 0
    for char in value:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def main():
    codes = get_input('input.txt')
    boxes: Dict[int, Dict[str, int]] = {box_num: {} for box_num in range(256)}
    for code in codes:
        assert ('=' in code) or ('-' in code)
        if '-' in code:
            label = code.strip('-')
            label_hash = hash_str(label)
            box = boxes[label_hash]
            if label in box:
                box.pop(label)
        else:
            label, length_str = code.split('=')
            focal_length = int(length_str)
            label_hash = hash_str(label)
            box = boxes[label_hash]
            box[label] = focal_length
        # print(code)
        # for box_num, box in boxes.items():
        #     if box:
        #         print(f'Box {box_num} | {box}')
        # print('-----------------')
        # print()
    total = 0
    for box_num, box in enumerate(boxes.values(), start=1):
        for slot, focal_length in enumerate(box.values(), start=1):
            total += box_num * slot * focal_length
    print(total)


main()
