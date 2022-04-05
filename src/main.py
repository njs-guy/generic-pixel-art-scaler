# UI for main window

from importlib.resources import path
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import webbrowser, os, glob

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
        options_m.add_command(label='Open output folder...', command=lambda: openOutputFolder())

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

        # Asks user for a file, and then opens the image to scale it
        def openSprite():
            file_path = filedialog.askopenfilename()
            if file_path != '': # If file exists
                #messagebox.showinfo("Info", file_path)

                # get the scale_num and convert it to an int
                spr_scale = int(scale_num.get()) 

                # Scale the selected image by the current scale
                rescale_image(spr_scale, file_path) 

                # Open output folder when done
                openOutputFolder()
            else:
                # Show an error if the file does not exist
                invalidFileError() 
        
        # Asks user for a folder, and then opens every image in the folder to scale them
        def openSpriteFolder(path=''):
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
                
                openOutputFolder()
            else:
                invalidFileError()
        
        def openSpriteFromClipboard():
            pass
        
        def openAbout():
            pass
        
        # Opens the output folder in the file explorer
        def openOutputFolder():
            outputPath = "output"
            outputPath = os.path.realpath(outputPath)
            os.startfile(outputPath)
        
        # Opens the link to the Github repo in a web browser
        def viewSource():
            url = "https://github.com/njshockey/generic-pixel-art-scaler"
            webbrowser.open_new_tab(url)
        
        # Displays an invalid file error
        def invalidFileError():
            messagebox.showerror("Error", "Please select a valid file.")

# Driver
if __name__ == "__main__":
    app = App()
    app.mainloop()