from py2cd.bild import Bild

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

bf = Bild.lade_bild_aus_datei("testimages/bolt_strike_0001.png", True)

boltAnim = Animation([('testimages/bolt_strike_0001.png', zeit),
                      (Bild.lade_bild_aus_datei('testimages/bolt_strike_0002.png', True), zeit),
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


zeit /=2

blitzAnim = Animation([("sprites/explosion/explosion_0.png", zeit),
                      ("sprites/explosion/explosion_1.png", zeit),
                      ("sprites/explosion/explosion_2.png", zeit),
                      ("sprites/explosion/explosion_3.png", zeit),
                       ("sprites/explosion/explosion_4.png", zeit),
                       ("sprites/explosion/explosion_5.png", zeit),
                       ("sprites/explosion/explosion_6.png", zeit),
                       ("sprites//explosion/explosion_7.png", zeit),
                       ("sprites/explosion/explosion_8.png", zeit),
                       ("sprites/explosion/explosion_9.png", zeit),
                       ("sprites/explosion/explosion_10.png", zeit),
                       ("sprites/explosion/explosion_11.png", zeit),
                       ("sprites/explosion/explosion_12.png", zeit),
                       ("sprites/explosion/explosion_13.png", zeit),
                       ("sprites/explosion/explosion_14.png", zeit),
                       ("sprites/explosion/explosion_15.png", zeit),
                       ("sprites/explosion/explosion_16.png", zeit),
                       ("sprites/explosion/explosion_17.png", zeit),
                       ("sprites/explosion/explosion_18.png", zeit),
                       ("sprites/explosion/explosion_19.png", zeit),
                       ], False)
blitzAnim.start()
blitzAnim.setze_wiederhole(True)
blitzAnim.setze_position(300, 400)
blitzAnim.abstand_unten = 0
blitzAnim.abstand_links = 12



schiff_anim = Animation([("sprites/weltall/Ship/f1.png", zeit),
                         ("sprites/weltall/Ship/f2.png", zeit),
                         ("sprites/weltall/Ship/f3.png", zeit),
                         ("sprites/weltall/Ship/f4.png", zeit)], False)
schiff_anim.start()
schiff_anim.setze_wiederhole(True)
schiff_anim.setze_position(200, 200)



ufo_anim = Animation([("sprites/weltall/Enemy/Example/e_f1.png", zeit),
                         ("sprites/weltall/Enemy/Example/e_f2.png", zeit),
                         ("sprites/weltall/Enemy/Example/e_f3.png", zeit),
                         ("sprites/weltall/Enemy/Example/e_f4.png", zeit)], False)
ufo_anim.start()
ufo_anim.setze_wiederhole(True)
ufo_anim.setze_position(310, 200)






Spiel.registriere_taste_gedrueckt(K_p, lambda a, b: boltAnim.pause())
Spiel.registriere_taste_gedrueckt(K_s, lambda a, b: boltAnim.start())

Spiel.starten()
