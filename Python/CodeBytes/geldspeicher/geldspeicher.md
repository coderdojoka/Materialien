---
autor: Mark  
version: 1.0  
daturm: 29.07.16  
titel: Der Geldspeicher  
---

Die Aufgabenstellung
====================

Eines Tages stellt Onkel Dagobert fest, dass er sein Notizzettel
verloren hat. Dort hat er das Passwort für seinen Geldspeicher notiert.
Nun hat er Angst davor, dass die bösen Panzerknacker seine Reichtümer
verschleppen und will deshalb sein Geld in Sicherheit bringen.

Onkel Dagobert ist ganz verzweifelt und hofft auf deine Hilfe. Versuche
ein Programm zu schreiben, welches ihm beim Öffnen des Geldspeichers
hilft.

Vorgabe
-------

Daniel Düsentrieb hat ein Hilfsprogramm entwickelt, mit dem du ein
dreistelliges Passwort (nur Ziffern) im Sicherheitsfeld eingeben kannst.
Hierzu musst du das Modul *geldspeicher* importieren und die Methode
`rate_passwort()` mit deinem geratenen Passwort aufrufen.

Vorrausetzungen
---------------

Um diese Aufgabe erfolgreich lösen zu können solltest du dich mit
Schleifen auskennen und die Aufgaben zu -Schleifen und geschachtelten
-Schleifen gemacht haben.

Umsetzung
=========

Überlege dir eine Technik, mit der du möglichst geschickt die richtige
Kombination eingeben kannst.
Um die Aufgabe zu lösen benötigst du die Dateien `geldspeicher.py` und `geldspeicher_test.py`.
Hier der Inhalt von `geldspeicher_test.py`:
    
```{.python include="geldspeicher_test.py"}
Inhalt wird eingefügt.
```

**Hinweis:** Du kannst beliebig viele Falscheingaben ausprobieren.  


Die Methode `rate_passwort()` gibt wahr oder falsch zurück. Außerdem
erscheint die Ausgabe `’Geldspeicher geöffent’`, wenn du die richtige
Kombination gefunden hast.

Onkel Dagobert wird sich in diesem Fall bestimmt erkenntlich zeigen.
