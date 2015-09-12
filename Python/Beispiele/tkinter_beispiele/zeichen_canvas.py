__author__ = 'Mark Weinreuter'

from tkinter import *
# ACHTUNG: Pillow muss installiert sein: Z.B: 'pip install Pillow' in der Konsole ausführen
from PIL import Image, ImageTk


master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()

# Linie mit Dicke 5 in Rot
i = w.create_line((30, 30, 50, 200), width=5, fill="red")
# Wird ein Objekt erstellt, dann bekommt man eine Nummer zurück
# Über diese Nummer, kann man diese wieder finden

j = w.create_line((130, 30, 150, 100), width=5, fill="blue")

# Farbe ändern, über die Nummer gespeichert in j
w.itemconfig(j, fill="green")


# Zum entfernen
# w.delete(i)


# Die Koordinaten, bzw. der Start-, Endpunkt auslesen
koordinaten = w.coords(i)
print(koordinaten)


def bewegen():
    # Koordinaten, bzw. start-punkt, end-punkt ändern
    w.coords(i, (330, 30, 200, 200))


bild = Image.open("python_bild.png")
photo = ImageTk.PhotoImage(bild)


# Button der, die Linie bewegt
b = Button(text="Bewege", image=photo, command=bewegen)
b.pack()

master.mainloop()
