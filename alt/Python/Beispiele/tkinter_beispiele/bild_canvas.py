from tkinter import *

fenster = Tk()

# Foto erstellen, das Bild muss im gleichen Ordner liegen!!
photo = PhotoImage(file="python_bild.png")


"""
Falls tkinter keine png-Bilder direkt laden kann,
dann kannst du das Bild wieder über PIL laden

from PIL import Image, ImageTk

bild = Image.open("python_bild.png")
photo = ImageTk.PhotoImage(bild)
"""

# Ein Label mit Bild
photo_label = Label(image=photo)
photo_label.image = photo
photo_label.pack()

text = Label(text="Noch ein bisschen Text")
text.pack()

fenster.mainloop()
