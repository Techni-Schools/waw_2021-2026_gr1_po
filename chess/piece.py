from abc import abstractmethod

class Piece:
    @abstractmethod
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        pass

    @abstractmethod
    def get_moves_beetwen(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        pass

