from rook import Rook
from queen import Queen
from pawn import Pawn
from knight import Knight
from king import King
from bishop import Bishop
from field import Field


class InvalidMoveException(Exception):
    pass


class Board:
    def __init__(self):
        first_row = [Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()]
        self.board = [[Field(piece), Field(Pawn()), *[Field() for _ in range(6)]] for piece in first_row]

        # self.board = [
        #     [Field(Rook()),Field(Pawn()),*[Field() for _ in range(6)]],
        #     [Field(Knight()),Field(Pawn()),*[Field() for _ in range(6)]],
        #     [Field(Bishop()),Field(Pawn()),*[Field() for _ in range(6)]],
        #     [Field(Queen()),Field(Pawn()),*[Field() for _ in range(6)]],
        #     [Field(King()),Field(Pawn()),*[Field() for _ in range(6)]],
        #     [Field(Bishop()),Field(Pawn()),*[Field() for _ in range(6)]],
        #     [Field(Knight()),Field(Pawn()),*[Field() for _ in range(6)]],
        #     [Field(Rook()),Field(Pawn()),*[Field() for _ in range(6)]],
        # ]

    def print_board(self):
        for i in range(7, -1, -1):
            print(i + 1, end=' ')
            for j in range(8):
                print(self.board[j][i], end=' ')
            print()
        print("   ", end='')
        for i in range(8):
            print(chr(i + 65), end="    ")
        print()

    def is_valid_move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        piece = self.board[x1][y1].piece
        if not piece:
            return False
        if self.board[x2][y2].piece:
            return False

        list_of_moves = piece.get_moves(x1, y1)
        if (x2, y2) not in list_of_moves:
            return False
        moves_between = piece.get_moves_between(x1, y1, x2, y2)
        for i, j in moves_between:
            if self.board[i][j].piece:
                return False
        return True

    def make_move(self, x1: int, y1: int, x2: int, y2: int):
        if self.is_valid_move(x1, y1, x2, y2):
            self.board[x2][y2].piece = self.board[x1][y1].piece
            self.board[x1][y1].piece = None
        else:
            raise InvalidMoveException()


board = Board()
board.print_board()
assert board.is_valid_move(1, 1, 1, 2)
assert not board.is_valid_move(0, 0, 0, 2)
assert not board.is_valid_move(0, 0, 1, 6)

try:
    board.make_move(1, 1, 1, 2)
except InvalidMoveException:
    print("Invalid move")
board.print_board()
