package io.github.coderdojoka.encryption;

import io.github.coderdojoka.util.Terminal;

public class Main {

	public static void main(String[] args) {
		Terminal terminal = new Terminal();
		
		//Eingabe des Schlüssels
		int schluessel = terminal.erfrageInt("Schlüssel: ");
		
		//Eingabe des Textes
		String klartext = terminal.erfrageString("Klartext: ");
		String geheimtext = verschluessel(schluessel, klartext);
		
		//Ausgabe des Geheimtextes mit dem terminal
		terminal.println("Geheimtext: " + geheimtext);
	}
	
	//Das Alphabet ist die Menge von Zeichen, die verschlüsselt werden. In diesem Fall
	//die Buchstaben a-z, A-Z und die Zahlen 0-1. Alles andere wird ignoriert und als
	//Klartext an den Geheimtext angehängt.
	private static final char[] alphabet = {
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
			'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
			'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
			'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
	};

	private static String verschluessel(int schluessel, String klartext) {
		//Umwandlung des Strings zu einem Array aus Zeichen
		char[] zeichen = klartext.toCharArray();
		//Anlegen der Variable für den Geheimtext, da dieser Zeichen für Zeichen erstellt wird.
		String geheimtext = "";
		
		//Jedes Zeichen des Klartextes wird einzeln verschlüsselt
		for (int zeichenIndex = 0; zeichenIndex < zeichen.length; zeichenIndex++) {
			//Index des verschlüsselten Zeichens im Alphabet.
			//Wird mit -1 initialisiert, um zu erkennen ob das Zeichen auch gefunden wurde.
			int geheimIndex = -1;
			
			//Jeder Buchstabe des Alphabets wird mit dem aktuellen Zeichen verglichen
			for (int alphabetIndex = 0; alphabetIndex < alphabet.length; alphabetIndex++) {
				if (zeichen[zeichenIndex] == alphabet[alphabetIndex]) {
					//Das Zeichen wurde im Alphabet an der Stelle alphabetIndex gefunden.
					//Das verschlüsselte Zeichen befindet sich schluessel Stellen dahinter.
					geheimIndex = alphabetIndex + schluessel;
					if (geheimIndex >= alphabet.length) {
						//Falls der geheimIndex größer ist als der Array würde es bei einem
						//Zugriff einen Fehler geben.
						geheimIndex = geheimIndex - alphabet.length;
					}
					break;
				}
			}
			
			if (geheimIndex == -1) {
				//Das Zeichen wurde nicht im Alphabet gefunden, also wird es nicht verschlüsselt.
				geheimtext = geheimtext + zeichen[zeichenIndex];
			} else {
				//Das verschlüsselte Zeichen wird an den Geheimtext angehängt.
				geheimtext = geheimtext + alphabet[geheimIndex];
			}
		}
		return geheimtext;
	}

}
