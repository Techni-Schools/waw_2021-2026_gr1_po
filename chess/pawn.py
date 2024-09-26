from chess.piece import Piece
from color import Color

class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.moved = False

    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        color_direction = 1 if self.color == Color.WHITE else -1
        moves = [(x - 1, y + color_direction), (x, y + color_direction), (x + 1, y + color_direction)]

        if not self.moved:
            moves.append((x, y + color_direction * 2))

        return moves

    def __str__(self):
        return self.get_piece_name("Pawn")
    
    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        if abs(y1 - y2) == 2:
            step = 1 if y1 < y2 else -1
            return [(x1, y1 + step)]
        else:
            return []