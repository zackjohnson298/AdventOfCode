import ast


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    pairs = []
    pair = []
    for line in lines:
        if len(line):
            pair.append(ast.literal_eval(line))
        else:
            pairs.append(pair)
            pair = []
    pairs.append(pair)
    return pairs


def debug_print(string, should_print):
    print(string) if should_print else ''


def evaluate(left_list: list, right_list: list, debug=False, depth=1):
    # Return Values:
    #   True: lists are in the correct order (left < right)
    #   False: lists are not in correct order (left > right)
    #   None: order could not be determined
    debug_print('\t' * depth + str(left_list) + ' vs. ' + str(right_list), debug)
    for ii in range(len(left_list)):
        if ii >= len(right_list):
            debug_print('\t' * (depth+1) + 'Right list ran out of items first: FALSE', debug)
            debug_print('---------------------------', debug)
            return False                # Right ran out of items first, lists are not in order
        left_value = left_list[ii]
        right_value = right_list[ii]
        if type(left_value) == int and type(right_value) == int:
            debug_print('\t' * (depth+1) + str(left_value) + ' vs. ' + str(right_value), debug)
            if left_value == right_value:
                continue
            else:
                debug_print('\t' * (depth+1) + f'Direct Integer Comparison: {left_value < right_value}', debug)
                debug_print('---------------------------', debug)
                return left_value < right_value     # In sorted pairs, left value should be less than right value
        else:
            if type(left_value) == int:
                left_value = [left_value]
            if type(right_value) == int:
                right_value = [right_value]
            result = evaluate(left_value, right_value, debug=debug, depth=depth+1)
            if result is not None:
                return result
    # Indeterminate result so far, check if left list ran out of items first
    if len(left_list) < len(right_list):
        debug_print('\t' * depth + 'Left list ran out of items first: True', debug)
        debug_print('---------------------------', debug)
        return True
    debug_print('\t' * depth + 'Could not determine order', debug)
    return None


def main():
    pairs = get_input('input.txt')
    total = 0
    for ii, (left, right) in enumerate(pairs):
        result = evaluate(left, right, debug=False)
        if result:
            total += ii + 1
    print(total)


main()
