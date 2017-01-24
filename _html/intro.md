---
layout: tutorial
type: tutorial
title: HTML / CSS
date: 2017-01-19
author: Norbert
---
Eine HTML Seite besteht immer aus folgendem Grundgerüst:

```
<!DOCTYPE html>
<html lang="de">
  <head>
    <title>Titel</title>         
    <meta charset="utf-8">
    <meta name="description" content="Beschreibung (160 Zeichen)">
    <link href="style.css" rel="stylesheet">  
    </head>
  <body>


  </body>
</html>
```

**Hinweis:** Schreibe dieses Grundgerüst in eine Datei und verwende es für jeden neuen HTML Seitenentwurf.

**Wichtig:** Alle HTML Befehle (tag) beginnen mit einem Befehl der in spitze Klammern gesetzt ist und enden mit einem Befehl, der zusätzlich noch einen Schrägstrich (/) hinter der öffnenden spitzen Klammer hat.
Bsp.:  `<b>Der Text zwischen den beiden tags wird fett angezeigt </b>`



## Seitenkopf `<head> </head>`

Der Kopf enthält:

* Seitentitel: `<title>HTML / CSS Tutorial</title>`
![Seitentitel]({{ site.baseurl }}public/imgs/html/intro/title.png)

* Seiteninformationen: Beschreibung der Seite `<meta name="description" content="Beschreibung (160 Zeichen)">`

* Stylesheets einbinden (Erklärung weiter unten)
`<link href="style.css" rel="stylesheet">  `

<div class="float-container">
  <div class="col50" markdown="1">
  </div>
  <div class="col50" markdown="1">
  </div>
</div>

## Seitenkörper `<body> </body>`
Alles was auf unserer Webseite sichtbar sein soll, steht zwischen den beiden `<body>` tags.

Erklärung einiger HTML-tags. (Vergleiche tag Übersichtstabelle)


### Das `<div>` Element
Das`<div>` Element ist ein Basiselement in HTML. Es ist ein Container, in den man etwas packt und dient zur besseren Strukturierung der Seite und hilft auch bei der Formatierung eines Bereiches. Bsp: Tabelle in einem `<div>`Container:

```
<div>
	<table>
	....
	</table>
</div>
```

### Überschriften:
können automatisch in verschiedenen Schriftgrößen angezeigt werden. Die jeweilige Überschrift wird zwischen `<h>` tags gesetzt (h = engl.: header = Überschrift) wobei dem h jeweils eine Ziffer folgt.  `<h1> </h1>` ist die größte Überschrift.

Dieser HTML-Code:

```
<h1> Überschrift h1</h1>
<h2> Überschrift h2</h2>
<h3> Überschrift h3</h3>
```

Ergibt diese Ausgabe:

<div class="message">
<h1> Überschrift h1</h1>
<h2> Überschrift h2</h2>
<h3> Überschrift h3</h3>
</div>

###	Absatz / Paragraph  `<p> </p>`
Normalen Text schreibt man zwischen die `<p>` tags.

**Wichtig:** Will man im Text eine neue Zeile beginnen, kann man auf dem PC zwar die Enter-Taste drücken. HTML ignoriert dies aber und fährt einfach in der Zeile fort. Deshalb benötigt man hier den `<br>` tag (Manche schreiben auch `<br />`. Beides ist okay.)
**Bitte beachten:** es gibt keinen Endtag für `<br>`.  

Dieser HTML Code:

```
<div>
	<p >Hinter mir kommt ein
	Seitenumbruch<br>Dann wird der Text <b>fett</b> und schließlich <i>kursiv</i>.
	Der Rest ist <b><i> fett und kursiv</i></b>.
	</p>
</div>
```

Ergibt diese Ausgabe:
<div class="message">
	<p >Hinter mir kommt ein
	Seitenumbruch<br>Dann wird der Text <b>fett</b> und schließlich <i>kursiv</i>.
	Der Rest ist <b><i> fett und kursiv</i></b>.
	</p>
</div>


