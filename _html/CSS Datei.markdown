###Das CSS Stylesheet

Mit dem CSS Stylesheet gestaltet man das Erscheinungsbild einer Webseite. Zum Beispiel kann man u.a. folgende Dinge festlegen   
* Schriftart, -größe -farbe  
* Hintergrund   
* Rahmen, Ränder   
* Größe von Bildern   
* …..   

Als erstes erstellen wir eine neue Datei und nennen sie bspw. _tutorial.css_. 
Wichtig ist, dass die Datei mit **.css** endet. 

Dann binden wir unsere .css Datei in unseren HTML Text in den <head> folgendermaßen ein:

`<link href="tutorial.css" rel="stylesheet">`


Damit wir einzelne Elemente in unserem HTML Text ansprechen können, müssen wir sie kennzeichnen. Hierfür gibt es 3 Möglichkeiten:

	1.	eine ID vergeben
	2.	eine Klasse erstellen
	3.	das <tag> benutzen.


###1.	Eine ID vergeben

In unserem aktuellen Beispielcode können wir folgendes sehen:
```
<div id="container_1"> 
		<h1 class="head_1"> Überschrift h1</h1>
		<h2> Überschrift h2</h2>
		<h3> Überschrift h3</h3>
	  </div>
```

* Wir haben einen Container `<div> </div>` , in dem 3 Überschriften stehen.
* Damit wir diesen `<div>` Block manipulieren können, hat er eine ID bekommen:     `id="container_1"`.

**Achtung:** die ID muss innerhalb der spitzen Klammern stehen.

* Dass wir eine ID benutzen wollen, teilen wir der css_Datei mit, in dem wir ein # mit dem Namen der ID setzen .

* Was wir tun wollen, setzen wir in geschweifte Klammern: 
  
          {  
           den Hintergrund grün färben
            }  

```
#container_1{
	background-color: green;
}
```

Das Ergebnis: alles Was in dem `<div>` Container mit der `id="container_1"` steht ist jetzt grün: 

![Überschrift](ueb.png)


 

**Wichtig:** der ID-Name _hier:_ `container_1` kann nur **_EINMAL_** vergeben werden.


###2.	Eine Klasse erstellen


in unserem Beispielcodeschnipsel (oben) sehen wir:

```<h1 class="head_1"> Überschrift h1</h1>```


Wir benutzen jetzt eine _Klasse_ statt einer _ID_. Die Klasse hat den Vorteil, dass sie wiederholt benutzt werden kann. Im _css stylesheet_ wird die Klasse mit einem Punkt (.) eingeführt:

```
.head_1{
	background-color: blue;
	text-align: center;
	color: white;
}
```

Bei der Überschrift 1 ändern wir gleich drei Dinge:  
* die Hintergrundfarbe: blau  
* die Ausrichtung des Textes: zentriert  
* die Schriftfarbe: weiß  



3.	Den `<tag>` Namen benutzen

wir können auch den tag Namen  (hier: `<h2>`) benutzen, und dem direkt eine Eigenschaft zuweisen. Allerdings ändern wir dann die Eigenschaft für alle `<h2>` die auf der Seite vorkommen. (in unserem Beispiel kommt `<h2>` sieben Mal vor).

```
h2{
	color: red;
}
```

`<h2>` soll (überall auf der Seite) rot werden. 

![h2](h2.png)  

 



###4.	Erklärung: margin und padding


wenn ich einen Container habe und darin zu schreiben beginne, wird meine Schrift am linken Rand beginnen.

![padd1](padd1.png)  




deshalb definiere ich mir einen Rand, um einen Außenabstand (margin) zu bekommen. Mein Text beginnt immer noch ganz außen.

![padd1](padd2.png)  
 


Nun benötige zusätzlich noch einen Innenabstand (padding) damit ich meinen Text richtig platzieren kann.


![padd1](padd3.png)  
 



Der `container_2` sieht im HTML Code so aus:

```
<h2>Absatz</h2>
	  <div id ="container_2">
		<p class="p_class">Hinter mir kommt ein
		Seitenumbruch<br>Dann wird der
			Text <b>fett</b> und schließlich <i>kursiv</i>. Der Rest ist <b><i>  fett und kursiv</i></b>. 
	  </div>

```



´container_2´

*	bekommt die Hintergrundfarbe: gelb
*	wird 100 Pixel (px) hoch
*	wird 50% breit
*	erhält einen Rand von 25px
+	ein zusätzliches padding von 40px

**Achtung:** man kann Höhen-, Breitenangaben mit einem 

* festen Wert z.B. 150px oder     
* in Prozentwerten ausdrücken

Unser Container soll die Hälfte der Webseitenbreite einnehmen; deshalb geben wir bei der Breite 50% vor


Der Absatz im container_2 enthält eine eigene Klasse class="p_class". Er bekommt

* rot als Hintergrundfarbe 
* eine Breite von 300px
* eine eigene Schriftgröße von 18pt

![Absatz](absatz.png)

