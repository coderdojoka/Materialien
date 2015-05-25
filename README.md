# Materialien
Sammlung von Beispielprogrammen, Übungen etc.

## Python  
Hier finden sich [Aufgaben](Python/Aufgaben), [Beispiele](Python/Beispiele) und Anleitungen für die Programmierung mit Python. Die Beispiele sind für Python3 ausgelegt. Die aktuelle Python Version ist 3.4 und sollte installiert werden.
Hinweise zur Installation von Python können in [hier](Installation/installation_python.pdf) gefunden werden.
### py2cd  
[py2cd](Python/py2cd) ist einfaches Zeichen-/Spiele-Framework, dass einen Wrapper um das in Spiele-Framework [pygame](https://pygame.org) bietet. Es ist auf Deutsch geschrieben, so dass die Befehle einfacher und verständlicher benutzt werden können.
Hinweise zur Installation sind [hier](Installation/installation_pygame.pdf) zu finden.


## Für Mentoren

### LaTeX
Die meisten unserer Materialien sind mit LaTeX erstellt. Deshalb sind im [Vorlagen-Ordner](Vorlagen) LaTeX-Templates zu finden, so dass alle Materialien ein einheitliches Aussehen erhalten (und um uns das Leben einfacher zu machen).
Die Vorlage verwendet das in Python geschriebene [Pygments](http://pygments.org/) um Code zu formatieren und muss deswegen installiert sein. Dies kann zum Beispiel über den Python Package Index mittels
```python
pip install Pygments
```
installiert werden (vorrausgestzt Python und [pip](https://pip.pypa.io/en/latest/installing.html) (kommt mit Python 3.4 standartmäßig mit) sind installiert).  

Außerdem muss Latex-Dokument dann mit dem 'shell-escape' Flag kompiliert werden:
```
-shell-escape
```


## Aufgaben
Zur Zeit gibt es noch noch relativ wenige Aufgaben und Tutorials. Dies soll sich in nächster Zeit allerdings ändern :)  
Ein Tutorial ist z.B. das Spiel [Zahlenraten](Python/Aufgaben/zahlenraten.pdf).  

Ein Aufgabe ist z.B. [Maler](Python/Aufgaben/maler.pdf).
