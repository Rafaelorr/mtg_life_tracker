import tkinter as tk


class Counter(tk.Frame):
    def __init__(self, parent, name, starting_value=0):
        super().__init__(parent)

        self.name = name
        self.value = starting_value

        # Counter display
        self.display = tk.Label(
            self,
            text=f"{self.name}: {self.value}"
        )
        self.display.grid(row=0, column=0, columnspan=2)

        # Decrease button
        self.decrease_button = tk.Button(
            self,
            text="-",
            command=lambda: self.change(-1)
        )
        self.decrease_button.grid(row=1, column=0)

        # Increase button
        self.increase_button = tk.Button(
            self,
            text="+",
            command=lambda: self.change(1)
        )
        self.increase_button.grid(row=1, column=1)

    def change(self, amount):
        self.value += amount
        self.update_display()

    def update_display(self):
        self.display.config(
            text=f"{self.name}: {self.value}"
        )