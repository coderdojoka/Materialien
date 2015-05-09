## Allgemeine Infos f�r Anf�ngertutorial

### Pr�fung der Korrektheit der Aufgaben

Die Erf�llung der Aufgaben wird durch automatische Tests gepr�ft. Dazu ist es f�r eine korrekte L�sung notwendig sich exakt an die
Vorgaben zu halten. Obwohl man durch die Wahl anderer Bezeichner (z.B. Namen f�r Attribute oder Methoden) korrekte Java-Programme erh�hlt,
bleiben die Tests rot.

### Einf�hrende Erkl�rungen

Folgende Aufgaben erl�utern den Umgang mit einem wichtiges Grundger�st der Programmiersprache Java. Java geh�rt zur Familie der objektorientierten Sprachen (kurz: OO). Dabei wird versucht die wahre Welt als eine Objektmodell zu betrachten. So w�rde man ein Haus aus
der Realtit�t als ein Objekt Haus modellieren, welches unter anderem aus weiteren Objekten wie einer T�r oder mehreren Fenstern besteht.
Dabei ist eine vollst�ndige Modellierung nicht m�glich, aber auch erst gar nicht n�tig. So ist es f�r ein Programm m�glicherweise nicht relevant, ob das Haus rechteckig oder quaderf�rmig ist. Im Objektmodell gehen also immer Informationen aus der realen Welt verloren.
Man programmiert nur die Zusammenh�nge, die tats�chlich ben�tigt werden.

In Java sind Objekte zun�chst in Form von Klassen dargestellt. Als Programmierer definiert man dort, wie der Computer sp�ter ein Objekt dieser
Klasse (dazu sagt man "Instanz") zusammenbaut. Im Projekt findest du eine vordefinierte Klasse Person. In den Aufgaben wird diese Klasse
Schritt f�r Schritt um weitere Elemente erg�nzt.

### TODO

Auf Junit Tests hinweisen. Auf Reihenfolge hinweisen. Tests sind durchnummeriert

## Aufgaben

### Aufgabe 1 - Attribute

Rufe die Klasse Person auf und erstelle dort Attribute f�r einen Namen ("name") und das Alter ("alter"). Attribute (oder Instanzvariablen) speichern Inhalte die f�r das Objekt wichtig sind. Damit definieren sie den Zustand. Attribute werden wie folgt definiert:

<Sichtbarkeit> <Typ> <Name>;

Der Name soll vom Typ String sein und das Alter vom Typ int.
Initialisiere den Namen mit "Max". Dies erfolgt mit einer Zuweisung (=);

### Aufgabe 2 - Methode (void)

F�ge eine Methode ("gibNameAus") hinzu, die den Namen der Person auf der Konsole ausgibt. Verwende f�r die Ausgabe die Hilfsklasse Terminal.
Lasse dir ein neues Terminal vom TerminalProvider geben -> TerminalProvider.getTerminal().gebeAufKonsoleAus(....)

### Aufgabe 3 - Methode (int)

Schreibe eine Methode ("getAlter"), welche den Wert des Attributs f�r das Alter zur�ckliefert. Hinweis: Methoden, die den Inhalt ihrer
privaten Instanzvariablen zur�ckliefern werden als "getter" bezeichnet.

### Aufgabe 4 - Konstruktor

Jede Klasse ben�tigt einen spezielle Methode, um Objekte davon anzulegen. Diese werden als Konstruktoren bezeichnet.

[TODO]...

Hinweis: Der erste Test ist schon gr�n, weil jede Klasse automatisch einen Standardkonstruktor hat, der keine Parameter entgegen nimmt.