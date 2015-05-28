__author__ = 'Mark Weinreuter'

from unittest.case import TestCase

import pygame

from py2cd.anim import Animation

from py2cd.farben import *
from py2cd.flaeche import neue_pygame_flaeche
from py2cd.linie import Linie
from py2cd.poly import Polygon, AALinien, Linien
from py2cd.rechteck import Rechteck
from py2cd.spiel import Spiel


class PositionTest(TestCase):
    fenster_breite = 640
    fenster_hoehe = 480
    laufzeit = 10
    laufend = 0

    @staticmethod
    def beenden_timer(dt):
        PositionTest.laufend += dt
        if PositionTest.laufzeit < PositionTest.laufend:
            Spiel._ist_aktiv = False

    def setUp(self):
        Spiel.init(PositionTest.fenster_breite, PositionTest.fenster_hoehe, "Test", PositionTest.beenden_timer)

    def dimension_test(self, zeichenbar):
        """

        :param zeichenbar:
        :type zeichenbar:
        :return:
        :rtype:
        """
        print("Test abstand_xy()")
        abstand = 12.534234234235
        stellen = 5

        zeichenbar.abstand_links = abstand
        self.assertAlmostEqual(abstand, zeichenbar.x, stellen)

        zeichenbar.abstand_rechts = abstand
        self.assertAlmostEqual(zeichenbar._eltern_flaeche.breite - abstand - zeichenbar.breite, zeichenbar.x, stellen)

        zeichenbar.abstand_oben = abstand
        self.assertAlmostEqual(abstand, zeichenbar.y, stellen)

        zeichenbar.abstand_unten = abstand
        self.assertAlmostEqual(zeichenbar._eltern_flaeche.hoehe - zeichenbar.hoehe - abstand, zeichenbar.y, stellen)

        print("Done")

        zeichenbar.zentriere()

        print("Teste zentriere()")
        self.assertAlmostEqual((PositionTest.fenster_breite - zeichenbar.breite) / 2, zeichenbar.x, stellen)
        self.assertAlmostEqual((PositionTest.fenster_hoehe - zeichenbar.hoehe) / 2, zeichenbar.y, stellen)
        print("Done.")

    def test1(self):
        r = Rechteck(0, 10, 100.533343343434, 10.3340, BLAU)
        p = Polygon([(20.444, 210.22), (200, 200), (450, 150)], ROT, 1)
        l = Linie((50, 50.67667), (200, 200), (150, 250, 50), 4)
        ll = Linien([(233, 456), (5.55, 2.21)], True, SCHWARZ)
        al = AALinien([(400, 450), (530.3304, 500)], True, GRUEN)
        a = Animation([(neue_pygame_flaeche(400, 400), 10)], True)

        self.dimension_test(r)
        self.dimension_test(p)
        self.dimension_test(l)
        self.dimension_test(ll)
        self.dimension_test(al)
        self.dimension_test(a)
        Spiel.starten()

    def tearDown(self):
        pygame.quit()
