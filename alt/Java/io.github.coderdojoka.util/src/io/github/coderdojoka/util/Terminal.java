package io.github.coderdojoka.util;

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Diese Klasse stellt einige einfache Methoden zur Ein- und Ausgabe auf der
 * Konsole zur Verf&uuml;gung.
 * 
 * @author Lennart Hensler
 * @version 1.0
 */
public class Terminal {

	private static final String ERROR = "Fehler!";
	private static final String ERROR_INVALID_INT = "Ungültige Integer-Zahl! (Nochmal eingeben) ";
	private static final String ERROR_INVALID_DOUBLE = "Ungültige Double-Zahl! (Nochmal eingeben) ";
	private static final String ERROR_EMPTY_ARRAY = "Ein leeres Array ist nicht erlaubt! (Nochmal eingeben) ";
	private static final String ERROR_EMPTY_LINE = "Eine leere Zeile ist nicht erlaubt! (Nochmal eingeben) ";

	/**
	 * Praezision fuer float-Zahlen. Alle betragsmaessig kleineren Zahlen werden
	 * als 0 ausgegeben.
	 */
	private static final float FLOAT_PRECISION = 1E-8f;
	/**
	 * Praezision fuer double-Zahlen. Alle betragsmaessig kleineren Zahlen
	 * werden als 0 ausgegeben.
	 */
	private static final double DOUBLE_PRECISION = 1E-8d;

	/** Ein Reader-Objekt, das bei allen Lesezugriffen verwendet wird. */
	private final BufferedReader in;

	/**
	 * Erzeugt ein neues Terminal, mit dem man Ein- und Ausgaben auf der Konsole durchführen kann.
	 */
	public Terminal() {
		in = new BufferedReader(new InputStreamReader(System.in));
	}

	/**
	 * Gibt einen Text auf der Konsole aus.
	 */
	public void print(String text) {
		System.out.print(text);
		System.out.flush();
	}

	/**
	 * Gibt einen Text gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(String text) {
		System.out.println(text);
		System.out.flush();
	}

	/**
	 * Gibt einen Wahrheitswert auf der Konsole aus.
	 */
	public void print(boolean wert) {
		print(Boolean.toString(wert));
	}

	/**
	 * Gibt einen Wahrheitswert gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(boolean wert) {
		println(Boolean.toString(wert));
	}

	/**
	 * Gibt ein Zeichen aus.
	 */
	public void print(char zeichen) {
		print(Character.toString(zeichen));
	}

	/**
	 * Gibt ein Zeichen gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(char zeichen) {
		println(Character.toString(zeichen));
	}

	/**
	 * Gibt eine ganze Zahl aus.<br>
	 * Kann auch mit byte und short aufgerufen werden.
	 */
	public void print(long zahl) {
		print(Long.toString(zahl));
	}

	/**
	 * Gibt eine ganze Zahl gefolgt von einem Zeilenumbruch aus.<br>
	 * Kann auch mit byte und short aufgerufen werden.
	 */
	public void println(long zahl) {
		println(Long.toString(zahl));
	}

	/**
	 * Gibt eine Gleitkommazahl aus.
	 */
	public void print(float zahl) {
		print(alsString(zahl));
	}

	/**
	 * Gibt eine Gleitkommazahl gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(float zahl) {
		println(alsString(zahl));
	}

	/**
	 * Gibt eine Gleitkommazahl aus.
	 */
	public void print(double zahl) {
		print(alsString(zahl));
	}

	/**
	 * Gibt eine Gleitkommazahl gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(double zahl) {
		println(alsString(zahl));
	}

	/**
	 * Gibt einen Array von ganzen Zahlen aus.
	 */
	public void print(int[] array) {
		System.out.print("[");
		for (int i = 0; i < array.length; i++) {
			System.out.print(Long.toString((long) array[i]));
			if (i != array.length - 1) {
				System.out.print(", ");
			}
		}
		System.out.print("]");
	}

