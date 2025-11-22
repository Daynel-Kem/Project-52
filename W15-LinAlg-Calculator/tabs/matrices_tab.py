import tkinter as tk
from tkinter import ttk
from helper import make_frame_scrollable

class Matrices_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.inner, self.update_scroll = make_frame_scrollable(self)

        tk.Label(self, text="Matrices").pack(pady=20)

    # Make it so u can add a mxn matrix and also show a list of current matrices