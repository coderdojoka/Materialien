# Importiert alle wichtigen pyenguin Befehle
from pyenguin import *

__author__ = 'Mark Weinreuter'

# Fenster mit Größe und Titel erstellen
fenster = Fenster(600, 300, "Hallo Text")

# Ein einfacher Text mit Abstand zum linken oberen Eck: 50x20
text1 = Text("Hallo Welt")
text1.links = 50
text1.oben = 20

# Ein Text kann in einer beliebigen Größe sein
schrift1 = Schrift(24)
text2 = Text("Hallo in groß", schrift1)
text2.links = 50
text2.oben = text1.unten + 20

# Ein Text kann in einer beliebigen Schriftart sein
schrift2 = Schrift(30, "Times New Roman")
text3 = Text("Hallo in noch größer und anderer Schrift", schrift2)
text3.links = 50
text3.oben = text2.unten + 20

# Das Fenster anzeigen
fenster.starten()
