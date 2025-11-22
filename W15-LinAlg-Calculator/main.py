import tkinter as tk
from tkinter import ttk
from helper import is_natural_number, ScrollableTab
import numpy as np
from logic import LogicApp
from tabs.vectors_tab import Vectors_Tab, vectors
from tabs.matrices_tab import Matrices_Tab
from tabs.calculator_tab import Calculator_Tab
from tabs.algorithms_tab import Algorithm_Tab

app = LogicApp()

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
matrices = ["A", "B"]

listbox = tk.Listbox(sidebar)
listbox.pack(expand=True, fill="both", padx=5, pady=5)

for vector in vectors:
    listbox.insert(tk.END, vector)

# Tabs
notebook = ttk.Notebook(content)
notebook.pack(expand=True, fill="both")

# Add tabs to the notebook
notebook.add(Vectors_Tab(notebook), text="Vectors")
notebook.add(Matrices_Tab(notebook), text="Matrices")

notebook.add(Calculator_Tab(notebook), text="Calculator")
notebook.add(Algorithm_Tab(notebook), text="Algorithms")


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