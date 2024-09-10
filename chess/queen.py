from piece import Piece


class Queen(Piece):
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

        column_moves.extend([
            (x + i, y + i) for i in range(-7, 0)
        ])

        column_moves.extend([
            (x + i, y + i) for i in range(1, 8)
        ])

        column_moves.extend([
            (x - i, y + i) for i in range(-7, 0)
        ])

        column_moves.extend([
            (x - i, y + i) for i in range(1, 8)
        ])

        return column_moves
