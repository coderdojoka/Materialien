__author__ = 'Mark Weinreuter'

import random

# versteckte Kombination :D
__kombi_gs_v1 = [
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
]

# versteckte Kombination (zufällige ascii a-z)
__kombi_gs_v2 = [
    chr(random.randint(97, 122)),
    chr(random.randint(97, 122)),
    chr(random.randint(97, 122))
]
#print(__kombi_gs_v1)

def teste_passwort(z1, z2, z3):
    """
    Testet die Kombination des Geldspeichers. In dieser Version besteht die Kombination aus Zahlen.
    :param z1: Die erste Ziffer
    :type z1: int
    :param z2: Die zweite Ziffer
    :type z2: int
    :param z3: Die dritte Ziffer
    :type z3: int
    """

    return __test_kombination(z1, z2, z3, __kombi_gs_v1)


def teste_passwort_buchstaben(c1, c2, c3):
    __test_kombination(c1, c2, c3, __kombi_gs_v2)


def __test_kombination(z1, z2, z3, __kombi):

    # alle drei ziffern vergleichen
    if z1 == __kombi[0] and z2 == __kombi[1] and z3 == __kombi[2]:

        # Kombination ist richtig
        print("Gelspeicher geöffnet!")
        return True

    return False
