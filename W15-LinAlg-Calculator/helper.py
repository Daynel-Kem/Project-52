import tkinter as tk
from tkinter import ttk

def is_natural_number(s):
    try:
        num = int(s)
        if num > 0:
            return True, num
        else:
            return False, -1
    except ValueError:
        return False, -1
    
# ChatGPT generated this function to make a scrollable tab in a notebook, use now, understand later
"""
To use:
setup the class as

class Class_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.inner, self.update_scroll = make_frame_scrollable(self)

and whenever you .pack do it with self.inner
i.e.
label = tk.Label()
label.pack(self.inner)

and whenever you add any elements that could make the frame scrollable (such as adding additional widgets), call the function
self.update_scroll()
"""
def make_frame_scrollable(parent):
    import tkinter as tk
    from tkinter import ttk

    # --- Canvas + Scrollbar ---
    canvas = tk.Canvas(parent, highlightthickness=0)
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Layout (IMPORTANT: pack canvas BEFORE scrollbar so it fills properly)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # --- Inner frame (where widgets go) ---
    inner = ttk.Frame(canvas)

    # Create window and LET IT STRETCH horizontally
    window = canvas.create_window(
        (0, 0),
        window=inner,
        anchor="nw",
        width=canvas.winfo_width()   # <--- FIX: ensures full width
    )

    # When inner changes size → update scrollregion
    def update_scrollregion(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner.bind("<Configure>", update_scrollregion)

    # When canvas resizes → stretch inner frame horizontally
    def resize_inner(event):
        canvas.itemconfig(window, width=event.width)

    canvas.bind("<Configure>", resize_inner)

    return inner, update_scrollregion