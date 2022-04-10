# UI for about window

import tkinter as tk
from tkinter import *
from tkinter import ttk

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Window properties
        self.geometry('500x300')
        self.resizable(False, False)
        self.title('About GPAS')

        version = "1.0.0"
        lbl_about = ttk.Label(self, text=f"Generic Pixel Art Scaler v{version}")
        lbl_about.pack(ipadx=10, ipady=10, side='top', fill='x')

        lbl_creator = ttk.Label(self, text="Created by Nick Shockey under the MIT license.")
        lbl_creator.pack(ipadx=10, ipady=10, side='bottom', fill='x')