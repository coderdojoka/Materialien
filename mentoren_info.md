---
author: Mark
layout: page
date: 2017-02-06
title: Infos für Mentoren
---

Die Materialien-Webseite wird mit [Jekyll](https://jekyllrb.com/) erstellt.


## Jekyll Installation
Jekyll benötigt Ruby und kan wie folgt installiert werden:

```
gem install jekyll bundler
```

Nachdem das Materialien Repo geclont wurde sollte einmal

```
bundle install
```

ausgeführt werden.


### Seite lokal anzeigen
Die Seite kann lokal getestet weren, dafür muss man lediglich folgenden Befehl ausführen:

```
bundle exec jekyll serve
```


## Inhalte hinzufügen

Inhalte können in Form von Markdown- oder statischen HTML-Dateien vorliegen.
Jede Markdown Datei benötigt einen Header:

```
---
author: Mark
layout: page
date: 2017-02-06
title: Infos für Mentoren
---

Inhalt...
```

Dieser Header gibt grundlegende Infos wie das zu verwendende Layout und Titel an. 
Es können aber auch beliebige eigene Werte hinzugefügt werden


**Beispiel** wird ein `permalink: test.html` angegeben, so heißt die resultierende Datei
`test.html`, ansonsten wird der Dateiname der Markdowndatei verwendet.


Mehr [Infos](https://jekyllrb.com/docs/frontmatter/).

### Verschiedene Sprachen

Die Unterteilung in verschiedene Programmiersprachen wird mithilfe von sogenannten 
[Collections](https://jekyllrb.com/docs/collections/) realisiert.

Effektiv gibt es die Ordner: `_python`, `_scratch` in die Dateien entsprechend eingefügt werden sollen.
Als Unterordner gibt es dort `aufgaben`, `beispiele`, `tutorials`. 
Diese weiter Aufteilung spiegelt sich später nicht im Namen der resultierenden HTML-Datei wieder.
Liegt einen Datei z.B. unter `_python/aufgaben/einfach/test.md` wird daraus `python/test.html`. 

**WICHTIG:** Der Dateiname der Markdown-Dateien muss also eindeutig sein oder mittels `permalink` geändert werden!
