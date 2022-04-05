# UI for main window

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser

from img_scale import rescale_image

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.geometry('400x200')
        self.resizable(False, False)
        self.title('Generic Pixel Art Scaler')

        # Variables
        scale_num = StringVar()
        scale_num.set('2') # Default value.

        theme = StringVar()
        theme.set('0') # Default value

        export_type = StringVar()
        export_type.set('0') # Default value

        # UI ######################
        self.sb_scale = ttk.Spinbox(from_=2, to=500,textvariable=scale_num, wrap=False)
        self.sb_scale.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.lbl_scale = ttk.Label(text="Scale:")
        self.lbl_scale.place(relx=0.25, rely=0.1, anchor=CENTER)
        
        self.lbl_files = ttk.Label(text="Open some pixel art to resize it...")
        self.lbl_files.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.btn_open_file = ttk.Button(text="Open file", width=12, command=lambda: openSprite())
        self.btn_open_file.place(relx=0.35, rely=0.6, anchor=CENTER)

        self.btn_open_folder = ttk.Button(text="Open folder", width=12, command=lambda: openSpriteFolder())
        self.btn_open_folder.place(relx=0.65, rely=0.6, anchor=CENTER)

        # Copy from clipboard

        # Menu bar ######################
        menubar = Menu(self, relief=FLAT, bd=0)
        self.config(menu=menubar)

        # Options - Settings, Open output folder, Exit
        options_m = Menu(menubar, tearoff=0, activeborderwidth=3)
        options_m.add_command(label='Open output folder...')

        # Export submenu
        export_submenu = Menu(options_m, tearoff=0, activeborderwidth=3)
        export_submenu.add_radiobutton(label='PNG')
        export_submenu.add_radiobutton(label='Static GIF')
        export_submenu.add_radiobutton(label='JPEG')
        options_m.add_cascade(label='Export as...', menu=export_submenu)

        options_m.add_separator()
        options_m.add_command(label='Exit', command=self.destroy)

        # Theme
        # theme_m = Menu(options_m, tearoff=0, activeborderwidth=3)
        # theme_m.add_radiobutton(label='Theme1')
        # theme_m.add_radiobutton(label='Theme2')

        # Help - About, Source code
        help_m = Menu(menubar, tearoff=0, activeborderwidth=3)
        help_m.add_command(label='About', command=lambda: openAbout())
        help_m.add_command(label='Source code', command=lambda: viewSource())

        # Add to window
        menubar.add_cascade(label='Options', menu=options_m)
        # menubar.add_cascade(label='Theme', menu=theme_m)
        menubar.add_cascade(label='Help', menu=help_m)

        def openSprite():
            file_path = filedialog.askopenfilename()
            if file_path != '':
                #messagebox.showinfo("Info", file_path)
                spr_scale = int(scale_num.get())
                rescale_image(spr_scale, file_path)
            else:
                invalidFileError()
        
        def openSpriteFolder(path=''):
            if path != '':
                pass
            else:
                invalidFileError()
        
        def openSpriteFromClipboard():
            pass
        
        def openAbout():
            pass
        
        def viewSource():
            url = "https://github.com/njshockey/generic-pixel-art-scaler"
            webbrowser.open_new_tab(url)
        
        def invalidFileError():
            messagebox.showerror("Error", "Please select a valid file.")

# Driver
if __name__ == "__main__":
    app = App()
    app.mainloop()

# rescale_image(30, 'src/test.png')
# print("Output file to output folder.")
