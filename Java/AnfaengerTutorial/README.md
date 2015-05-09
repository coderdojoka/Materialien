## Allgemeine Infos für Anfängertutorial

### Prüfung der Korrektheit der Aufgaben

Die Erfüllung der Aufgaben wird durch automatische Tests geprüft. Dazu ist es für eine korrekte Lösung notwendig sich exakt an die
Vorgaben zu halten. Obwohl man durch die Wahl anderer Bezeichner (z.B. Namen für Attribute oder Methoden) korrekte Java-Programme erhählt,
bleiben die Tests rot.

### Einführende Erklärungen

Folgende Aufgaben erläutern den Umgang mit einem wichtiges Grundgerüst der Programmiersprache Java. Java gehört zur Familie der objektorientierten Sprachen (kurz: OO). Dabei wird versucht die wahre Welt als eine Objektmodell zu betrachten. So würde man ein Haus aus
der Realtität als ein Objekt Haus modellieren, welches unter anderem aus weiteren Objekten wie einer Tür oder mehreren Fenstern besteht.
Dabei ist eine vollständige Modellierung nicht möglich, aber auch erst gar nicht nötig. So ist es für ein Programm möglicherweise nicht relevant, ob das Haus rechteckig oder quaderförmig ist. Im Objektmodell gehen also immer Informationen aus der realen Welt verloren.
Man programmiert nur die Zusammenhänge, die tatsächlich benötigt werden.

In Java sind Objekte zunächst in Form von Klassen dargestellt. Als Programmierer definiert man dort, wie der Computer später ein Objekt dieser
Klasse (dazu sagt man "Instanz") zusammenbaut. Im Projekt findest du eine vordefinierte Klasse Person. In den Aufgaben wird diese Klasse
Schritt für Schritt um weitere Elemente ergänzt.

### TODO

Auf Junit Tests hinweisen. Auf Reihenfolge hinweisen. Tests sind durchnummeriert

## Aufgaben

### Aufgabe 1 - Attribute

Rufe die Klasse Person auf und erstelle dort Attribute für einen Namen ("name") und das Alter ("alter"). Attribute (oder Instanzvariablen) speichern Inhalte die für das Objekt wichtig sind. Damit definieren sie den Zustand. Attribute werden wie folgt definiert:

<Sichtbarkeit> <Typ> <Name>;

Der Name soll vom Typ String sein und das Alter vom Typ int.
Initialisiere den Namen mit "Max". Dies erfolgt mit einer Zuweisung (=);

### Aufgabe 2 - Methode (void)

Füge eine Methode ("gibNameAus") hinzu, die den Namen der Person auf der Konsole ausgibt. Verwende für die Ausgabe die Hilfsklasse Terminal.
Lasse dir ein neues Terminal vom TerminalProvider geben -> TerminalProvider.getTerminal().gebeAufKonsoleAus(....)

### Aufgabe 3 - Methode (int)

Schreibe eine Methode ("getAlter"), welche den Wert des Attributs für das Alter zurückliefert. Hinweis: Methoden, die den Inhalt ihrer
privaten Instanzvariablen zurückliefern werden als "getter" bezeichnet.

### Aufgabe 4 - Konstruktor

Jede Klasse benötigt einen spezielle Methode, um Objekte davon anzulegen. Diese werden als Konstruktoren bezeichnet.

[TODO]...

Hinweis: Der erste Test ist schon grün, weil jede Klasse automatisch einen Standardkonstruktor hat, der keine Parameter entgegen nimmt.