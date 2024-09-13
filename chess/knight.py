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
        return "Knht"