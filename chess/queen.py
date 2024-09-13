from chess.bishop import Bishop
from chess.rook import Rook
from piece import Piece


class Queen(Piece):
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        return Bishop().get_moves(x, y) + Rook().get_moves(x, y)

    def __str__(self):
        return 'Quen'