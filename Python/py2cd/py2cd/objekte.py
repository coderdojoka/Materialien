__author__ = 'Mark Weinreuter'


class ZeichenbaresObjekt:
    """
    Überklasse für alle zeichenbaren Objekte. Diese haben ein Position (x,y) und eine Farbe.
    """

    def __init__(self, x, y, breite, hoehe, eltern_flaeche, farbe, position_geändert=lambda: None):
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
        :type farbe:tuple[int]
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
        """:type: float """

        self.__y = y
        """:type: float """

        self.__hoehe = hoehe
        """
        Die Höhe der umgebenden Box
        """

        self.__breite = breite
        """
        Die Breite der umgebenden Box
        """

        self.position_geaendert = position_geändert
        """
        Funktion die aufgerufen wird, wenn die Position geändert wurde.
        :type: (None)->None
        """

        # füge das Element zum Elternelement hinzu
        if self._eltern_flaeche is not None:
            self._eltern_flaeche.fuege_hinzu(self)

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
    def abstand_oben(self, oben):
        return self._eltern_flaeche.hoehe - oben

    @abstand_oben.setter
    def abstand_oben(self, oben):
        self.__y = self._eltern_flaeche.hoehe - oben
        self.position_geaendert()

    def position(self):
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

    def lese_welt_position(self):
        x = self.x
        y = self.y

        obj = self._eltern_flaeche

        while obj is not None:
            x += obj.x
            y += obj.y
            obj = obj._eltern_flaeche

        return x, y


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

