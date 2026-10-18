import tkinter as tk
from counter import Counter


class Player(tk.Frame):
    def __init__(self, parent, player_name, starting_life=20):
        super().__init__(parent)

        # Player name
        self.player_name = tk.Label(
            self,
            text=player_name
        )
        self.player_name.grid(row=0, column=0)

        # Life counter
        self.life_counter = Counter(
            self,
            name="Life",
            starting_value=starting_life
        )
        self.life_counter.grid(row=1, column=0)

        # Poison counter
        self.poison_counter = Counter(
            self,
            name="Poison",
            starting_value=0
        )
        self.poison_counter.grid(row=2, column=0)