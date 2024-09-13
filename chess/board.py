from rook import Rook
from queen import Queen
from pawn import Pawn
from knight import Knight
from king import King
from bishop import Bishop
from field import Field

class Board:
    def __init__(self):
        first_row = [Field(Rook()),
                       Field(Knight()),
                       Field(Bishop()),
                       Field(Queen()),
                       Field(King()),
                       Field(Bishop()),
                       Field(Knight()),
                       Field(Rook())]
        self.board = [
                    first_row,
                    [Field(Pawn()) for _ in range(8)],
                    *[[Field() for _ in range(8)] for _ in range(6)]
                    ]


    def print_board(self):
        for i in range(7, -1, -1):
            print(i + 1, end=' ')
            for j in range(7, -1, -1):
                print(self.board[i][j], end=" ")
            print()
        print("   " , end='')
        for i in range(8):
                print(chr(i + 65), end="    ")

    def check_field(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        if self.board[x1][y1].piece is not None:
            return False
        if self.board[x2][y2].piece:
            return False


board = Board()
board.print_board()





