# Materialien
Sammlung von Beispielprogrammen, Übungen etc. Es gibt zwei Branches, dieser hier, der an die Mentoren gerichtet ist, und der 'usb_stick' Branch, der für die Teilnehmer (und deren USB-Sticks) gedacht ist :)

## Scratch
Hier finden sich einige kleine Scratch Programme und Anleitungen.

## Python  
Hier finden sich [Beispiele](Python/Beispiele) und Anleitungen für die Programmierung mit Python. Die Beispiele sind für Python3 ausgelegt. Die aktuelle Python Version ist 3.4/3.5 und sollte installiert werden.
Hinweise zur Installation von Python können in [hier](Installation/installation_python.pdf) gefunden werden.


## Für Mentoren

### LaTeX
Die meisten unserer Materialien sind mit LaTeX erstellt. Deshalb sind im [Vorlagen-Ordner](Vorlagen) LaTeX-Templates zu finden, so dass alle Materialien ein einheitliches Aussehen erhalten (und um uns das Leben einfacher zu machen).
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
Ein Tutorial ist z.B. das Spiel [Zahlenraten](Python/Gelber Gürtel/Aufgaben/Zahlenraten/zahlenraten.pdf).  

Ein Aufgabe ist z.B. [Maler](Python/Roter\ Gürtel/Aufgaben/maler.pdf).
