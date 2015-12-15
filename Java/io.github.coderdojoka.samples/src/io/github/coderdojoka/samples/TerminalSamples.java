package io.github.coderdojoka.samples;

import io.github.coderdojoka.util.Terminal;

public class TerminalSamples {

	public static void main(String[] args) {
		//Ausgabe eines Textes auf der Konsole
		Terminal terminal = new Terminal();
		terminal.println("Hallo Welt!");

		//Ausgabe einer Zahl auf der Konsole
		int zahl1 = 42;
		terminal.println(zahl1);
		double zahl2 = 1.0 / 3.0;
		terminal.println(zahl2);
		
		//Eingabe eines Textes mit dem Terminal
		String name = terminal.erfrageString("Wie ist dein Name? ");
		terminal.println("Hallo " + name + "!");
		
		//Eingabe einer Zahl mit dem Terminal
		int alter = terminal.erfrageInt("Wie alt bist du? ");
		terminal.println("Du bist " + alter + " Jahre alt.");
	}

}
