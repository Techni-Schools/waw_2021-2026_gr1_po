from chess.piece import Piece
from color import Color

class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.moved = False

    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        moves = [(x-1, y+1), (x, y+1), (x+1, y+1)]

        if not self.moved:
            moves.append((x, y+2))

        return moves

    def __str__(self):
        return self.get_piece_name("Pawn")
    
    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        if abs(y1 - y2) == 2:
            step = 1 if y1 < y2 else -1
            return [(x1, y1 + step)]
        else:
            return []