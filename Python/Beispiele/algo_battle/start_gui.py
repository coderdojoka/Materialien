from py2cd import *
from py2cd.farben import *

from algorithmus import Algorithmus
from py2cd_spielfeld import SpielFeld

__author__ = "Mark Weinreuter"

# Der erste Schritt, um ein Spiel zu starten ist immer init() aufzurufen
Spiel.init(640, 480, "dotWars")


def hintergrund(delta):
    delta = int(delta * 1000) % 200

    if delta < 100:
        Spiel.setze_hintergrund_farbe(MATT_GRUEN)
        text.farbe = WEISS
        text2.farbe = SCHWARZ
    else:
        Spiel.setze_hintergrund_farbe(MATT_LILA)
        text.farbe = SCHWARZ
        text2.farbe = WEISS


def aktualisiere_spiel(delta):
   pass


def beenden():
    Spiel.setze_aktualisierung(lambda dt: None)
    text.schrift = Schrift(90)
    text.hintergrund = HELL_GRAU

    if spielfeld.punkte[0] > spielfeld.punkte[1]:
        text.setze_text("Algo 1 gewinnt!")
    else:
        text.setze_text("Algo 2 gewinnt!")

    text.zeige()
    text.zentriere()

    text.nach_vorne()


def spiel_aktualisiere(delta):
    spielfeld.aktualisiere()

    # Texte aktualisieren
    txt_zuege.setze_text("Runde: " + str(spielfeld.zuege_uebersicht[0]))
    txt_spieler1.setze_text("Algo 1: " + str(spielfeld.punkte[0]))
    txt_spieler2.setze_text("Algo 2: " + str(spielfeld.punkte[1]))

    if not spielfeld.laueft_noch():
        beenden()


# Funktion die aufgerufen wird, wenn das Spiel aktualisiert wird (fps mal)
Spiel.setze_aktualisierung(aktualisiere_spiel)

schrift = Schrift(50)
text = Text("Willkommen zur epischen", 0, 150, schrift)
text2 = Text("Schlacht zwischen rot und blau!", 0, 200, schrift)
text.zentriere_horizontal()
text2.zentriere_horizontal()

txt_zuege = Text("Runde: 0", 30, 50, farbe=WEISS)
txt_spieler1 = Text("Algo 1: 0", 30, 70, farbe=WEISS)
txt_spieler2 = Text("Algo 2: 0", 30, 90, farbe=WEISS)


def init_animation():
    farbe1 = BLAU
    dicke1 = 6
    abstand = 10
    spiel_haelfte = Spiel.breite / 2
    end_breite = Spiel.breite - abstand
    end_hoehe = Spiel.hoehe - abstand

    ges_laenge = (end_breite - abstand) * 2 + (end_hoehe - abstand) * 2
    dauer_ms = 2000  # => 5 sec
    ges = ges_laenge / dauer_ms

    a1 = AnimierteLinie((spiel_haelfte, abstand), (abstand, abstand), geschwindigkeit=ges, farbe=farbe1, dicke=dicke1)
    a2 = AnimierteLinie((abstand, abstand), (abstand, end_hoehe), geschwindigkeit=ges, farbe=farbe1, dicke=dicke1)
    a3 = AnimierteLinie((abstand, end_hoehe), (end_breite, end_hoehe), geschwindigkeit=ges, farbe=farbe1, dicke=dicke1)
    a4 = AnimierteLinie((end_breite, end_hoehe), (end_breite, abstand), geschwindigkeit=ges, farbe=farbe1, dicke=dicke1)
    a5 = AnimierteLinie((end_breite, abstand), (spiel_haelfte, abstand), geschwindigkeit=ges, farbe=farbe1, dicke=dicke1)

    ak1 = AnimationenKette([a1, a2, a3, a4, a5])

    farbe2 = ROT
    dicke2 = 2
    a12 = AnimierteLinie((spiel_haelfte, abstand), (abstand, abstand), geschwindigkeit=ges, farbe=farbe2, dicke=dicke2)
    a22 = AnimierteLinie((abstand, abstand), (abstand, end_hoehe), geschwindigkeit=ges, farbe=farbe2, dicke=dicke2)
    a32 = AnimierteLinie((abstand, end_hoehe), (end_breite, end_hoehe), geschwindigkeit=ges, farbe=farbe2, dicke=dicke2)
    a42 = AnimierteLinie((end_breite, end_hoehe), (end_breite, abstand), geschwindigkeit=ges, farbe=farbe2, dicke=dicke2)
    a52 = AnimierteLinie((end_breite, abstand), (spiel_haelfte, abstand), geschwindigkeit=ges, farbe=farbe2, dicke=dicke2)

    ak2 = AnimationenKette([a12, a22, a32, a42, a52])

    farbe3 = GRAU
    dicke3 = 2
    abstand = 20
    spiel_haelfte = Spiel.breite / 2
    end_breite = Spiel.breite - abstand
    end_hoehe = Spiel.hoehe - abstand

    ges_laenge = (end_breite - abstand) * 2 + (end_hoehe - abstand) * 2
    ges = ges_laenge / dauer_ms  # => 2 sec dauer

    a13 = AnimierteLinie((abstand, abstand), (spiel_haelfte, abstand), geschwindigkeit=ges, farbe=farbe3, dicke=dicke3)
    a23 = AnimierteLinie((abstand, end_hoehe), (abstand, abstand), geschwindigkeit=ges, farbe=farbe3, dicke=dicke3)
    a33 = AnimierteLinie((end_breite, end_hoehe), (abstand, end_hoehe), geschwindigkeit=ges, farbe=farbe3, dicke=dicke3)
    a43 = AnimierteLinie((end_breite, abstand), (end_breite, end_hoehe), geschwindigkeit=ges, farbe=farbe3, dicke=dicke3)
    a53 = AnimierteLinie((spiel_haelfte, abstand), (end_breite, abstand), geschwindigkeit=ges, farbe=farbe3, dicke=dicke3)

    ak3 = AnimationenKette([a53, a43, a33, a23, a13])

    anim = Animation(dauer_ms, hintergrund)

    ak1.start()
    ak2.start()
    ak3.start()
    anim.start()

    return ak1, ak2, ak3, anim


ak1, ak2, ak3, anim = init_animation()


def intro_ende():
    text.verstecke()
    text2.verstecke()

    spielfeld.flaeche.zeige()
    Spiel.setze_aktualisierung(spiel_aktualisiere)

    spielfeld.start()


ak3.setze_animation_gestoppt(intro_ende)
Algorithmus.SCHLAF_ZEIT = .001
spielfeld = SpielFeld("zufall", "Zufall1", "liner", "Liner")

txt_spieler1.setze_text(spielfeld.algo1.name)
txt_spieler2.setze_text(spielfeld.algo2.name)

Spiel.registriere_spiel_wird_beendet(spielfeld.beenden)

# Um das Spiel zu starten, muss Spiel.start() aufgerufen werden. Dies sollte immer die letzte Anweisung sein.
Spiel.starten()
