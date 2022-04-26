import numpy as np
import itertools


class Board:
    SYMBOLS = ".", "X", "O"

    def __init__(self):
        self.__data = np.zeros((3, 3), dtype=np.uint8)

    @property
    def data(self):
        return self.__data

    def __str__(self):
        return "\n".join("".join(Board.SYMBOLS[entry] for entry in row) for row in self.data)

    def get_winner(self):
        for line in itertools.chain(
                self.data,
                self.data.transpose(),
                (self.data.diagonal(),
                 self.data.transpose().diagonal())):
            if (line == 1).all():
                return 1
            elif (line == 2).all():
                return 2
        return 0


def play(get_move_func):
    board = Board()
    for turn in range(9):
        player = turn % 2 + 1

        yield f"Turn {turn}\nPlayer {player} to move", board
        x, y = get_move_func(board)
        board.data[y][x] = player

        winner = board.get_winner()
        if winner:
            yield f"Player {player} wins", board
            break
    else:
        yield "Draw", board


def main():
    game = play(lambda _: map(int, input("Enter move in `x y` format: ").split()))
    for printout, board in game:
        print(printout)
        print(board)


if __name__ == '__main__':
    main()
