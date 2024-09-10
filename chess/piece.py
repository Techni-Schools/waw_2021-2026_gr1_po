from abc import abstractmethod

class Piece:
    @abstractmethod
    def get_moves(self, x: int, y: int) -> list[tuple[int, int]]:
        pass