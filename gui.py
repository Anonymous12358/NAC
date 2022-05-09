import tkinter as tk
import time


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Naughts and Crosses")
        self.__frame = tk.Frame(self)
        self.__frame.pack()

        self.__buttons = [[tk.Button(self.__frame) for _ in range(3)] for _ in range(3)]
        self.__text_vars = [[tk.StringVar() for _ in range(3)] for _ in range(3)]
        for y, row in enumerate(self.__buttons):
            for x, button in enumerate(row):
                self.__text_vars[y][x].set("-")
                button.configure(textvariable=self.__text_vars[y][x])
                button.grid(column=y, row=x)

        self.__dialogue_text_var = tk.StringVar()
        tk.Label(self.__frame, textvariable=self.__dialogue_text_var).grid(column=4, row=4)

        self.__result_x, self.__result_y = tk.IntVar(), tk.IntVar()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def on_exit(self):
        self.__result_x.set(0)
        self.__result_y.set(0)
        self.destroy()

    def display_move(self, printout, board):
        for y, row in enumerate(self.__text_vars):
            for x, text_var in enumerate(row):
                text_var.set(board.SYMBOLS[board.data[y][x]])
        self.__dialogue_text_var.set(printout)

        self.update()

    def get_move(self, is_legal):
        def gen_button_cmd(x, y):
            def button_cmd():
                self.__result_x.set(x)
                self.__result_y.set(y)

            return button_cmd

        for y, row in enumerate(self.__buttons):
            for x, button in enumerate(row):
                if is_legal(x, y):
                    button.configure(command=gen_button_cmd(x, y))
                else:
                    button.configure(command=lambda: None)

        self.wait_variable(self.__result_y)
        return self.__result_x.get(), self.__result_y.get()


def gui(game):
    gui = Gui()
    for printout, board in game(gui.get_move):
        gui.display_move(printout, board)
    time.sleep(2)
