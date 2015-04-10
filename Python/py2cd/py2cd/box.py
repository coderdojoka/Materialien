__author__ = 'Mark Weinreuter'

def umgebendes_rechteck(punkte, e_hoehe):
    r = Box(punkte[0][0], punkte[0][1], punkte[0][0], punkte[0][1])
    for p in punkte:

        if p[0] < r.x:
            r.x = p[0]

        if p[0] > r.breite:
            r.breite = p[0]

        if p[1] < r.y:
            r.y = p[1]

        if p[1] > r.hoehe:
            r.hoehe = p[1]

    # größe anpassen
    r.breite -= r.x
    r.hoehe -= r.y

    r.y = e_hoehe - r.y - r.hoehe
    return r


class Box:
    def __init__(self, x, y, breite, hoehe):
        self.x = x
        self.y = y
        self.breite = breite
        self.hoehe = hoehe

    def __str__(self, *args, **kwargs):
        return (self.x, self.y).__str__()