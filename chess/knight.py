from piece import Piece

class Knight(Piece):

    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        return [(x+2, y-1),
                (x+1, y-2),
                (x+1, y+2),
                (x-2, y-1),
                (x-2, y+1),
                (x-1, y+2),
                (x+2, y+1),
                (x-1, y-2)]

    def __str__(self):
        return self.get_piece_name("Knht")

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        return []

