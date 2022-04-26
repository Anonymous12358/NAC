import argparse
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


def cli_get_move(board):
    while True:
        try:
            x, y = map(int, input("Enter move in `x y` format: ").split())
            if board.data[y][x] == 0:
                return x, y
        except (ValueError, IndexError):
            print("Please enter two integers within range, separated by a space")
        else:
            print("Please select an empty location")


def cli():
    game = play(cli_get_move)
    for printout, board in game:
        print(printout)
        print(board)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("naughtsandcrosses")
    parser.add_argument("ui", help="t for cli; g for gui (not implemented)", type=str, choices=("t", "g"))
    args = parser.parse_args()
    if args.ui == "t":
        cli()
    elif args.ui == "g":
        raise NotImplementedError
