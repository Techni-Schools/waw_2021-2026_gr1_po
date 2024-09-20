from chess.bishop import Bishop
from chess.rook import Rook
from piece import Piece


class Queen(Piece):
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        return Bishop().get_moves(x, y) + Rook().get_moves(x, y)

    def __str__(self):
        return 'Quen'

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        if x1 == x2 or y1 == y2:
            return Rook().get_moves_between(x1, y1, x2, y2)
        else:
            return Bishop().get_moves_between(x1, y1, x2, y2)
