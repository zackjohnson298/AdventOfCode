from typing import List, Tuple, Dict, Optional, Set, Union


class Rule:
    def __init__(self, line: str):
        assert line[1] in ('>', '<')
        self.category = line[0]
        self.operation = line[1]
        value_str, self.destination = line[2:].split(':')
        self.threshold = int(value_str)

    def evaluate(self, part: Dict[str, int]) -> Tuple[Optional[str], Optional[bool]]:
        # Returns Destination, pass/fail
        value = part[self.category]
        if self.operation == '>':
            if value > self.threshold:
                return self.destination, True
            return None, False
        if value < self.threshold:
            return self.destination, True
        return None, False


def get_input(filename) -> Tuple[Dict[str, List[Union[Rule, str]]], List[Dict[str, int]]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    rules = {}
    while True:
        line = lines.pop(0)
        if line == '':
            break
        name, rules_str = line.split('{')
        rules_str = rules_str.replace('}', '')
        rule_strings = rules_str.split(',')
        rules[name] = [Rule(rule_str) for rule_str in rule_strings[:-1]] + [rule_strings[-1]]
    parts = []
    for line in lines:
        line = line[1:-1]
        sub_strings = line.split(',')
        part = {}
        for sub_string in sub_strings:
            name, value_str = sub_string.split('=')
            part[name] = int(value_str)
        parts.append(part)
    return rules, parts


def evaluate(workflows: Dict[str, List[Union[Rule, str]]], part: Dict[str, int]) -> bool:
    workflow_id = 'in'
    while True:
        workflow = workflows[workflow_id]
        for rule in workflow[:-1]:
            destination, passed = rule.evaluate(part)
            if passed:
                if destination in 'AR':
                    return destination == 'A'
                workflow_id = destination
                break
        else:
            destination = workflow[-1]
            if destination in 'AR':
                return destination == 'A'
            workflow_id = destination


def main():
    workflows, parts = get_input('input.txt')
    total = 0
    for part in parts:
        if evaluate(workflows, part):
            total += sum(part.values())
    print(total)


main()


#  Flood Fil Method

# def neighbors(pos: Tuple[int, int], width: int, height: int) -> List[Tuple[int, int]]:
#     output = []
#     r, c = pos
#     for nr in [r - 1, r, r + 1]:
#         for nc in [c - 1, c, c + 1]:
#             if (nr, nc) != pos and 0 <= nr < height and 0 <= nc < width:
#                 output.append((nr, nc))
#     return output

# def main():
#     instructions = get_input('input.txt')
#     directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
#     points = [(0, 0)]
#     for direction, value, color in instructions:
#         r, c = points[-1]
#         dr, dc = directions[direction]
#         new_points = [(r + ii*dr, c + ii*dc) for ii in range(1, value+1)]
#         points.extend(new_points)
#     min_r = min([point[0] for point in points])
#     min_c = min([point[1] for point in points])
#     for ii in range(len(points)):
#         point = points[ii]
#         point = (point[0] - (min_r - 2), point[1] - (min_c - 2))
#         points[ii] = point
#
#     height = max([point[0] for point in points]) + 2
#     width = max([point[1] for point in points]) + 2
#     visited_grid = [[False for _ in range(width)] for _ in range(height)]
#
#     iterations = 0
#     queue = [(0, 0)]
#     while queue:
#         if iterations % 10 == 0:
#             print(f'Queue: {len(queue)},\tIter: {iterations}')
#         iterations += 1
#         r, c = queue.pop(0)
#         visited_grid[r][c] = True
#         for neighbor in neighbors((r, c), width, height):
#             nr, nc = neighbor
#             if not visited_grid[nr][nc] and neighbor not in points + queue:
#                 queue.append(neighbor)
#
#     for r in range(height):
#         line = ''
#         for c in range(width):
#             line = line + ('#' if (r, c) in points else 'o' if visited_grid[r][c] else '.')
#         print(line)
#
#     print('Counting enclosed positions')
#     print(sum([sum([not value for value in row]) for row in visited_grid]))
