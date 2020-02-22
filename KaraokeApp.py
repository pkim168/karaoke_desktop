import tkinter as tk
import MenuPage, ScorePage, PlayerPage

class KaraokeApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", expand=True)

        self.test = tk.Label(self, text="This is the start page", width=20, borderwidth=1, relief="solid")
        self.test.place(relx=1.0, rely=1.0, x=2, y=2, anchor="nw")
