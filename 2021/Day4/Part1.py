from BingoBoard import BingoBoard


def get_input():
    with open('input.txt') as file:
        lines = file.read().splitlines()
    numbers = [int(value) for value in lines.pop(0).split(',')]
    boards = []
    lines.pop(0)     # Get rid of extra newline between numbers and first board

    board = []
    for line in lines:
        if line:
            row = [int(value) for value in line.split()]
            board.append(row)
        else:
            boards.append(BingoBoard(board.copy()))
            board = []
    boards.append(BingoBoard(board.copy()))
    return numbers, boards


def main():
    numbers, boards = get_input()
    for number in numbers:
        for board in boards:
            win = board.play(number)
            if win:
                print(number, board.score)
                return


main()
