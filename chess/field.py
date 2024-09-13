from piece import Piece

class Field:
    def __init__(self, piece: Piece = None):
        self.piece = piece

    def __str__(self) -> str:
        if self.piece is None:
            return "____"

        return str(self.piece)