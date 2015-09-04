__author__ = 'Mark Weinreuter'

import pygame
from pygame.constants import *

from py2cd.text import Schrift, Text
from py2cd.farben import *
from py2cd.poly import Polygon

tasten = {}


class Taste:
    standard_farbe_normal = WEISS
    stardard_farbe_gedrueckt = GELB

    def __init__(self, flaeche, zeichen, x, y, punkte, schrift):
        self.zeichen = zeichen
        self.__farbe_normal = Taste.standard_farbe_normal
        self.farbe_gedrueckt = Taste.stardard_farbe_gedrueckt

        self.hintergrund = Polygon(punkte, self.farbe_normal, eltern_flaeche=flaeche)
        self.rand = Polygon(punkte, dicke=2, eltern_flaeche=flaeche)
        self.hintergrund.setze_position(x, y)
        self.rand.setze_position(x, y)

        self.text = Text(zeichen[0], x, y, schrift, eltern_flaeche=flaeche)
        self.text.zentriere_in_objekt(self.hintergrund)

    @property
    def farbe_normal(self):
        return self.__farbe_normal

    @farbe_normal.setter
    def farbe_normal(self, farbe):
        self.__farbe_normal = farbe
        self.hintergrund.farbe = farbe

    def gedrueckt(self):
        self.hintergrund.farbe = self.farbe_gedrueckt

    def losgelassen(self):
        self.hintergrund.farbe = self.farbe_normal


