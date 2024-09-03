from states import Alive, Dead

cells = [["d","d","d","d"],["d","a","d","d"],["d","d","a","d"],["d","d","a","d"]]
class Game:
    def __init__(self):
        self.board = self.set_up_board()

    def set_up_board(self):
        empty_board = [[] for _ in range(len(cells))]
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                if cells[i][j] == "d":
                    empty_board[i].append(Dead())
                else:
                    empty_board[i].append(Alive())
        return empty_board

    def print_board(self):
        for i in self.board:
            print(i)

    def count_neighbours(self, x: int, y: int) -> int:
        count = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if not (i == 0 and j == 0) and type(self.board[x+i][y+j]) == Alive:
                        count += 1
                except IndexError:
                    continue

        return count

    def update_board(self) -> None:
        copied_board = [[] for _ in range(len(cells))]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                current_cell = self.board[i][j]
                neighbours = self.count_neighbours(i, j)
                copied_board[i].append(current_cell.get_next_state(neighbours))

        self.board = copied_board


game = Game()
game.print_board()
# print(game.count_neighbours(3, 1))
game.update_board()
print()
game.print_board()

