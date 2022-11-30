import numpy as np


class BingoBoard:
    def __init__(self, board_arr: list):
        self.board = np.array(board_arr)
        self.rows, self.cols = self.board.shape
        self.state = np.zeros(self.board.shape)
        self.score = 0

    def play(self, number):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r, c] == number:
                    self.state[r, c] = 1
        self.update_score(number)
        return self.check()

    def check(self):
        return self.rows in sum(self.state) or self.cols in sum(self.state.T)

    def update_score(self, number):
        self.score = int(number * (sum(sum(self.board)) - sum(sum(self.board * self.state))))


