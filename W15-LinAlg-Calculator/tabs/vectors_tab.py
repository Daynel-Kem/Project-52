import tkinter as tk
from tkinter import ttk
from helper import ScrollableTab, is_natural_number, make_frame_scrollable
import numpy as np

# List of numpy vectors
vectors = []

class Vectors_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.inner, self.update_scroll = make_frame_scrollable(self)

        size = 0

        tk.Label(self.inner, text="Vectors").pack(pady=20)

        m_label = tk.Label(self.inner, text="Size of Vector")
        m_label.pack(pady=1)
        m = tk.Entry(self.inner, width=5)
        m.pack(pady=4)

        self.size_error_label = None
        self.vector_inputs = []

        def setup_vector():
            if self.size_error_label is not None:
                self.size_error_label.destroy()
                self.size_error_label = None
            
            if self.vector_creation_fail_label is not None:
                self.vector_creation_fail_label.destroy()
                self.vector_creation_fail_label = None

            if len(self.vector_inputs) != 0:
                for entry in self.vector_inputs:
                    entry.destroy()
                self.vector_inputs.clear()
            
            t_o_f, size = is_natural_number(m.get())
            if t_o_f is False:
                self.size_error_label = tk.Label(self.inner, text="Invalid Input", fg="red")
                self.size_error_label.pack(pady=1)
            else:
                label = tk.Label(self.inner, text="Input Values")
                self.vector_inputs.append(label)
                label.pack(pady=3)
                for i in range(size):
                    entry = tk.Entry(self.inner, width=5)
                    self.vector_inputs.append(entry)
                    entry.pack(pady=2)
                create_vector_button = tk.Button(self.inner, text="Create", command=make_vector)
                create_vector_button.pack(pady=5)
                self.vector_inputs.append(create_vector_button)
                self.update_scroll()
        
        size_button = tk.Button(self.inner, text="Submit", command=setup_vector)
        size_button.pack(pady=3)

        self.vector_creation_fail_label = None

        def make_vector():
            if self.vector_creation_fail_label is not None:
                self.vector_creation_fail_label.destroy()
                self.vector_creation_fail_label = None

            vector = []
            global vectors
            success = True
            for vector_entry in self.vector_inputs:
                if not isinstance(vector_entry, tk.Entry):
                    continue
                val = vector_entry.get()
                try:
                    float(val)
                except Exception:
                    self.vector_creation_fail_label = tk.Label(self.inner, text="Invalid Input", fg="red")
                    self.vector_creation_fail_label.pack(pady=1)
                    success = False
                    print(val)
                    break
                vector.append(val)
            if success:
                vectors.append(np.array(vector))
            
        def list_vectors():
            global vectors
            print(vectors)

        list_vectors = tk.Button(self.inner, text="Yes", command=list_vectors)
        list_vectors.pack(pady=10)

        def update_vector_list():
            pass



    # Make it so u can add a n-sized vector and also show current list of vectors