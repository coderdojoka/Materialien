# -*- coding: utf-8 -*-

# ASCII-Aufgabe

"""
Nachrichten:
"asdf"
"blubkeks"
"banane"

Empfänger:
Horst: 1
Ilse: 2

Prompt: "Habe Post! Wer kriegts?"
> 1
goto 1
Prompt: Zugeordnete Post ausgeben

Aufbau:
1. Briefliste ausgeben
2. Allen den selben Brief zustellen

Zusatz:
- Briefe anzeigen
- Mögliche Empfänger mit Hausnummern ausgeben
"""

briefe = "Brief 1", "Brief 2", "Brief 3"
empfaenger = "Horst", "Ilse", "Hans"
briefkasten = {}

print("Es gibt diese Briefkästen, die so durchnummeriert sind:")
for i in range(0, len(empfaenger)):
	print(i, ":", empfaenger[i])

print()
print("Es gibt Post!")
for brief in briefe:
	hausnummer = input("Zu welcher Hausnummer soll dieser Brief? ")
	hausnummer = int(hausnummer)
	briefkasten[hausnummer] = brief

print("")
print("Alle Briefe wurden zugestellt!")
for i in range(0, len(empfaenger)):
	if i in briefkasten:
		print(empfaenger[i], "hat diesen Brief bekommen:", briefkasten[i])
	else:
		print(empfaenger[i], "hat keinen Brief bekommen")