def initialisiere_tasten(flaeche):
    abstand = 6
    groesse = 46

    # Eine Schriftart auswählen
    # Alle verfügbaren Schriften laden
    fonts = pygame.font.get_fonts()
    schrift = None
    schrift_groesse = 30

    # überprüfen ob diese Schriften vorhanden sind
    verfuegbare_schriften = [("freesans", 30), ("comicsansms", 32), ("arial", 28)]
    for f, g in verfuegbare_schriften:
        if f in verfuegbare_schriften:
            schrift = f
            schrift_groesse = g
            break

    # Schriftart festlegen
    tastatur_schrift = Schrift(schrift_groesse, schrift)

    def mache_box(breite=groesse, hoehe=groesse):
        return (0, 0), (breite, 0), (breite, hoehe), (0, hoehe)

    # Die verschiedenen Formen für die Tasten definieren
    normale_box = mache_box()

    box2 = mache_box(groesse * 1.5 + abstand * .5)
    loeschen_box = mache_box(2 * groesse + abstand)
    shift_box = mache_box(1.5 * (groesse) + .5 * abstand)
    caps_box = mache_box(2 * groesse)

    # Enter ist ein bisschen komplizierter zu erzeugen
    enter_hoehe = groesse * 2 + abstand
    enter_breite = groesse * 1.5 + abstand * .5
    unterschied = enter_breite - groesse - abstand

    enter_box = ((0, 0), (enter_breite, 0), (enter_breite, enter_hoehe), (unterschied, enter_hoehe),
                 (unterschied, groesse), (0, groesse))
    leer_box = mache_box(5 * groesse + 4 * abstand)

    finger = [
        [
            [0, 1, 2],
            [0, 1],
            [0, 1],
            [0, 1, 2],
            [0]
        ],
        [
            [3],
            [2],
            [2],
            [3],
            [1]
        ],
        [
            [4],
            [3],
            [3],
            [4],
            []
        ],
        [
            [5, 6],
            [4, 5],
            [4, 5],
            [5, 6],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [4],
        ],
        [
            [],
            [],
            [],
            [],
            [],
        ],
        [
            [7, 8],
            [6, 7],
            [6, 7],
            [7, 8],
            []
        ],

        [
            [9],
            [8],
            [8],
            [9],
            []
        ],
        [
            [10],
            [9],
            [9],
            [10],
            []
        ],
        [
            [11, 12, 13],
            [10, 11, 12, 13],
            [10, 11, 12],
            [11, 12],
            [6]
        ]
    ]

    # Die einzelnen Reihen der Tastatur und deren Tasten erstellen
    erste_reihe = [
        (normale_box, ('^', 94, '°', -1)),
        (normale_box, ('1', K_1, '!', K_EXCLAIM)),
        (normale_box, ('2', K_2, '"', K_QUOTE)),
        (normale_box, ('3', K_3, '§', -1)),
        (normale_box, ('4', K_4, '$', K_DOLLAR)),
        (normale_box, ('5', K_5, '%', -1)),
        (normale_box, ('6', K_6, '%', K_AMPERSAND)),
        (normale_box, ('7', K_7, '/', K_SLASH, '{', K_LEFTBRACKET)),
        (normale_box, ('8', K_8, '(', K_LEFTPAREN)),
        (normale_box, ('9', K_9, ')', K_RIGHTPAREN)),
        (normale_box, ('0', K_0, K_0, '=', K_EQUALS)),
        (normale_box, ('ß', 223, '?', K_QUESTION)),
        (normale_box, ('\'', 314, '`', -1)),
        (loeschen_box, ('<-', K_BACKSPACE))
    ]

    zweite_reihe = [

        (box2, ("Tab", K_TAB)),
        (normale_box, ("q", K_q)),
        (normale_box, ("w", K_w)),
        (normale_box, ("e", K_e)),
        (normale_box, ("r", K_r)),
        (normale_box, ("t", K_t)),
        (normale_box, ("z", K_z)),
        (normale_box, ("u", K_u)),
        (normale_box, ("i", K_i)),
        (normale_box, ("o", K_o)),
        (normale_box, ("p", K_p)),
        (normale_box, ("ü", 252)),
        (normale_box, ("+", K_PLUS)),
        (enter_box, ("", 13))
    ]

    dritte_reihe = [

        (caps_box, ("HOCH", K_CAPSLOCK)),
        (normale_box, ("a", K_a)),
        (normale_box, ("s", K_s)),
        (normale_box, ("d", K_d)),
        (normale_box, ("f", K_f)),
        (normale_box, ("g", K_g)),
        (normale_box, ("h", K_h)),
        (normale_box, ("j", K_j)),
        (normale_box, ("k", K_k)),
        (normale_box, ("l", K_l)),
        (normale_box, ("ö", 246)),
        (normale_box, ("ä", 228)),
        (normale_box, ("#", K_HASH)),
    ]

    vierte_reihe = [

        (shift_box, ("Hoch", K_LSHIFT)),
        (normale_box, ("<", K_LESS)),
        (normale_box, ("y", K_y)),
        (normale_box, ("x", K_x)),
        (normale_box, ("c", K_c)),
        (normale_box, ("v", K_v)),
        (normale_box, ("b", K_b)),
        (normale_box, ("n", K_n)),
        (normale_box, ("m", K_m)),
        (normale_box, (",", K_COMMA, ";", K_SEMICOLON)),
        (normale_box, (".", K_PERIOD, ":", K_COLON)),
        (normale_box, ("-", K_MINUS, "_", K_UNDERSCORE)),
        (shift_box, ("Hoch", K_RSHIFT)),
        (normale_box, ("", -1))
    ]

    fuenfte_reihe = [

        (shift_box, ("Strg", K_LCTRL)),
        (normale_box, ("Fn", -1)),
        (normale_box, ("", -1)),
        (normale_box, ("Alt", K_LALT)),
        (leer_box, ("Leer", K_SPACE)),
        (normale_box, ("AGr", K_MODE)),
        (normale_box, ("", -1)),
        (shift_box, ("Strg", K_RCTRL)),
        (normale_box, ("", -1)),
        (normale_box, ("", -1))
    ]

    alle_tasten = [
        erste_reihe,
        zweite_reihe,
        dritte_reihe,
        vierte_reihe,
        fuenfte_reihe
    ]

    taste_x = abstand
    taste_y = abstand

    transparenz_wert = 120
    finger_farben = [farbe + (transparenz_wert, ) for farbe in
                     [LILA, MATT_BLAU, NEON_GRUEN, HELL_GELB, ORANGE, ORANGE, OLIVE, MATT_GRUEN, MATT_BLAU, MATT_LILA]]
    tastatur = []

    for reihe in alle_tasten:

        tastatur_reihe = []
        for box, zeichen in reihe:

            t = Taste(flaeche, zeichen[::2], taste_x, taste_y, box, tastatur_schrift)
            tastatur_reihe.append(t)

            # alle Tasten registrieren
            for i in zeichen[1::2]:
                if i != -1:
                    print(i)
                    tasten[i] = t

            # Nächste Taste links vondieser Taste
            taste_x += box[1][0] + abstand  # Die zweite Reihe erzeugen

        tastatur.append(tastatur_reihe)

        taste_y += groesse + abstand
        taste_x = abstand

    for i, finger_tasten in enumerate(finger):
        for j, tasten_in_reihe in enumerate(finger_tasten):
            print(tasten_in_reihe)
            for k in tasten_in_reihe:
                print(i, j, tasten_in_reihe)
                tastatur[j][k].farbe_normal = finger_farben[i]