	/**
	 * Gibt einen Array von ganzen Zahlen gefolgt von einem Zeilenumbruch aus.
	 * 
	 * @param array
	 *            der auszugebende Array.
	 */
	public void println(int[] array) {
		print(array);
		System.out.println();
		System.out.flush();
	}

	/**
	 * Gibt einen Array von ganzen Zahlen aus.
	 */
	public void print(long[] array) {
		System.out.print("[");
		for (int i = 0; i < array.length; i++) {
			System.out.print(Long.toString(array[i]));
			if (i != array.length - 1) {
				System.out.print(", ");
			}
		}
		System.out.print("]");
	}

	/**
	 * Gibt einen Array von ganzen Zahlen gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(long[] array) {
		print(array);
		System.out.println();
		System.out.flush();
	}

	/**
	 * Gibt einen Array von Gleitpunktzahlen aus.
	 */
	public void print(float[] array) {
		System.out.print("[");
		for (int i = 0; i < array.length; i++) {
			System.out.print(alsString(array[i]));
			if (i != array.length - 1) {
				System.out.print(", ");
			}
		}
		System.out.print("]");
	}

	/**
	 * Gibt einen Array von Gleitpunktzahlen gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(float[] array) {
		print(array);
		System.out.println();
		System.out.flush();
	}

	/**
	 * Gibt einen Array von Gleitpunktzahlen aus.
	 */
	public void print(double[] array) {
		System.out.print("[");
		for (int i = 0; i < array.length; i++) {
			System.out.print(alsString(array[i]));
			if (i != array.length - 1) {
				System.out.print(", ");
			}
		}
		System.out.print("]");
	}

	/**
	 * Gibt einen Array von Gleitpunktzahlen gefolgt von einem Zeilenumbruch aus.
	 */
	public void println(double[] array) {
		print(array);
		System.out.println();
		System.out.flush();
	}

	/**
	 * Liest einen Text von der Konsole ein.
	 * 
	 * @return Der gelesene Text.
	 */
	public String leseString() {
		return leseZeile();
	}

	/**
	 * Gibt einen Text aus und erwartet die Eingabe eines Textes.
	 * 
	 * @param frage Der Text der ausgegeben wird, bevor nach der Eingabe gefragt wird.
	 * @return Der eingebene Text.
	 */
	public String erfrageString(String frage) {
		print(frage);
		return leseString();
	}

	/**
	 * Liest einen Wahrheitswert vom Terminal. Die Eingabe "true"
	 * (unabh&auml;ngig von Gro&szlig;-/Kleinschreibung) liefert <code>true</code>, alles
	 * andere <code>false</code>.
	 * 
	 * @return Der eingegebene Wert.
	 */
	public boolean leseBoolean() {
		return Boolean.parseBoolean(leseString());
	}

	/**
	 * Gibt einen Text aus und erwartet die Eingabe eines Wahrheitswerts.
	 * Die Eingabe "true" (unabh&auml;ngig von Gro&szlig;-/Kleinschreibung)
	 * liefert <code>true</code>, alles andere <code>false</code>.
	 * 
	 * @param frage Der Text der ausgegeben wird, bevor nach der Eingabe gefragt wird.
	 * @return der eingegebene Wert.
	 */
	public boolean erfrageBoolean(String frage) {
		print(frage);
		return leseBoolean();
	}

	/**
	 * Liest ein Zeichen vom Terminal. Zeilenumbruche zählen als eigene Zeichen.
	 * 
	 * @return Das gelesene Zeichen.
	 */
	public char leseChar() {
		return erfrageChar("");
	}

	/**
	 * Gibt einen Text aus und erwartet die Eingabe eines Zeichens.
	 * 
	 * @param frage Der Text der ausgegeben wird, bevor nach der Eingabe gefragt wird.
	 * @return Das eingegebene Zeichen.
	 */
	public char erfrageChar(String frage) {
		print(frage);
		String input = leseString();

		if (!input.isEmpty()) {
			return input.charAt(0);
		} else {
			if (frage.isEmpty()) {
				print(ERROR_EMPTY_LINE);
			} else {
				println(ERROR_EMPTY_LINE);
			}
			return erfrageChar(frage);
		}
	}

