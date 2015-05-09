package aufgabe;

import helper.PersonTestHelper;

import java.lang.reflect.Field;

import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class Aufgabe1Test extends PersonTestHelper {

	@Test
	public void aufgabe1a_personSollEinenNamenHaben() throws Exception {
		Field field = sucheNachAttributName();

		pruefeObNamensAttributExistiert(field);
		pruefeNameTyp(field);
		pruefeNameSichtbarkeit(field);
	}

	@Test
	public void aufgabe1b_personSollEinAlterHaben() throws Exception {
		Field field = sucheNachAttributAlter();

		pruefeObAlterAttributExistiert(field);
		pruefeAlterTyp(field);
		pruefeAlterSichtbarkeit(field);
	}

	@Test
	public void aufgabe1c_attributNameInitialisieren() throws Exception {
		Field field = sucheNachAttributName();

		pruefeObNameGleichMax(field);
	}

	@Test
	public void aufgabe1d_personSollEineGroesseHaben() throws Exception {
		Field field = sucheNachAttributGroesse();

		pruefeObGroesseAttributExistiert(field);
		pruefeGroesseTyp(field);
		pruefeGroesseSichtbarkeit(field);
	}

}
