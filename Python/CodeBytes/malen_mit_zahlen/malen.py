__author__ = 'Mark Weinreuter'

# 1. Rechteck gefüllt
breite = 10
hoehe = 5

print("Rechteck gefüllt: %dx%d" % (breite, hoehe))
for i in range(0, hoehe):
    print("X" * breite)

print()
print("Rechteck hohl: %dx%d" % (breite, hoehe))

print("X" * breite)
for i in range(0, hoehe-2):
    print("X" + " " * (breite - 2) + "X")
print("X" * breite)


# 3. Dreieck
stufe = 6
print()
print("Dreieck gefüllt:  Stufe %d" % (stufe))

for j in range(0, stufe):
    print((stufe - j-1) * " " + "X" * (1 + 2 * j))

dreieck_breite = 11
dreieck_hoehe = dreieck_breite // 2 + 1
for k in range(0, dreieck_hoehe):
    print(k * " " + (dreieck_breite - 2 * k) * "Y")

for j in range(0, stufe):
    print((j) * " " + "X" * (1 + 2 * (stufe -j -1)))

# 2. Dreieck
stufe = 6
print((stufe) * " " + "X" + " " * (stufe - j))
for j in range(1, stufe):
    print((stufe - j) * " " + "X" + " " * ((j - 1) * 2 + 1) + "X" + " " * (stufe - j))
print("X" * (stufe * 2 + 1))