Klassen können mehrfach verwendet werden, deshalb verpassen wir der Liste mit bulletpoints ebenfalls die Klasse  `class="p_class"`.  
D.h. die Liste hat auch die Eigenschaften: roter Hintergrund, 300px breit, Schrift 18pt.

![Bullet](bullet.png)


###5.	Tabelle

die Tabelle hat zwei IDs id="tab1" und "row_1".

```
	  <h2>Tabellen</h2>
	  <div>
		  <table id="tab1" border>
			  <tr>
				<td id="row_1">Zeile 1 /Spalte 1</td>
				<td>Zeile 1 /Spalte 2</td>
			  </tr>
			  <tr>
				<td> Zeile 2 / Spalte 1</td>
				<td> Zeile 2 / Spalte 2</td>
			  </tr>
		  </table>
		</div>
```

* Mit der ersten ID `id="tab1"`  beeinflussen wir die ganze Tabelle, weil sie im `<table>` tag steht. Wir wollen, dass die gesamte Tabelle 30% breit ist und die Schriftgröße 20pt beträgt.
* Mit der zweiten `id="row_1"`  nur die erste Zeile: die erste Zeile soll 100px hoch sein. 

```
    #tab1{
    	    width: 30%;
	   font-size: 20pt;
     }
    #row_1{
	height: 100px;
    }
```



![Tabelle](tabelle.png)

###6.	das Logo

Das Logo hat die `id="logo_dojo"`  
`<img id="logo_dojo" src="Bilder/coderdojo.png" title="Dies ist das Coderdojo Logo">`

und in der _css Datei_ legen wir die Größe auf 100px fest:

```
#logo_dojo{
	height: 100px;
	
}
```


In der css-Datei der HTML Seite wurden folgende Eigenschafte benutzt:

Name                    Aktion                          Werteangabe

background-color	für die Hintergrundfarbe       Text: red oder code: #CB2828
color                   für die Schriftfarbe	       Text: red oder code: #CB2828
font-size               Schriftgröß                    in pt
text-align              Positionierung des Textes      Wert: center (=mittig)
width                   Breite                         in px oder %-Wert
height                  Höhe                           in px oder %-Wert
margin                  äußerer Rand                   in px oder %-Wert
padding                 Innenabstand                   in px oder %-Wert


Unsere gesamte HTML Seite sieht so aus:

![Seite](seite.png)


Der entsprechende HTML Code dazu:

```
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="beschreibung des Inhalts (160 Zeichen)">
	<link href="tutorial.css" rel="stylesheet">
	<title>HTML / CSS Tutorial</title>
  </head>
  <body>
	  <div id="container_1"> 
		<h1 class="head_1"> Überschrift h1</h1>
		<h2> Überschrift h2</h2>
		<h3> Überschrift h3</h3>
	  </div>
	  
	  
	  <h2>Absatz</h2>
	  <div id ="container_2">
		<p class="p_class">Hinter mir kommt ein
		Seitenumbruch<br>Dann wird der
			Text <b>fett</b> und schließlich <i>kursiv</i>. Der Rest ist <b><i>  fett und kursiv</i></b>. 
	  </div>
	 

	 <h2>Listen mit bulletpoint</h2>
	 <div id="container_3">
		<ul class="p_class">
			<li>erste Listenzeile</li>
			<li>zweite Listenzeile</li>
			<li>dritte Listenzeile</li>
		</ul>
	  </div>
	<h2>durchnummerierte Listen</h2>
	  <div id="ol_id">
		<ol>
			<li>erste Listenzeile</li>
			<li>zweite Listenzeile</li>
			<li>dritte Listenzeile</li>
		</ol>
	  </div>

	  <h2>Tabellen</h2>
	  <div>
		  <table id="tab1" border>
			  <tr>
				<td id="row_1">Zeile 1 /Spalte 1</td>
				<td>Zeile 1 /Spalte 2</td>
			  </tr>
			  <tr>
				<td> Zeile 2 / Spalte 1</td>
				<td> Zeile 2 / Spalte 2</td>
			  </tr>
		  </table>
		</div>
		<h2>Links</h2>
		
		<a href="https://coderdojoka.github.io/">Das tolle CoderDojo Karlsruhe</a>
	  <div>
		<h2>Bilder</h2>
		<img id="logo_dojo" src="Bilder/coderdojo.png" title="Dies ist das Coderdojo Logo">
	  </div>	
  
  
  </body>
</html>
```



und die css-Datei:  _tutorial.css_

```
#container_1{
	background-color: green;
}

.head_1{
	background-color: blue;
	text-align: center;
	color: white;
}
h2{
	color: red;
}
#container_2{
	background-color: yellow;
	height: 150px;
	width: 50%;
	margin: 25px;
	padding: 20px;
}

.p_class{
	background-color: red;
	width: 300px;
	font-size: 18pt;
}
#tab1{
	width: 30%;
	font-size: 20pt;
}
#row_1{
	height: 100px;
}
#logo_dojo{
	height: 100px;
	
}
``` 

