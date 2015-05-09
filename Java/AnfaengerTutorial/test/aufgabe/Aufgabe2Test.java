package aufgabe;

import helper.PersonTestHelper;

import java.lang.reflect.Method;

import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class Aufgabe2Test extends PersonTestHelper {

	@Test
	public void aufgabe2a_personHatMethodeDieNamenAusgibt() throws Exception {
		Method method = sucheNachMethodeGibNameAus();

		pruefeObGibNameAusExistiert(method);
		pruefeSichtbarkeitGibNameAus(method);
		pruefeTypVonGibNameAus(method);
	}

	@Test
	public void aufgabe2b_gibNameAus_RuftKonsoleAuf() throws Exception {
		Method method = sucheNachMethodeGibNameAus();
		method.invoke(person);

		pruefeObKonsolenAusgabeAufgerufen();
	}

	@Test
	public void aufgabe2c_gibtNameAus_KorrekteAusgabe() throws Exception {
		pruefeObAusgabeKorrekt();
	}

}
