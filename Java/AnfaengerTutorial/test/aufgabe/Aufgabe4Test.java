package aufgabe;

import helper.PersonTestHelper;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;

import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class Aufgabe4Test extends PersonTestHelper {

	@Test
	public void aufgabe4a_personHatKonstruktor() throws Exception {
		Constructor<?>[] constructors = findeKonstruktoren();

		pruefeAnzahlKonstruktoren(constructors);
	}

	@Test
	public void aufgabe4b_konstruktorNimmtGroesseEntgegen() throws Exception {
		Constructor<?> constructors = findeKonstruktoren()[0];

		pruefeKonstruktorParameterTyp(constructors);
	}

	@Test
	public void aufgabe4c_konstruktorGroesseInitialisierung() throws Exception {
		Field field = sucheNachAttributGroesse();

		pruefeObGroesseInitialisiert(field);
	}

}
