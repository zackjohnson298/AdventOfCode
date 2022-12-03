

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    outcomes = []
    their_moves = []
    for line in lines:
        them, you = line.split()
        outcomes.append(you)
        their_moves.append(them)
    return their_moves, outcomes


def evaluate(their_move, desired_outcome):
    points = {
        'A': 1,     # Rock
        'B': 2,     # Paper
        'C': 3      # Scissors
    }
    possibilities = {
        'A': {
            'X': 'C',       # Loss
            'Y': 'A',       # Draw
            'Z': 'B'        # Win
        },
        'B': {
            'X': 'A',
            'Y': 'B',
            'Z': 'C'
        },
        'C': {
            'X': 'B',
            'Y': 'C',
            'Z': 'A'
        }
    }
    your_move = possibilities[their_move][desired_outcome]
    score = points[your_move]
    if desired_outcome == 'Z':      # Win
        score += 6
    elif desired_outcome == 'Y':    # Draw
        score += 3
    return score


if __name__ == '__main__':
    their_moves, outcomes = get_input('input.txt')
    total = 0
    for their_move, desired_outcome in zip(their_moves, outcomes):
        score = evaluate(their_move, desired_outcome)
        # print(their_move, desired_outcome, score)
        total += score
    print()
    print(total)
