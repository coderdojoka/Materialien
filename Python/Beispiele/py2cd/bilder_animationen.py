__author__ = 'Mark Weinreuter'

from py2cd import *

# Der erste Schritt, um ein Spiel zu starten ist immer init() aufzurufen
Spiel.init(640, 480, "Mein Spiel")
# Erstellt ein neues Fenster mit der gegebenen Größe von 640x480 und dem Titel "Mein Spiel"

# Das Bild in den BildSpeicher laden und ihm einen Namen geben: ’scratch’
BildSpeicher.lade_bild("scratch", "bilder/scratch.png")

# Das Bild über seinen Namen holen und anzeigen
bild1 = BildSpeicher.gib_bild("scratch")
bild1.setze_position(250, 100)

# Das Bild (nocheinmal) über seinen Namen holen und anzeigen
bild2 = BildSpeicher.gib_bild("scratch")
bild2.setze_position(200, 300)

bild1.setze_skalierung(2.0)  # Das Bild doppelt so groß zeichnen
bild1.setze_rotation(180)  # um 180°, d.h. auf den Kopf stellen

bild2.aendere_skalierung(.5)  # Ändert die aktuelle! Skalierung um die Hälfte
bild2.aendere_rotation(90)  # Die aktuelle! Rotation um 90°

bild1.rotiere_und_skaliere(180, 2.0)  # Dreht um 180° und skaliert um das 2-fache
bild1.aendere_rotation_und_skalierung(90, 1.2)  # ändert Rotation und Skalierung

# alle diese Bilder gehören zur Animation
# Bilder können über ihren BilderSpeicher-Namen geladen werden
# oder über den Dateipfad!
bilder_liste = [
    "bilder/n1.png",  # über den Dateipfad laden
    "bilder/n2.png",
    "bilder/n3.png",
    "bilder/n4.png",
    "bilder/n5.png",
    "bilder/n6.png",
    "bilder/n7.png"
]

# Eine neue Animation mit unseren Bilder, die endlos wiederholt wird
animation = BildAnimation(bilder_liste, True)
# rechts unten im Eck positionieren
animation.rechts = 20
animation.unten = 20

# Die Animation starten
animation.start()

# ein bestimmtes Bild, hier das 3.te (wir zählen ab 0!) anzeigen
# Hält die Animation an! Wie .stop(), zeigt das ausgewählte Bild an
animation.zeige_bild(2)


# Steuerbefehle, wie bei einem Musikspiler mit:
animation.pause()  # pausieren, .start() macht an der aktuellen Stelle weiter
animation.stop()  # komplett anhalten und verstecken, .start() beginnt von vorne.
animation.start()  # neustarten oder fortsezten


# Hilfsgitter einblenden
Spiel.zeichne_gitter()

# Um das Spiel zu starten, muss Spiel.start() aufgerufen werden. Dies sollte immer die letzte Anweisung sein.
Spiel.starten()
