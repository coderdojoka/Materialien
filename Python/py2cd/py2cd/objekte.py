__author__ = 'Mark Weinreuter'


class Zeichenbar:
    """
    Überklasse für alle zeichenbaren Objekte. Diese haben ein Position (x,y) und eine Farbe.
    """

    def __init__(self, x, y, breite, hoehe, farbe, eltern_flaeche, position_geändert=lambda: None):
        """
         Ein neues Zeichenbares Objekt mit der gegebenen (Hintergrund-)Farbe und Elternflaeche.
        :param x:
        :type x: float
        :param y:
        :type y: float
        :param breite:
        :type breite: float
        :param hoehe:
        :type hoehe: float
        :param farbe:
        :type farbe:tuple[int]|None
        :param eltern_flaeche:
        :type eltern_flaeche: py2cd.flaeche.ZeichenFlaeche
        :return:
        :rtype:
        """

        self.farbe = farbe
        """:type: tuple[int]"""

        self._eltern_flaeche = eltern_flaeche
        """ :type: py2cd.zf.ZeichenFlaeche"""

        self.__x = x
        """
        Die interne x-Position
        :type: float """

        self.__y = y
        """
        Die interne y-Position
        :type: float """

        self.__hoehe = hoehe
        """
        Die Höhe der umgebenden Box (Rechteck)
        :type:float
        """

        self.__breite = breite
        """
        Die Breite der umgebenden Box
        :type:float
        """

        self.__sichtbar = True
        """ Ob das Objekt gezeichnet werden soll."""

        self.position_geaendert = position_geändert
        """
        Funktion die aufgerufen wird, wenn die Position geändert wurde.
        :type: (None)->None
        """

        # füge das Element zum Elternelement hinzu
        if self._eltern_flaeche is not None:
            self._eltern_flaeche.fuege_hinzu(self)

        # die Position wurde aktualisiert
        self.position_geaendert()

    @property
    def breite(self):
        """
        Die Breite der umgebenden Box
        :return:
        :rtype: float
        """
        return self.__breite

    @property
    def hoehe(self):
        """
        Die Höhe der umgebenden Box
        :return:
        :rtype:float
        """
        return self.__hoehe

    # x, y sind nicht direkt setzbar, da position_geandert sonst immer 2mal aufgerufen würde
    @property
    def x(self):
        """
        Der x-Wert gemessen an der linken unteren Ecke des Elternelementes.
        :return:
        :rtype: float
        """
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def mitte(self):
        return self.x + self.breite / 2, self.y + self.hoehe / 2

    @property
    def abstand_oben(self):
        return self.__y

    @abstand_oben.setter
    def abstand_oben(self, oben):
        self.__y = oben
        self.position_geaendert()

    @property
    def abstand_unten(self):
        return self._eltern_flaeche.hoehe - (self.__y + self.hoehe)

    @abstand_unten.setter
    def abstand_unten(self, unten):
        self.__y = self._eltern_flaeche.hoehe - (unten + self.hoehe)
        self.position_geaendert()

    @property
    def abstand_rechts(self):
        return self._eltern_flaeche.breite - (self.__x + self.breite)

    @abstand_rechts.setter
    def abstand_rechts(self, rechts):
        self.__x = self._eltern_flaeche.breite - (rechts + self.breite)
        self.position_geaendert()

    @property
    def abstand_links(self):
        return self.__x

    @abstand_links.setter
    def abstand_links(self, links):
        self.__x = links
        self.position_geaendert()

    def position(self):
        """
        Gibt die aktuelle Position als Tupel zurück.
        :return:
        :rtype: tuple[float]
        """
        return self.__x, self.__y

    def render(self, pyg_zeichen_flaeche):
        """

        :param pyg_zeichen_flaeche:
        :type pyg_zeichen_flaeche:
        :return:
        :rtype:pygame.Rect
        """
        raise NotImplementedError("render() Methode muss überschrieben werden!")

    def zeichne(self):
        """
        Zeichnet das aktuelle Objekt
        :return:
        :rtype:
        """
        if self.__sichtbar:
            self.render(self._eltern_flaeche.pyg_flaeche)

    def aendere_position(self, x, y):
        """
        Ändert die Position um den gegebenen Wert, d.h: self._x = self._x + x.
        :param x:
        :type x: float
        :param y:
        :type y: float
        :return:
        :rtype:
        """
        self.__x += x
        self.__y += y
        self.position_geaendert()

    def setze_position(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.position_geaendert()

    def zentriere(self):
        d_breite = self._eltern_flaeche.breite - self.breite
        d_hoehe = self._eltern_flaeche.hoehe - self.hoehe
        self.__x = d_breite / 2
        self.__y = d_hoehe / 2
        self.position_geaendert()

    def zentriere_vertikal(self):
        d_hoehe = self._eltern_flaeche.hoehe - self.hoehe
        self.__y = d_hoehe / 2
        self.position_geaendert()

    def zentriere_horizontal(self):
        d_breite = self._eltern_flaeche.breite - self.breite
        self.__x = d_breite / 2
        self.position_geaendert()

    def setze_mitte(self, mitte_x, mitte_y):
        self.__x = mitte_x - (self.breite / 2)
        self.__y = mitte_y - (self.hoehe / 2)
        self.position_geaendert()

    def zentriere_in_objekt(self, objekt):
        if not isinstance(objekt, Zeichenbar):
            raise ValueError("Objekt muss Zeichenbar sein.")

        self.setze_mitte(*objekt.mitte)

    def lese_welt_position(self):
        x = self.x
        y = self.y

        obj = self._eltern_flaeche

        while obj is not None:
            x += obj.x
            y += obj.y
            obj = obj._eltern_flaeche

        return x, y

    def verstecke(self):
        self.__sichtbar = False

    def zeige(self):
        self.__sichtbar = True

    def nach_vorne(self):
        self._eltern_flaeche._zeichenbareObjekte.remove(self)
        self._eltern_flaeche._zeichenbareObjekte.append(self)

    def entferne(self):
        self._eltern_flaeche.entferne(self)

    def punkt_in_rechteck(self, punkt):
        """
        Überprüft, ob der Punkt im umgebenden Rechteckt liegt.
        :param punkt:
        :type punkt:tuple[float]
        :return:
        :rtype:
        """
        start = self.lese_welt_position()

        left = (start[0] <= punkt[0] <= (start[0] + self.breite))
        top = (start[1] <= punkt[1] <= (start[1] + self.hoehe))

        return left and top

    def beruehrt_rechteck(self, r2_links, r2_oben, breite, hoehe):
        r1_rechts = self.x + self.breite
        r1_unten = self.y + self.hoehe

        r2_rechts = r2_links + breite
        r2_unten = r2_oben + hoehe

        # print("Ich: ", self.x, self.y, self.breite, self.hoehe)
        # print("Du: ", r2_links, r2_oben, r2_rechts, r2_unten)

        return not (r2_links > r1_rechts or r2_rechts < self.x or r2_oben > r1_unten or r2_unten < self.y)

    def beruehrt_umgebendes_rechteck(self, zeichenbar):
        return self.beruehrt_rechteck(zeichenbar.x, zeichenbar.y, zeichenbar.breite, zeichenbar.hoehe)

    def _aendere_groesse(self, breite, hoehe):
        self.__breite = breite
        self.__hoehe = hoehe
        self.position_geaendert()


class ZeichenbaresElement(Zeichenbar):
    def __init__(self, x, y, breite, hoehe, farbe, eltern_flaeche=None, position_geaendert=lambda: None):
        if eltern_flaeche is None:
            # falls keine Elternfläche angegeben wurde, dann wir die Haupt-Zeichenfläche verwendet
            from py2cd.spiel import Spiel

            eltern_flaeche = Spiel.standard_flaeche

        super().__init__(x, y, breite, hoehe, farbe, eltern_flaeche, position_geaendert)

    def render(self, pyg_zeichen_flaeche):
        """

        :param pyg_zeichen_flaeche:
        :type pyg_zeichen_flaeche:
        :return:
        :rtype:pygame.Rect
        """
        raise NotImplementedError("render() Methode muss überschrieben werden!")
