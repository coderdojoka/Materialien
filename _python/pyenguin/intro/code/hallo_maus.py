# Importiert alle wichtigen pyenguin Befehle
import random

from pyenguin import *

__author__ = 'Mark Weinreuter'

# Fenster mit Größe und Titel erstellen
fenster = Fenster(640, 480, "Hallo Fenster")

# Info-Text in der Mitte anzeigen
text = Text("Klicke um neue Rechtecke zu erzeugen!!", Schrift(30))
text.zentriere()


def bei_maus_klick(x, y, e):
    # Zufällige Position und Größe
    zuf_x = random.randint(0, 600)
    zuf_y = random.randint(0, 600)
    zuf_breite = random.randint(10, 50)
    zuf_hoehe = random.randint(10, 50)

    neues_rechteck = Rechteck(zuf_x, zuf_y, zuf_breite, zuf_hoehe, HELL_GRUEN)


# Wird irgendwo auf das Fenster geklickt, wird die Funktion bei_maus_klick aufgerufen
registriere_maus_geklickt(bei_maus_klick)

# Das Fenster anzeigen
fenster.starten()
