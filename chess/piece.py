from abc import abstractmethod

from color import Color


class Piece:
    def __init__(self, color: Color = Color.WHITE):
        self.color = color

    def get_piece_name(self, piece_name: str):
        if self.color == Color.WHITE:
            return piece_name.upper()
        else:
            return piece_name.lower()

    @abstractmethod
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        pass

    @abstractmethod
    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        pass
