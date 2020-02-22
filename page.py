import tkinter as tk

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Menu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Player page",
                           command=lambda: controller.show_frame("PlayerPage"))
        button.pack()

class ScorePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Score page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Menu",
                            command=lambda: controller.show_frame("MenuPage"))
        button2 = tk.Button(self, text="Go to Player",
                            command=lambda: controller.show_frame("PlayerPage"))
        button1.pack()
        button2.pack()

class PlayerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Player page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Menu",
                            command=lambda: controller.show_frame("MenuPage"))
        button2 = tk.Button(self, text="Go to Score",
                            command=lambda: controller.show_frame("ScorePage"))
        button1.pack()
        button2.pack()
