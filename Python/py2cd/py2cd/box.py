__author__ = 'Mark Weinreuter'


def berechne_groesse2(punkte):
    x = punkte[0][0]
    y = punkte[0][1]
    breite = punkte[0][0]
    hoehe = punkte[0][1]

    for p in punkte:

        if p[0] < x:
            x = p[0]

        if p[0] > breite:
            breite = p[0]

        if p[1] < y:
            y = p[1]

        if p[1] > hoehe:
            hoehe = p[1]

    # größe anpassen
    breite -= x
    hoehe -= y

    return breite, hoehe


class Box:
    """
    Eine einfache Box (Rechteck) mit Position und Breite, Hoehe
    """

    def __init__(self, x, y, breite, hoehe):
        self.x = x
        self.y = y
        self.breite = breite
        self.hoehe = hoehe

    def __str__(self, *args, **kwargs):
        return (self.x, self.y).__str__()