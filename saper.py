import tkinter as tk
import random

class Minesweeper(tk.Tk):
    def __init__(self, rows=10, cols=10, mines=10):
        super().__init__()
        self.title("Minesweeper")
        self.geometry(f"{cols*30}x{rows*30}")
        self.resizable(False, False)

        self.rows = rows
        self.cols = cols
        self.mines = mines

        self.buttons = {}
        self.create_widgets()
        self.place_mines()
        self.update_counts()

    def create_widgets(self):
        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self, width=3, height=1, command=lambda r=row, c=col: self.click(r, c))
                button.bind("<Button-3>", lambda e, r=row, c=col: self.right_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

    def place_mines(self):
        self.mines_locations = set(random.sample(self.buttons.keys(), self.mines))
        self.mine_count = {loc: 0 for loc in self.buttons.keys()}

        for mine in self.mines_locations:
            for r in range(mine[0] - 1, mine[0] + 2):
                for c in range(mine[1] - 1, mine[1] + 2):
                    if (r, c) in self.mine_count:
                        self.mine_count[(r, c)] += 1

    def update_counts(self):
        for (r, c), button in self.buttons.items():
            if (r, c) in self.mines_locations:
                button.config(text='*')
            else:
                button.config(text=str(self.mine_count[(r, c)]))

    def click(self, row, col):
        if (row, col) in self.mines_locations:
            self.game_over(False)
        else:
            self.reveal(row, col)
            if self.check_win():
                self.game_over(True)

    def right_click(self, row, col):
        button = self.buttons[(row, col)]
        if button['text'] == 'F':
            button.config(text='')
        else:
            button.config(text='F')

    def reveal(self, row, col):
        button = self.buttons[(row, col)]
        if button['state'] == 'disabled':
            return
        button.config(state='disabled', relief=tk.SUNKEN)
        if self.mine_count[(row, col)] == 0:
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if (r, c) in self.buttons:
                        self.reveal(r, c)

    def check_win(self):
        for (row, col), button in self.buttons.items():
            if (row, col) not in self.mines_locations and button['state'] != 'disabled':
                return False
        return True

    def game_over(self, won):
        for button in self.buttons.values():
            button.config(state='disabled')
        if won:
            message = "You won!"
        else:
            message = "Game over!"
        tk.messagebox.showinfo("Game Over", message)
        self.after(2000, self.destroy)

if __name__ == "__main__":
    game = Minesweeper()
    game.mainloop()