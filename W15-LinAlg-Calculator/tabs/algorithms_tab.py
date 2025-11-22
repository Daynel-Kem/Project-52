import tkinter as tk
from tkinter import ttk
from helper import make_frame_scrollable

class Algorithm_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.inner, self.update_scroll = make_frame_scrollable(self)

        tk.Label(self, text="Algorithms", font=('Arial', 16)).pack(pady=20)

    # Functions to add
    """
    """