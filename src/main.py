# UI for main window

import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import webbrowser, os, glob

from img_scale import rescale_image, rescale_clipboard
from about import About

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
        self.lbl_scale = ttk.Label(text="Scale:")
        self.lbl_scale.place(relx=0.25, rely=0.1, anchor=CENTER)

        self.sb_scale = ttk.Spinbox(from_=2, to=500,textvariable=scale_num, wrap=False)
        self.sb_scale.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        self.lbl_files = ttk.Label(text="Open some pixel art to resize it...")
        self.lbl_files.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.btn_open_file = ttk.Button(text="Open file", width=12, command=lambda: open_sprite())
        self.btn_open_file.place(relx=0.15, rely=0.6, anchor=CENTER)

        self.btn_open_folder = ttk.Button(text="Open folder", width=12, command=lambda: open_sprite_folder())
        self.btn_open_folder.place(relx=0.45, rely=0.6, anchor=CENTER)

        self.btn_open_file = ttk.Button(text="Copy from Clipboard", width=20, command=lambda: open_sprite_from_clipboard())
        self.btn_open_file.place(relx=0.75, rely=0.6, anchor=CENTER)

        # Menu bar ######################
        menubar = Menu(self, relief=FLAT, bd=0)
        self.config(menu=menubar)

        # Options - Settings, Open output folder, Exit
        options_m = Menu(menubar, tearoff=0, activeborderwidth=3)
        options_m.add_command(label='Open output folder...', command=lambda: open_output_folder())

        # Export submenu
        #export_submenu = Menu(options_m, tearoff=0, activeborderwidth=3)
        #export_submenu.add_radiobutton(label='PNG')
        #export_submenu.add_radiobutton(label='Static GIF')
        #export_submenu.add_radiobutton(label='JPEG')
        #options_m.add_cascade(label='Export as...', menu=export_submenu)

        options_m.add_separator()
        options_m.add_command(label='Exit', command=self.destroy)

        # Theme
        # theme_m = Menu(options_m, tearoff=0, activeborderwidth=3)
        # theme_m.add_radiobutton(label='Theme1')
        # theme_m.add_radiobutton(label='Theme2')

        # Help - About, Source code
        help_m = Menu(menubar, tearoff=0, activeborderwidth=3)
        help_m.add_command(label='About', command=lambda: self.open_about())
        help_m.add_command(label='Source code', command=lambda: view_source())

        # Add to window
        menubar.add_cascade(label='Options', menu=options_m)
        # menubar.add_cascade(label='Theme', menu=theme_m)
        menubar.add_cascade(label='Help', menu=help_m)

        # Asks user for a file, and then opens the image to scale it
        def open_sprite():
            file_path = filedialog.askopenfilename()
            try:
                #messagebox.showinfo("Info", file_path)

                # get the scale_num and convert it to an int
                spr_scale = int(scale_num.get()) 

                # Scale the selected image by the current scale
                rescale_image(spr_scale, file_path) 

                # Open output folder when done
                open_output_folder()
            except:
                # Show an error if the file does not exist
                invalid_file_error() 
        
        # Asks user for a folder, and then opens every image in the folder to scale them
        def open_sprite_folder(path=''):
            file_path = filedialog.askdirectory(title="Select folder...")
            if file_path != '': # If folder exists
                #messagebox.showinfo("Info", file_path)

                # get the scale_num and convert it to an int
                spr_scale = int(scale_num.get())

                # For each file in the folder
                for spr in glob.glob(os.path.join(file_path, '*.png')):
                    
                    # Open each file as read only
                    with open(os.path.join(os.getcwd(), spr), 'r') as f:
                        # Replace the back slash with a forward slash
                        spr = spr.replace("\\", "/")

                        # Scale the current image
                        rescale_image(spr_scale, spr)
                
                open_output_folder()
            else:
                invalid_file_error()
        
        def open_sprite_from_clipboard():
            # get the scale_num and convert it to an int
            spr_scale = int(scale_num.get())
            
            try:
                rescale_clipboard(spr_scale)
                open_output_folder()
            except:
                messagebox.showerror("Error", "Please copy a valid image to the clipboard.")

        # Opens the output folder in the file explorer
        def open_output_folder():
            outputPath = "output"
            outputPath = os.path.realpath(outputPath)
            os.startfile(outputPath)
        
        # Opens the link to the Github repo in a web browser
        def view_source():
            url = "https://github.com/njshockey/generic-pixel-art-scaler"
            webbrowser.open_new_tab(url)
        
        # Displays an invalid file error
        def invalid_file_error():
            messagebox.showerror("Error", "Please select a valid file.")
    
    def open_about(self):
        aw = About(self)
        aw.grab_set()

# Driver
if __name__ == "__main__":
    app = App()
    app.mainloop()