from cell import Cell

class Alive(Cell):
    def __repr__(self):
        return "Alive"

    def get_next_state(self, neighbours: int):
        if neighbours in [2, 3]:
            return self
        else:
            return Dead()

class Dead(Cell):
    def __repr__(self):
        return "Dead"

    def get_next_state(self, neighbours: int):
        if neighbours == 3:
            return Alive()
        else:
            return self