Schaut man die Anzeige genauer an, sieht man, dass einige Wörter **fett**, _kursiv_, **_fett und kursiv_** angezeigt werden.
Die Lösung hierfür finden wir im HTML-Text:
`<b>fett</b>`  	`<i>kursiv</i>`		`<b><i>fett und kursiv</i></b>`

**Wichtig:** bei geschachtelten tags `<b><i>` muss das zuletzt erstellte tag also `<i>` zuerst geschlossen werden.


### Aufzählungen / Listen

Es gibt zwei verschiedene Typen von Aufzählungen:

-	mit durchnummerierten Zeilen
-	oder Zeilen, vor denen ein bulletpoint (•) steht

**Listen mit bulletpoints werden folgendermaßen erstellt:**

```
<ul>
	<li>erste Listenzeile</li>
	<li>zweite Listenzeile</li>
	<li>dritte Listenzeile</li>
</ul>
```

Dies ergibt folgende Ausgabe:
<div class="message">
  <ul>
  	<li>erste Listenzeile</li>
  	<li>zweite Listenzeile</li>
  	<li>dritte Listenzeile</li>
  </ul>
</div>


**Durchnummerierte Listen:**

```
<ol>
	<li>erste Listenzeile</li>
	<li>zweite Listenzeile</li>
	<li>dritte Listenzeile</li>
</ol>
```

Dies ergibt folgende Ausgabe:
<div class="message">
  <ol>
  	<li>erste Listenzeile</li>
  	<li>zweite Listenzeile</li>
  	<li>dritte Listenzeile</li>
  </ol>
</div>

### Tabellen

Tabellen werden benötigt, um Informationen in Zeilen und Spalten zu präsentieren.

```
<table>
	  <tr>
  		<td>Zeile 1 / Spalte 1</td>
  		<td>Zeile 1 /Spalte 2</td>
	  </tr>
	  <tr>
  		<td> Zeile 2 / Spalte 1</td>
  		<td> Zeile 2 / Spalte 2</td>
	  </tr>
</table>
```

<div class="message">
  <table>
  	  <tr>
    		<td>Zeile 1 / Spalte 1</td>
    		<td>Zeile 1 /Spalte 2</td>
  	  </tr>
  	  <tr>
    		<td> Zeile 2 / Spalte 1</td>
    		<td> Zeile 2 / Spalte 2</td>
  	  </tr>
  </table>
</div>


Die Tabelle wird durch die `<table>` tags begrenzt. Innerhalb der Tabelle stehen die `<tr>` tags für die Zeile /Reihe). Dazwischen wird jede Spalte durch `<td>` begrenzt.

### Link auf Webseiten

**Ein Link** auf eine Webseite wird in `<a>` tags (Ankerelemente) eingeschlossen.
Die Webseite, auf die verlinkt wird, wird mit href= eingebunden.  
**Achtung:** die Informationen werden alle in das `<a>` tag geschrieben.
Dahinter kommt der Text unter dem der Link angezeigt werden soll.

```html
<a href="https://coderdojoka.github.io/">Das tolle CoderDojo Karlsruhe</a>
```
wird so angezeigt

<div class="message">
  <a href="https://coderdojoka.github.io/">Das tolle CoderDojo Karlsruhe</a>
</div>

### Bilder einbinden

**Bilder** werden folgendermaßen eingebunden: man teilt HTML mit, dass jetzt ein Bild kommt
`<img>` und die Quelle `src` das Bild selbst bzw. den Pfad, wo das Bild abgelegt ist und den Namen des Bildes.
In unserem Beispiel liegt das Logo im Verzeichnis Bilder, das ein Unterverzeichnis des Ordners ist, in dm das HTML Script liegt.

`<img src="Bilder/coderdojo.png">`

<div class="message">
  <img src="{{ site.baseurl }}/public/imgs/html/intro/coderdojo.png">
</div>

Wenn man die paar Informationen zu HTML (es gibt noch einige mehr) als Webseite anzeigen lässt, sieht es so aus:

 ![Webseite]({{ site.baseurl }}public/imgs/html/intro/site.png)


Man sieht sofort:   

* die Tabelle ist zu klein,   
* das Logo ist zu groß.   

Dieses wird über ein _CSS Stylesheet_ angepasst, mehr dazu im Tutorial über CSS.
