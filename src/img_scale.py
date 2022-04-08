# Code for image rescaling

from PIL import Image, ImageGrab
import os

def rescale_image(scale = 2, path=''):
    # image and output vars
    img = Image.open(path)
    output = 'output'

    # Get the width and height and muliply it by the scale
    width = img.size[0] * scale
    height = img.size[1] * scale
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output):
        os.makedirs(output)

    # Create scaled image in output folder
    if hasattr(img, 'filename'): # Check if the img has a file name attribute
        fn = newFileName(str(img.filename))
        #print(fn)
        scaled_img = img.resize((width, height), Image.NEAREST)
        scaled_img.save(output + "/" + fn + ".png", 'png')

    else:
        print(str(img) + " is not a valid image.")

def rescale_clipboard(scale = 2):
    img = ImageGrab.grabclipboard()
    output = 'output/'

    # Get the width and height and muliply it by the scale
    width = img.size[0] * scale
    height = img.size[1] * scale

    scaled_img = img.resize((width, height), Image.NEAREST)
    scaled_img.save(output + "clipboard.png", "PNG")

def newFileName(filepath):
    # splits the path down to the file name ex: 'test.png'
    filename = filepath.split('/')[-1]
    
    # removes the extension from the file name ex: 'test' 
    filename = filename.split('.')[0]
    
    return filename