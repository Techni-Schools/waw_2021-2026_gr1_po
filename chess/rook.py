from piece import Piece

class Rook(Piece):
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        column_moves = [
            (x, y + i) for i in range(-7, 0)
        ]

        column_moves.extend([
            (x, y + i) for i in range(1, 8)
        ])

        row_moves = [
            (x + i, y) for i in range(-7, 0)
        ]

        row_moves.extend([
            (x + i, y) for i in range(1, 8)
        ])

        column_moves.extend(row_moves)
        return column_moves

    def __str__(self):
        return "Rook"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        if x1 == x2:
            step = 1 if y1 < y2 else -1
            return [(x1, i) for i in range(y1+step, y2, step)]
        elif y1 == y2:
            step = 1 if x1 < x2 else -1
            return [(i, y1) for i in range(x1+step, x2, step)]
