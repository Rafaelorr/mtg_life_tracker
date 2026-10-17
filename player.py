import tkinter as tk

class Player(tk.Frame):
    def __init__(self, parent, player_name, starting_life=20):
        super().__init__(parent)

        self.life = starting_life
        self.poison = 0

        # Speler Naam Onderdeel
        self.player_name = tk.Label(
            self,
            text=player_name
        )
        self.player_name.grid(row=0, column=0, columnspan=2)

        # Speler Life Code
        ## Speler Life Display Onderdeel
        self.life_counter = tk.Label(
            self,
            text=f"Life: {self.life}"
        )
        self.life_counter.grid(row=1, column=0, columnspan=2)

        self.life_min = tk.Button(
            self,
            text="-",
            command=lambda: self.change_life(-1)
        )
        self.life_min.grid(row=2, column=0)

        self.life_plus = tk.Button(
            self,
            text="+",
            command=lambda: self.change_life(1)
        )
        self.life_plus.grid(row=2, column=1)


        # Speler Poison Code
        ## Speler Poison Display Onderdeel
        self.poison_counter = tk.Label(
            self,
            text=f"Poison: {self.poison}"
        )
        self.poison_counter.grid(row=3, column=0, columnspan=2)

        self.poison_min = tk.Button(
            self,
            text="-",
            command=lambda: self.change_poison(-1)
        )
        self.poison_min.grid(row=4, column=0)

        self.poison_plus = tk.Button(
            self,
            text="+",
            command=lambda: self.change_poison(1)
        )
        self.poison_plus.grid(row=4, column=1)


    def change_life(self, amount):
        self.life += amount
        self.life_counter.config(text=f"Life: {self.life}")

    def change_poison(self, amount):
        self.poison += amount
        self.poison_counter.config(text=f"Poison: {self.poison}")
