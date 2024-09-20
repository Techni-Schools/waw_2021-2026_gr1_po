from piece import Piece

class Bishop(Piece):
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        column_moves = [
            (x + i, y + i) for i in range(-7, 0)
        ]

        column_moves.extend([
            (x + i, y + i) for i in range(1, 8)
        ])


        row_moves = [
            (x - i, y + i) for i in range(-7, 0)
        ]

        row_moves.extend([
            (x - i, y + i) for i in range(1, 8)
        ])

        column_moves.extend(row_moves)
        return column_moves

    def __str__(self):
        return "Shop"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        return [(i, j) for i, j in zip(range(step_x + x1, x2, step_x), range(step_y + y1, y2, step_y))]
