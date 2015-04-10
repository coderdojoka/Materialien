__author__ = 'Mark Weinreuter'


class ZeichenbaresObjekt:
    """
    Überklasse für alle zeichenbaren Objekte. Diese haben ein Position (x,y) und eine Farbe.
    """

    def __init__(self, farbe, eltern_flaeche, x=0, y=0):
        """

        :param farbe:
        :type farbe:tuple[int]
        :param x:
        :type x: int
        :param y:
        :type y: int
        :return:
        :rtype:
        """
        self.farbe = farbe
        """:type: tuple[int]"""

        self._eltern_flaeche = eltern_flaeche
        """ :type: py2cd.zf.ZeichenFlaeche"""

        self.__x = x
        """:type: float """

        self.__y = 0
        """:type: float """

        self.position_geaendert = lambda: None
        """
        Funktion die aufgerufen wird, wenn die Position geändert wurde.
        :type: (None)->None
        """

        self.dimension = self.berechne_groesse()
        """:type: Box"""

        # füge das Element zum Elternelement hinzu
        if self._eltern_flaeche is not None:
            self._eltern_flaeche.fuege_hinzu(self)


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
        return self._eltern_flaeche.dimension.hoehe - self.dimension.hoehe - self.__y

    @property
    def x_intern(self):
        """
        Der x-Wert gemessen an der linken oberen Ecke des Elternelementes.
        :return:
        :rtype: float
        """
        return self.__x

    @x_intern.setter
    def x_intern(self, x):
        self.__x = x

    @property
    def y_intern(self):
        return self.__y

    @y_intern.setter
    def y_intern(self, y):
        self.__y = self._eltern_flaeche.dimension.hoehe - (y + self.dimension.hoehe)

    def render(self, pyg_zeichen_flaeche):
        """

        :param pyg_zeichen_flaeche:
        :type pyg_zeichen_flaeche:
        :return:
        :rtype:pygame.Rect
        """
        raise NotImplementedError("render() Methode muss überschrieben werden!")

    def berechne_groesse(self):
        raise NotImplementedError("berechne_groesse muss überschrieben werden!")

    def zeichne(self):
        """
        Zeichnet das aktuelle Objekt
        :return:
        :rtype:
        """
        self.render(self._eltern_flaeche._pyg_flaeche)

    def setze_eltern_flaeche(self, flaeche):
        """

        :param flaeche:
        :type flaeche:py2cd.flaeche.ZeichenFlaeche
        :return:
        :rtype:
        """

        # alte position speichern
        old_x = 0
        old_y = 0

        if self._eltern_flaeche is not None:
            old_x = self.x_intern
            old_y = self.y_intern

        self._eltern_flaeche = flaeche

        # die alte position auf der neuen setzen
        if flaeche is not None:
            self.x_intern = old_x
            self.y_intern = old_y

            self.zeichne()


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
        self.x_intern += x
        self.y_intern = self.y + y  # invertiertes Koordinatensystem bezüglich y!
        self.position_geaendert()

    def setze_position(self, x=0, y=0):
        self.__x = x
        self.y_intern = y
        self.position_geaendert()

    def zentriere(self):

        d_breite = self._eltern_flaeche.breite - self.dimension.breite
        d_hoehe = self._eltern_flaeche.hoehe - self.dimension.hoehe
        self.__x = d_breite / 2
        self.y_intern = d_hoehe / 2
        self.position_geaendert()

    def lese_welt_position(self):
        x = self.x_intern
        y = self.y_intern

        obj = self._eltern_flaeche

        while obj is not None and obj.dimension is not None:
            x += obj.x_intern
            y += obj.y_intern
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
        print(punkt, "start", start, self.dimension)
        left = (start[0] <= punkt[0] <= (start[0] + self.dimension.breite))
        top = (start[1] <= punkt[1] <= (start[1] + self.dimension.hoehe))

        return left and top


