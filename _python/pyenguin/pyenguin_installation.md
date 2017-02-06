---
title: pyenguin - Installation
layout: page
author: Mark
uid: pg_install
date: 2017-01-24
---

Pyenguin bassiert auf [pygame](http://www.pygame.org).
Deshalb muss als erstes Pygame installiert werden!

## Pygame für Windows

Für Windows kann [hier](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame) die pygame-Installationsdatei heruntergeladen werden.  
**WICHTIG:** Es gibt dort verschiedene Versionen und man muss die richtige Datei auswählen.

Es wird unterschieden nach Python-**VERSION** und Python-**ART** (`32-bit` oder `64-bit`).
Führt man folgenden Befehl in der Windows-Kommandozeile (CMD) aus, erhält man Informationen über die Pythonversion.

```
python --version
```

Der Dateiname setzt sich wie folgt zusammen:

```
pygame‑1.9.3‑cp[VERSION]‑cp[VERSION]m‑[ART].whl
```

**Beispiel:** die Python Version, sind zwei Zahlen hintereinander z.B. `34` für Python 3.4.
Die Art ist z.B. `win32` oder `amd64`.

Für Python 3.5 mit 32-bit ergibt sich also:

```
pygame‑1.9.3‑cp35‑cp35m‑win32.whl
```

Die entsprechende Datei muss nun heruntergeladen werden.


Nun kann man die zuvor heruntergeladene Datei installieren, indem man folgendem Befehl in der Windows-Kommandozeile ausführt.
**WICHTIG**: Der Dateiname muss natürlich der heruntergeladenen Datei entsprechen!

```
pip install --use-wheel pygame‑1.9.3‑cp35‑cp35m‑win32.whl
```

**Tipp:** Hält man im Windows-Explorer die Shift-Taste gedrückt und macht einen
Rechtsklick auf den Ordner, so kann man im Menü den Eintrag:
 `Eingabeaufforderung hier öffnen` auswählen.


## pygame für Linux:

Hier gibt es keinen einheitlichen Weg. Die meisten Distributionen haben in ihren Paketquellen ein pygame-Paket. Wichtig hierbei ist, dass es ein Python3-Paket ist.
Z.B: 

### Arch Linux
```
pacman -S python-pygame
```

#### Ubuntu
Für Ubuntu ist es komplizierter, da pygame für Python3 selbst kompiliert werden muss. Eine Anleitung ist z.B. [hier][ubu] zu finden.

[ubu]: http://askubuntu.com/a/515506


## Pyenguin installieren

Die aktuellste Version kann [hier](https://github.com/coderdojoka/pyenguin/archive/master.zip) heruntergeladen werden.

Zum Installiern muss im entpackten Ordner folgender Befehl ausgeführt werden:

```
python setup.py install
```

**Hinweis Windows:** Unter Windows kann man der Einfachheit halber auch die **run_setup.bat** Windows-Batchdatei ausführen.
 
**Hinweis Linux:** Das Skript muss mit Python 3 ausgeführt werden, also ggf. `python` durch `python3` ersetzen. 


War die Installation erfolgreich, solltest du in der Lage sein die Beispiele aus dem **beispiele**- Ordner zu starten. 