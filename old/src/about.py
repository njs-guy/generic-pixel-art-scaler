# UI for about window

import tkinter as tk
from tkinter import *
from tkinter import ttk

from version import get_gpas_version

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Window properties
        self.geometry('500x300')
        self.resizable(False, False)
        self.title('About GPAS')
        self.iconbitmap('./src/img/gpas_logo.ico')

        version = get_gpas_version()
        self.logo = tk.PhotoImage(file="./src/img/gpas_logo.png")
        lbl_about = ttk.Label(self, 
            image=self.logo, 
            text=f"Generic Pixel Art Scaler v{version}", 
            compound='top')
        lbl_about.pack(ipadx=10, ipady=10)

        lbl_creator = ttk.Label(self, text="Created by Nick Shockey under the MIT license.")
        lbl_creator.pack(ipadx=10, ipady=10, side='bottom')