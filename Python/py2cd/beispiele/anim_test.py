__author__ = 'Mark Weinreuter'

from py2cd.spiel import *
from py2cd.anim import Animation


def aktualiserungs_funktion(t):
    pass


Spiel.init(400, 400, "Hallo Animation", aktualiserungs_funktion)
HINTER_GRUND = (100, 50, 50)

zf = Spiel.gib_zeichen_flaeche()
zf.farbe = HINTER_GRUND

zeit = 1000 / 11
Spiel.fps = 30

bf = ZeichenFlaeche.lade_bild_aus_datei("testimages/bolt_strike_0001.png", True)

boltAnim = Animation([('testimages/bolt_strike_0001.png', zeit),
                      (ZeichenFlaeche.lade_bild_aus_datei('testimages/bolt_strike_0002.png', True), zeit),
                      ('testimages/bolt_strike_0003.png', zeit),
                      ('testimages/bolt_strike_0004.png', zeit),
                      ('testimages/bolt_strike_0005.png', zeit),
                      ('testimages/bolt_strike_0006.png', zeit),
                      ('testimages/bolt_strike_0007.png', zeit),
                      ('testimages/bolt_strike_0008.png', zeit),
                      ('testimages/bolt_strike_0009.png', zeit),
                      ('testimages/bolt_strike_0010.png', zeit)])

boltAnim.start()
boltAnim.setze_wiederhole(True)
boltAnim.setze_position(200, 250)
boltAnim.abstand_oben = 0
boltAnim.abstand_rechts = Spiel.breite - boltAnim.breite - 10
boltAnim.zentriere_horizontal()
zeit = 1000 / 6
fireAnim = Animation([("testimages/flame_a_0001.png", zeit),
                      ("testimages/flame_a_0002.png", zeit),
                      ("testimages/flame_a_0003.png", zeit),
                      ("testimages/flame_a_0004.png", zeit),
                      ("testimages/flame_a_0005.png", zeit),
                      ("testimages/flame_a_0006.png", zeit)], False)
fireAnim.start()
fireAnim.setze_wiederhole(True)
fireAnim.setze_position(200, 200)
fireAnim.abstand_unten = 0
fireAnim.abstand_links = 12
fireAnim.zentriere_vertikal()

Spiel.registriere_taste_gedrueckt(K_p, lambda a, b: boltAnim.pause())
Spiel.registriere_taste_gedrueckt(K_s, lambda a, b: boltAnim.start())

Spiel.starten()
