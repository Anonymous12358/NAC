import argparse

import gui
import naughtsandcrosses


def cli_get_move(is_legal):
    while True:
        try:
            x, y = map(int, input("Enter move in `x y` format: ").split())
            if is_legal(x, y):
                return x, y
        except (ValueError, IndexError):
            print("Please enter two integers within range, separated by a space")
        else:
            print("Please select an empty location")


def cli(game):
    for printout, board in game(cli_get_move):
        print(printout)
        print(board)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("naughtsandcrosses")
    parser.add_argument("ui", help="t for cli; g for gui (not implemented)", type=str, choices=("t", "g"))
    args = parser.parse_args()
    if args.ui == "t":
        cli(naughtsandcrosses.nac)
    elif args.ui == "g":
        gui.gui(naughtsandcrosses.nac)
