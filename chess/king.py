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