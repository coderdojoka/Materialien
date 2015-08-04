from geldspeicher import rate_passwort

# Versuch das Passwort zu raten: 123 -> False/True
treffer = rate_passwort(1, 2, 3)
print(treffer) # Gibt True oder False aus

# Hier könnte deine Lösung stehen
for z1 in range(10):
    for z2 in range(10):
        for z3 in range(10):
            treffer=rate_passwort(z1,z2,z3)
            if treffer:
                print(z1,z2,z3)
                print(treffer)
