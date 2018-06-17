---
layout: tutorial  
title: Dateisystem
author: Mark
date: 2017-03-03
uid: filesystem
topic: advanced
type: tutorial
tags: [t_os]
level: l5
---

Ein Computer speichert Informationen in Dateien. Dateien sind in Ordnern gruppiert.
Ordner können sowohl Unterordner als auch Dateien enthalten.
Dateien sind in der Regel mit einer Dateiendung versehen, die den Typ der Datei angibt, z.B: `txt`für eine Textdatei.

## Eine Datei finden

Auf einem Computer sind sehr viele Dateien gespeichert, um eine konkrete Datei zu finden
muss man den Dateinamen und den Ordnerpfad dahin kennen.
Der Ordnerpfad zusammen mit dem Dateinamen ergibt den Dateipfad.
Mithilfe des Dateipfads ist eine Datei eindeutig zu finden.

### Beispiel

![Ein Beispielordner](/_assets/imgs/ordner1.png)

Die Datei heißt `namen.txt` und liegt unter `/home/coderdojo/mein_ordner/`,
der Dateipfad lautet also `/home/coderdojo/mein_ordner/namen.txt`.

## Ordnerpfad

Der Ordnerpfad gibt die Reihenfolge aller Ordner an, die man öffnen muss, um zu einer Datei zu gelangen. Die Ordnernamen sind 
dabei mit `/`  (unter Linux und Mac) bzw. u.U. auch mit `\` (unter Windows) getrennt.

Im obigen Beispiel ist der erste Ordner folglich `home`, darin liegt der Ordner `coderdojo`, darin liegt der Ordner `mein_ordner`.

## Absolute Pfade

Um nun in Python eine Datei zum lesen oder schreiben zu finden kann
man den Dateipfad angeben, also alle Ordner und den Dateinamen
spezifizieren. Dies nennt man auch einen absoluten Pfad angeben.

```python
datei = open("/home/coderdojo/mein_ordner/namen.txt")
inhalt = datei.read()
# ...
```

## Relative Pfade

In den meisten Fällen will man allerdings nicht den absoluten Pfad angeben, oder weiß diesen gar nicht! In diesen Fällen hilft ein relativer Pfad weiter.

Führt man ein Programm aus so führt man dies von deinem bestimmten Startpunkt irgendwo im Dateisystem aus. Der Startpunkt ist in den meisten Fällen der Ordnerpfad, indem das Pythonprogramm liegt, dass ausgeführt wird.
Ein relativer Pfad gibt den Pfad von dem Startpunkt zur gewünschten Datei an.

### Beispiel

Wir befinden uns immer noch im Ordner `/home/coderdojo/mein_ordner/` und wollen das Bild `bild1.png` im `bilder`-Ordner öffnen.

![Ein zweiter Beispielordner](/_assets/imgs/ordner2.png)

Der absolute Pfad für dieses Bild ist `/home/coderdojo/mein_ordner/bilder/bild1.png`. Unser Startpunkt ist `/home/coderdojo/mein_ordner/`. Der Unterschied ist also nur noch `bilder/bild1.png`. Dies ist der relative Pfad!

```python
# Wir sind in /home/coderdojo/mein_ordner/
datei = open("bilder/bild1.png")
# ...
```

> Ein absoluter Pfad einer Datei gibt die ganze Ordnerstruktur an, in der die Datei liegt
>
> Ein relativer Pfad gibt, ausgehend von einem Startordnerpfad, den Pfad zu der gewünschten Datei an.
> Der Startordnerpfad zusammen mit dem relativen Pfad ergibt den absoluten Pfad!

### Mit Relativen Pfaden navigieren

Angenommen wir sind im Ordner `/home/coderdojo/mein_ordner/bilder/` und wollen nun die Datei
`/home/coderdojo/mein_ordner/namen.txt` öffnen. Die Datei liegt nicht im Ordner `bilder` sondern,
im oberen Ordner `/home/coderdojo/mein_ordner/` also eine Ordnerebene tiefer.

Um eine Ordnerebene tiefer zu gelangen kann man `../` verwenden. Konkret kommen wir im obigen 
Beispiel zur Datei `namen.txt` über den relativen Pfad `../namen.txt`

## Mit Python das Dateisystem modifizieren

### Ordner anlegen

```python
import os

# neuen Ordner relativ anlegen
os.mkdir("neuer_ordner")

# Ordner löschen, Ordner muss leer sein!!!
os.rmdir("neuer_ordner")

# Ordner + Unterordner anlegen
os.mkdir("neuer_ordner")
os.mkdir("neuer_ordner/ordner2")

# Nicht leeren Ordner löschen
import shutil
shutil.rmtree('/folder_name')

# Einen Ordner samt Inhalt verschieben neuer_ordner wird heisst_jetzt_so
shutil.move('neuer_ordner', 'heisst_jetzt_so')
```