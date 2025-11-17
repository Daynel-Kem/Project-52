import tkinter as tk
from tkinter import ttk

# Setting up the Window
root = tk.Tk()
root.title("Matrix Calculator")
root.geometry("1280x720")


# Matrix and Vector Sidebar
sidebar = tk.Frame(root, width=150, bg="#ddf")
sidebar.pack(side="left", fill="y")

content = tk.Frame(root)
content.pack(side="right", expand=True, fill="both")

# Will be one of the lists
vectors = ["v", "u", "c"]
matrices = ["A", "B"]

listbox = tk.Listbox(sidebar)
listbox.pack(expand=True, fill="both", padx=5, pady=5)

for vector in vectors:
    listbox.insert(tk.END, vector)

# Tabs
notebook = ttk.Notebook(content)
notebook.pack(expand=True, fill="both")

class Calculator_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Calculator", font=('Arial', 16)).pack(pady=20)

    # Functions to add
    """
    """

class Algorithm_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Algorithms", font=('Arial', 16)).pack(pady=20)

    # Functions to add
    """
    """

class Vectors_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Vectors").pack(pady=20)

        size = 0

        m_label = tk.Label(self, text="Size of Vector")
        m_label.pack(pady=1)
        m = tk.Entry(self, width=5)
        m.pack(pady=4)

        def make_vector():
            num = m.get()
            try:
                value = int(num)
                if value > 0:
                    return value
                else:
                    raise ValueError("Int is less than or equal to 0")
            except ValueError:
                raise ValueError("Not an Integer")


    # Make it so u can add a n-sized vector and also show current list of vectors

class Matrices_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Matrices").pack(pady=20)

    # Make it so u can add a mxn matrix and also show a list of current matrices

# Add tabs to the notebook
notebook.add(Vectors_Tab(notebook), text="Vectors")

notebook.add(Calculator_Tab(notebook), text="Calculator")
notebook.add(Algorithm_Tab(notebook), text="Algorithms")

notebook.add(Matrices_Tab(notebook), text="Matrices")


# # Adds the Label to the textbox
# label = tk.Label(root, text="Enter your name: ")
# label.pack(pady=5) # .pack actually puts the thing into the window

# # The actual textbox
# entry = tk.Entry(root)
# entry.pack(pady=2)

# def submit():
#     print("Hello, ", entry.get())

# # The button
# button = tk.Button(root, text="Submit", command=submit)
# button.pack(pady=10)

# Starts the app and the main loop
root.mainloop()