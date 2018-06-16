__author__ = 'Mark Weinreuter'

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


# Ein Unterfenster mit einer Liste und 2 Buttons
fensterMitListe = Tk()

# Ein Container, in dem Objekte gruppiert werden können
container = Frame(fensterMitListe)

# Falls die Liste zu lang ist, brauchen wir einen Scrollbar (einen Balken am Rand zu scrollen)
scrollbar = Scrollbar(container)
# pack() aufrufen, bevor! die Listbox hinzugefügt wird
scrollbar.pack(side=RIGHT, fill=BOTH)

# Eine neue Liste (ListBox) erstellen und den Scroll-Befehl der Liste mit der Scrollbar verbinden
listbox = Listbox(container, yscrollcommand=scrollbar.set)
listbox["selectmode"] = EXTENDED

# Die ListBox mit Werten füllen
for i in range(100):
   listbox.insert(END, "Eintrag: " + str(i))

# Das Scrollen der Liste mit an die Scrollbox binden
scrollbar.config(command=listbox.yview)

# Pack aufrufen um das Layout zu erstellen, die Liste soll allen verfügbaren Raum füllen, x- und y-Richtung
listbox.pack(fill=BOTH)

# den Container anzeigen, mit einem Padding (Abstand zum Rand) von 5 Pixeln
container.pack(fill=BOTH, padx=5, pady=5)

# einen Button erstellen
okButton = Button(master=fensterMitListe, text="OK")

# den Button unter dem Container mit der Liste erstellen
okButton.pack(side=BOTTOM, pady=5)

def print_eintraege():
    # Alle markierten Einträge (genauer die Indices) bekommt man so
    eintraege = listbox.curselection()

    print("Alle Eintr#ge:")
    # die Einträge zu den Indices bekommt man mit get(...)
    for eintrag in eintraege:
        print(listbox.get(eintrag))

    # den aktuellen Eintrag bekommt man mittels get(ACTIVE)
    # Hier per Message Box ausgeben
    showinfo("Aktiver Eintrag", "Der aktuelle Eintrag ist: " +listbox.get(ACTIVE))

okButton["command"] = print_eintraege

fensterMitListe.mainloop()