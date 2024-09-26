from piece import Piece

class King(Piece):
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        return [
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y)
        ]


    def __str__(self):
        return self.get_piece_name("King")

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        return []

