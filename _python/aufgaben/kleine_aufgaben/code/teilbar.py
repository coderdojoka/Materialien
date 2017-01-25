# Zahlen einlesen und in eine Zahl konvertieren
zahl1 = int(input("Gib hier die erste Zahl ein: "))
zahl2 = int(input("Und hier die zweite Zahl ein: "))

# Divisionsrest muss 0 sein => teilbar
if zahl1 % zahl2 == 0:
    print("Die Zahlen sind restlos teilbar")
else:
    print("Die Zahlen sind NICHT restlos teilbar")