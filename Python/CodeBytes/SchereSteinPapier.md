---
minted_ausgabe: tmp_latex  
autor: Rafael, Mark  
version: 1.0  
datum: 14.05.16  
keine_sektions_nummern: ja  
titel: CodeBytes - Schere Stein Papier  
---

# Themen:
- `if`-Abfragen. Siehe dazu das Tutorial XY

# Aufgabe:
Donald Duck ist ein schlechter Verlierer. Deswegen will er seinen Enkel
Trick beim Schere-Stein-Papier Spiel immer fertigmachen! Doch wie?

Schließlich kann er doch nicht wissen was Trick wählen wird. Und Donald
ist es eigentlich peinlich, weil er sich einfach nicht merken kann,
womit man Schere, Stein oder Papier schlagen kann. Falls du es auch
vergessen hast, hier ist ein erklärendes Bild:

![Schere-Stein-Papier-Regeln](Schere_Stein_Papier.png){w=.8}

Deine Aufgabe, schreibe ein Programm, dass:

- eine Eingabe einliest, die entweder `Schere`, `Stein`, `Papier` sein sollte
- je nach Eingabe, sollst du die korrekte Antwort geben, um die Eingabe zu besiegen

# Vorüberlegung
- Wie viele verschiedene Eingabemöglichkeiten gibt es?
- Was kannst du bei einer falschen Eingabe tun?

# Beispielabläufe:

```
Was hat Trick für eine Figur: Stein
Du kannst Stein mit Papier schlagen!
```

```
Was hat Trick für eine Figur: Papier
Du kannst Stein mit Schere schlagen!
```

**Hinweis:** `Stein` und `Papier` wurde vom Benutzer eingegeben.
