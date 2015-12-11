package io.github.coderdojoka.encryption;

import io.github.coderdojoka.util.Terminal;

public class Main {

	public static void main(String[] args) {
		Terminal terminal = new Terminal();
		
		//Eingabe des Schlüssels
		int schluessel = 3; //Anstatt einer festen Zahl sollte mit dem terminal eine Zahl erfragt werden.
		
		//Eingabe des Textes
		String klartext = "Ich programmiere Java!"; //Anstatt eines festen Textes sollte mit dem terminal
													//ein Text erfragt werden.
		String geheimtext = verschluessel(schluessel, klartext);
		
		//Ausgabe des Geheimtextes mit dem terminal
	}

	private static String verschluessel(int schluessel, String klartext) {
		return klartext;
	}

}
