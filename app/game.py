class Game:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "x"
        self.winner = None
        self.win_row = None

    def calculate_turn(self):
        x_count = sum(row.count("x") for row in self.board)
        o_count = sum(row.count("o") for row in self.board)
        self.turn = "x" if x_count <= o_count else "o"

    @classmethod
    def from_dict(cls, board):
        game = cls()
        game.board = board
        game.calculate_turn()
        return game

    def make_move(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.turn
            self.calculate_turn()
        self.check_winner()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                self.winner = self.board[i][0]
                self.win_row = i
                self.draw_line = 10, 33/2 + i * 33, 90, 33/2 + i * 33
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                self.winner = self.board[0][i]
                self.win_row = i + 3
                self.draw_line = 33/2 + i * 33, 10, 33/2 + i * 33, 90
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.winner = self.board[0][0]
            self.win_row = 6
            self.draw_line = 10, 10, 90, 90
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.winner = self.board[0][2]
            self.win_row = 7
            self.draw_line = 90, 10, 10, 90
            return
        if all(cell is not None for row in self.board for cell in row):
            self.winner = "Tie"
            return
        self.winner = None

    def state(self):
        message = ""
        if self.winner:
            message = f"{self.winner} wins!" if self.winner != "Tie" else "It's a tie!"

        return {
            "board": self.board,
            "turn": self.turn,
            "winner": self.winner,
            "win_row": self.win_row,
            "message": message
        }
