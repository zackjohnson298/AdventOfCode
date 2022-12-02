

def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    your_moves = []
    their_moves = []
    for line in lines:
        them, you = line.split()
        your_moves.append(you)
        their_moves.append(them)
    return their_moves, your_moves


def evaluate(their_move, your_move):
    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    outcome = {
        'X': {
            'win': 'C',
            'loss': 'B'
        },
        'Y': {
            'win': 'A',
            'loss': 'C'
        },
        'Z': {
            'win': 'B',
            'loss': 'A'
        }
    }
    score = points[your_move]
    if their_move == outcome[your_move]['win']:
        score += 6
    elif their_move != outcome[your_move]['loss']:
        score += 3
    return score


def main():
    their_moves, your_moves = get_input('input.txt')
    total = 0
    for their_move, your_move in zip(their_moves, your_moves):
        score = evaluate(their_move, your_move)
        print(their_move, your_move, score)
        total += score
    print()
    print(total)


main()