	/**
	 * Liest eine ganze Zahl vom Terminal.
	 * 
	 * @return Die gelesene Zahl.
	 */
	public int leseInt() {
		return erfrageInt("");
	}

	/**
	 * Gibt einen Text aus und erwartet die Eingabe einer ganzen Zahl.
	 * 
	 * @param frage Der Text der ausgegeben wird, bevor nach der Eingabe gefragt wird.
	 * @return Die eingegebene Zahl.
	 */
	public int erfrageInt(String frage) {
		print(frage);
		String eingabe = leseString();
		try {
			return Integer.parseInt(eingabe);
		} catch (NumberFormatException e) {
			if (frage.isEmpty()) {
				print(ERROR_INVALID_INT);
			} else {
				println(ERROR_INVALID_INT);
			}
			return erfrageInt(frage);
		}
	}

	/**
	 * Liest eine Gleitkommazahl vom Terminal.
	 * 
	 * @return Die gelesene Zahl.
	 */
	public double leseDouble() {
		return erfrageDouble("");
	}

	/**
	 * Gibt einen Text aus und erwartet die Eingabe einer Gleitkommazahl.
	 * 
	 * @param frage Der Text der ausgegeben wird, bevor nach der Eingabe gefragt wird.
	 * @return Die eingegebene Zahl.
	 */
	public double erfrageDouble(String frage) {
		print(frage);
		String eingabe = leseString();
		try {
			return Double.parseDouble(eingabe);
		} catch (NumberFormatException e) {
			if (frage.isEmpty()) {
				print(ERROR_INVALID_DOUBLE);
			} else {
				println(ERROR_INVALID_DOUBLE);
			}
			return erfrageDouble(frage);
		}
	}

	/**
	 * Liest ein Integer Array vom Terminal.
	 * 
	 * @return Das gelesene Array.
	 */
	public int[] leseIntArray() {
		return erfrageIntArray("");
	}

	/**
	 * Gibt einen Text aus und erwartet die Eingabe eines Integer Arrays, wobei die einzelnen
	 * Ganzzahlen durch Kommas getrennt sind.
	 * 
	 * @param frage Der Text der ausgegeben wird, bevor nach der Eingabe gefragt wird.
	 * @return Das gelesene Array.
	 */
	public int[] erfrageIntArray(String frage) {
		print(frage);
		String[] tokens = leseString().split(",");
		if (tokens.length > 0) {
			int[] array = new int[tokens.length];

			try {
				for (int i = 0; i < tokens.length; i++) {
					array[i] = Integer.parseInt(tokens[i].trim());
				}
				return array;
			} catch (NumberFormatException e) {
				if (frage.isEmpty()) {
					print(ERROR_INVALID_INT);
				} else {
					println(ERROR_INVALID_INT);
				}
			}
		} else {
			if (frage.isEmpty()) {
				print(ERROR_EMPTY_ARRAY);
			} else {
				println(ERROR_EMPTY_ARRAY);
			}
		}
		return erfrageIntArray(frage);
	}

	/**
	 * Konvertiert eine Gleitkommazahl in einen String.
	 * 
	 * @param number Die zu konvertierende Zahl.
	 * @return String Darstellung der Zahl.
	 */
	private static String alsString(float number) {
		if (Math.abs(number) < FLOAT_PRECISION) {
			number = 0.0F;
		}
		return Float.toString(number);
	}

	/**
	 * Konvertiert eine Gleitkommazahl in einen String.
	 * 
	 * @param number Die zu konvertierende Zahl.
	 * @return String Darstellung der Zahl.
	 */
	private static String alsString(double number) {
		if (Math.abs(number) < DOUBLE_PRECISION) {
			number = 0.0;
		}
		return Double.toString(number);
	}
	
	private String leseZeile() {
		String zeile;
		try {
			zeile = in.readLine();
		} catch (IOException e) {
			throw new IOError(e);
		}

		if (zeile == null) {
			println(ERROR);
			return null;
		} else {
			return zeile;
		}
	}
}
