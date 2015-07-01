__author__ = 'Mark Weinreuter'

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

# Das Hauptfenster
fenster = Tk()

# Diese Variable speichert den aktuellen Spieler
spielerEins = True

# Die Liste mit all unseren Buttons
buttons = []


def gewonnen(ersterSpieler):
    # Der aktuelle Spieler hat gewonnen
    if ersterSpieler:
        showinfo("Das Spiel ist vorbei!", "Spieler 1 gewinnt!")
    else:
        showinfo("Das Spiel ist vorbei!", "Spieler 2 gewinnt!")

    # Die Texte aller Buttons zurücksetzen
    for button in buttons:
        button["text"] = "?"


def buttonGedrueckt(button):
    global spielerEins

    # überprufen ob der Button schon besetzt ist
    if button["text"] != "?":
        return

        # Der Button gehört jetzt dem aktuellen Spieler
    if spielerEins:
        button["text"] = "X"
    else:
        button["text"] = "O"


    # Spieler tauschen
    spielerEins = not spielerEins

    # Wir müssen beide Diagonalen überprüfen
    textDiagonalLinks = buttons[0]["text"] + buttons[4]["text"] + buttons[8]["text"]
    textDiagonalRechts = buttons[2]["text"] + buttons[4]["text"] + buttons[6]["text"]

    if textDiagonalRechts == "XXX" or textDiagonalLinks == "XXX":
        gewonnen(True)
    if textDiagonalRechts == "OOO" or textDiagonalLinks == "OOO":
        gewonnen(False)

    # und wir müsse alle Reihen und Spalten auf 3 Gleiche überprüfen
    for spalte in range(0, 3):
        textHorizontal = ""
        textVertikal = ""

        # Wir fügen die Texte der Buttons aller Spalten und Reihen zusammen und überprüfen auf 3 Richtige
        for reihe in range(0, 3):
            textVertikal += buttons[reihe * 3 + spalte]["text"]  # Z.B: die Einträge 0, 3, 6
            textHorizontal += buttons[spalte * 3 + reihe]["text"]  # Z.B: die Einträge 3,4,5

        if textHorizontal == "XXX" or textVertikal == "XXX":
            gewonnen(True)
            break  # die for-Schleife abbrechen

        elif textHorizontal == "OOO" or textVertikal == "OOO":
            gewonnen(False)
            break

# Die Überschrift
ueberschrift = Label(fenster, text="Klicke auf die Buttons und spiele zusammen mit Freunden 3 gewinnt!")
# In der ersten Reihe und über 3 Spalten
ueberschrift.grid(row=0, column=0, columnspan=3, padx=5, pady=5)


# Um die Spalten und Zeilen des Gitter automatisch an die Fenstergröße anzupaasen
# benötigen wir die folgenden Zeilen. Für jede Zeile/Spalte wird das "Skalier-Gewicht" gesetzt
for j in range(0, 4):
    Grid.rowconfigure(fenster, j, weight=1)
for j in range(0, 3):
    Grid.columnconfigure(fenster, j, weight=1)



# Erzeuge 9 Buttons
for i in range(0, 9):
    # Ein neuer Button :)
    button = Button(fenster, text="?")

    # in die Liste damit
    buttons.append(button)

    # platziere immer 3 Buttons in einer Reihe:
    # 0 -> (0,0)    1 -> (0,1)  2 -> (0,2)
    # 3 -> (1,0)    4 -> (1,1)  3 -> (1,2)
    # ...
    reihe = 1 + int(i / 3)
    spalte = i % 3
    # Die Buttons im Gitter plaxziern. Mit sticky wird festgelegt, dass die Buttons
    # am Rand (E, W, S, N stehen für Himmelsrichtungen und können auch einzeln gesetze werden,
    # also z.B: N oder E+ W) des Containers "kleben" und bei Größenänderung vergrößert werden
    button.grid(row=reihe, column=spalte, padx=5, pady=5, sticky=E + W + S + N)
    # Mithilfe dieses Tricks wird die Gedrückt-Funktion mit dem drückenden Button aufgerufen
    button["command"] = (lambda b1: lambda: buttonGedrueckt(b1))(button)


# Das Ganze sieht im Gitter angeordnet so aus:
# |__ Überschrift __|
# | _?_ | _?_ | _?_ |
# | _?_ | _?_ | _?_ |
# | _?_ | _?_ | _?_ |


fenster.mainloop()
