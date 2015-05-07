package aufgabe1;

import helper.PersonTestHelper;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

import org.junit.Test;

public class PersonTest extends PersonTestHelper {

	@Test
	// Aufgabe 1a
	public void personSollEinenNamenHaben() throws Exception {
		Field field = sucheNachAttributName();

		pruefeObNamensAttributExistiert(field);
		pruefeNameTyp(field);
		pruefeNameSichtbarkeit(field);
	}

	@Test
	// Aufgabe 1b
	public void personSollEinAlterHaben() throws Exception {
		Field field = sucheNachAttributAlter();

		pruefeObAlterAttributExistiert(field);
		pruefeAlterTyp(field);
	}

	@Test
	// Aufgabe 1c
	public void attributNameInitialisieren() throws Exception {
		Field field = sucheNachAttributName();

		pruefeObNameGleichMax(field);
	}

	@Test
	// Aufgabe 2
	public void personHatMethodeDieNamenAusgibt() throws Exception {
		Method method = sucheNachMethodeGibNameAus();

		pruefeObGibNameAusExistiert(method);
		pruefeTypVonGibNameAus(method);
	}

	@Test
	// Aufgabe 2 - bitte untere Zeile für Test einkommentieren
	// TODO Methode per Reflection aufrufen
	public void gibNameAus_RuftConsoleAuf() throws Exception {
		// person.gibNameAus();

		pruefeObKonsolenAusgabeAufgerufen();
	}

	@Test
	// Aufgabe 2
	public void gibtNameAus_KorrekteAusgabe() throws Exception {
		pruefeObAusgabeKorrekt();
	}
}
