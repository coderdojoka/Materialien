
class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class MitName():
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class PunktMitName(Punkt, MitName):
    def __init__(self, x, y, name):
        Punkt.__init__(self, x, y)
        MitName.__init__(self, name)


class MitNamePunkt(MitName, Punkt):
    def __init__(self, x, y, name):
        Punkt.__init__(self, x, y)
        MitName.__init__(self, name)


p1 = Punkt(5, 10)
p2 = Punkt(5, 10)
p3 = Punkt(10, 5)

print("Sind die Punkte p1 und p2 gleich?", p1 == p2)
print("Sind die Punkte p2 und p3 gleich?", p2 == p3)
print()


a = MitName("Hallo")
b = MitName("Hallo")
c = MitName("Welt")

print("Sind die MitName a und b gleich?", a == b)
print("Sind die MitName b und c gleich?", b == c)
print()

e = PunktMitName(5, 10, "Hallo")
f = PunktMitName(5, 10, "Welt")

g = MitNamePunkt(5, 10, "Hallo")
h = MitNamePunkt(5, 10, "Welt")


print("Sind die PunktMitName gleich?", e == f)
print("Sind die MitNamePunkt gleich?", g == h)
