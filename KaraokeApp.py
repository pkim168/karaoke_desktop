import tkinter as tk
from tkinter import font  as tkfont
import page

class KaraokeApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # Creates a container to hold all frames
        container = tk.Frame(self)
        container.pack(side="top", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Creates array of frames
        self.frames = {}
        for i in (page.MenuPage, page.ScorePage, page.PlayerPage):
            page_name = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page_name] = frame

            # Puts all frames in same location
            # If frame is smaller than previous, will align to Top left
            if page_name == 'MenuPage':
                frame.grid(row=0, column=0, sticky="nw")
            else:
                frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PlayerPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == '__main__':
    root = KaraokeApp()
    root.mainloop()
