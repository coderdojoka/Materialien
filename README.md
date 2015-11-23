# Materialien
Sammlung von Beispielprogrammen, Übungen etc. Es gibt zwei Branches, diesen hier,
 der an die Mentoren gerichtet ist und der 'usb_stick' Branch, der für die Teilnehmer (und deren USB-Sticks) gedacht ist :)

## Scratch
Hier finden sich einige kleine Scratch Programme und Anleitungen.

## Python  
Hier finden sich [Beispiele][bsp] und Anleitungen für die Programmierung mit Python. Die Beispiele sind für Python3 ausgelegt. Die aktuelle Python Version ist 3.4/3.5 und sollte installiert werden.
Hinweise zur Installation von Python können in [hier][python_install] gefunden werden.


## Für Mentoren

### LaTeX
Die meisten unserer Materialien sind mit LaTeX erstellt. Deshalb sind im [Vorlagen-Ordner][vorlagen] LaTeX-Templates zu finden,
 so dass alle Materialien ein einheitliches Aussehen erhalten (und um uns das Leben einfacher zu machen).
Die Vorlage verwendet das in Python geschriebene [Pygments](http://pygments.org/) um Code zu formatieren und muss deswegen installiert sein. Dies kann zum Beispiel über den Python Package Index mittels
```python
pip install Pygments
```
installiert werden (vorrausgesetzt Python und [pip](https://pip.pypa.io/en/latest/installing.html) sind installiert).  

Außerdem müssen Latex-Dokumente mit dem 'shell-escape' Flag kompiliert werden (dies kann man z.B. in den TexMaker-Einstellungen eintragen):
```
latex ... -shell-escape
```


## Aufgaben
Zur Zeit gibt es noch noch relativ wenige Aufgaben und Tutorials. Dies soll sich in nächster Zeit allerdings ändern :)  
Ein Tutorial ist z.B. das Spiel [Zahlenraten](z_raten).  

Ein Aufgabe ist z.B. [Maler][maler].


[python_install]: https://github.com/coderdojoka/Materialien/raw/master/Installation/installation_python.pdf
[vorlagen]: https://github.com/coderdojoka/Materialien/raw/master/Vorlagen
[bsp]: https://github.com/coderdojoka/Materialien/raw/master/Python/Beispiele
[z_raten]: https://github.com/coderdojoka/Materialien/raw/master//Python/Grundlagen/Aufgaben/Zahlenraten/zahlenraten.pdf
[maler]: https://github.com/coderdojoka/Materialien/raw/master/Python/Fortschritte/Aufgaben/maler.pdf