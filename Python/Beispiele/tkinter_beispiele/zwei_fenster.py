__author__ = 'Mark Weinreuter'

import time
import tkinter as tk


# Funktion die, die Zeit in ms ausgibt
def aktuelle_ms():
    zeit_in_ms = time.time()  # gibt eine Kommazahl: sekunden.millisekunden
    return int(round(zeit_in_ms * 1000))  # auf ganze MS runden


class LeertastenFenster(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)  # Als Fenster initalizieren

        # Alle Komponenten hinzufügen. WICHTIG: self.name bedeutet, dass man dies überall
        # in der Klasse verwenden kann, indem man self.name schreibt => kein global nötig
        self.lbl_info = tk.Label(self)
        self.lbl_info["text"] = "Drücke die Leertaste"
        self.lbl_info.pack()

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.text = tk.Text(self, wrap=tk.WORD)
        self.text.pack()

        # Scrollbar an Textfeld bindund und vice versa
        self.scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)

        # Tastatur-Events registrieren einmalfür gedrückt und einmal für losgelassen
        # Funktioniert bei mir allerdings NICHT zuverlässig
        self.bind("<Key-space>", self.wenn_leertaste_gedrueckt)
        self.bind("<KeyRelease-space>", self.wenn_leertaste_losgelassen)

    def wenn_leertaste_losgelassen(self, event):
        zeit_unterschied = aktuelle_ms() - self.zeit_wenn_unten
        self.text.insert("end", "Leertaste losgelassen:" + str(zeit_unterschied) + "\n")

    def wenn_leertaste_gedrueckt(self, event):
        self.text.insert("end", "Leertaste gedrückt.\n")
        self.zeit_wenn_unten = aktuelle_ms()


class StartFenster(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Beschriftungslabel
        self.lbl_info = tk.Label(self, text="Drücke die Leertaste")
        self.lbl_info.pack()

        # Button, der bei Klick ein neues Fenster öffnet
        self.btn_start = tk.Button(self, text="Neues Fenster", command=self.wenn_btn_start_gedrueckt)
        self.btn_start.pack()

    def wenn_btn_start_gedrueckt(self):
        # self.withdraw() selbst verstecken

        # Ein zweites Fenster erstellen und anzeigen
        self.leertastenFenster = LeertastenFenster()


if __name__ == "__main__":
    app = StartFenster()
    app.mainloop()
