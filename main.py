import tkinter as tk
from player import Player

class GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("MTG Life Tracker")

        # Title
        self.title = tk.Label(
            self.root,
            text="Life Tracker voor 1v1 Magic The Gathering",
            font=("Arial", 15)
        )
        self.title.pack(pady=10)

        # Container for the players
        self.players_frame = tk.Frame(self.root)
        self.players_frame.pack(fill="both", expand=True)

        # Make both columns expand equally
        self.players_frame.columnconfigure(0, weight=1)
        self.players_frame.columnconfigure(1, weight=1)

        # Create the player widgets
        self.player_1 = Player(
            self.players_frame,
            "Player 1"
        )
        self.player_1.grid(row=0, column=0, padx=20, pady=20)

        self.player_2 = Player(
            self.players_frame,
            "Player 2"
        )
        self.player_2.grid(row=0, column=1, padx=20, pady=20)

        self.root.mainloop()


GUI()