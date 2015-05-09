package aufgabe;

import helper.PersonTestHelper;

import java.lang.reflect.Method;

import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class Aufgabe3Test extends PersonTestHelper {

	@Test
	public void aufgabe3a_personHatMethodeGetAlter() throws Exception {
		Method method = sucheNachMethodeGetAlter();

		pruefeObGetAlterExistiert(method);
		pruefeTypVonGetAlter(method);
		pruefeSichtbarkeitGetAlter(method);
	}

	@Test
	public void aufgabe3b_getAlter_KorrekteRueckgabe() throws Exception {
		Method method = sucheNachMethodeGetAlter();

		pruefeRueckgabewert(method);
	}

}
