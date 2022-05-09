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
        return (" 012\n" +
                "\n".join(str(i) + "".join(Board.SYMBOLS[entry] for entry in row) for i, row in enumerate(self.data)))

    def get_winner(self):
        for line in itertools.chain(
                self.data,
                self.data.transpose(),
                (self.data.diagonal(),
                 np.fliplr(self.data).diagonal())):
            if (line == 1).all():
                return 1
            elif (line == 2).all():
                return 2
        return 0

    def is_legal(self, x, y):
        return self.data[y][x] == 0


def nac(get_move_func):
    board = Board()
    for turn in range(9):
        player = turn % 2 + 1

        yield f"Turn {turn}\nPlayer {player} to move", board
        x, y = get_move_func(board.is_legal)
        board.data[y][x] = player

        if board.get_winner():
            yield f"Player {player} wins", board
            break
    else:
        yield "Draw", board
