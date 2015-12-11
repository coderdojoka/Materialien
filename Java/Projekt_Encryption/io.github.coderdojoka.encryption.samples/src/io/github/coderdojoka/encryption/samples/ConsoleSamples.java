package io.github.coderdojoka.encryption.samples;

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

public class ConsoleSamples {
	
	public static void main(String[] args) {
//Ausgabe eines Textes auf der Konsole
System.out.println("Hallo Welt!");

//Ausgabe einer Zahl auf der Konsole
int zahl1 = 42;
System.out.println(zahl1);
double zahl2 = 1.0 / 3.0;
System.out.println(zahl2);

//Eingabe eines Textes mit der Konsole
InputStreamReader stream = new InputStreamReader(System.in);
BufferedReader reader = new BufferedReader(stream);
System.out.print("Wie ist dein Name? ");
try {
	String name = reader.readLine();
	System.out.println("Hallo " + name + "!");
} catch (IOException e) {
	throw new IOError(e);
}

readNumber();
	}
	
	private static void readNumber() {
//Eingabe einer Zahl mit der Konsole
InputStreamReader stream = new InputStreamReader(System.in);
BufferedReader reader = new BufferedReader(stream);
System.out.print("Wie alt bist du? ");
String eingabe = null;
try {
	eingabe = reader.readLine();
	int alter = Integer.parseInt(eingabe);
	System.out.println("Du bist " + alter + " Jahre alt.");
} catch (IOException e) {
	throw new IOError(e);
} catch (NumberFormatException e) {
	System.out.println("Deine Eingabe '" + eingabe + "' ist keine Zahl.");
}
	}

}
