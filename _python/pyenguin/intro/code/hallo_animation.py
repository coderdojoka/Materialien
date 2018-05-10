__author__ = 'Mark Weinreuter'

from pyenguin import *


# Fenster mit Größe und Titel
fenster = Fenster(400, 400, "Hallo Fenster")

# Generiere eine Liste von Namen. %d wird durch die Zahlen: 1,2 ersetzt
namen_liste = generiere_namen_liste("gegner/schnecke_laufen%d.png", 1, 3)

# Lade alle Bilder auf einmal. Die Bilder kommen mit pyenguin mit! => lade_aus_paket
schluessel = BildSpeicher.lade_aus_paket("schnecke", namen_liste)

b = BildAnimation(schluessel, anzeige_dauer=500, wiederhole=True, skalierung=2)
b.start()

b.zentriere()

fenster.starten()