package helper;

import static java.lang.reflect.Modifier.PRIVATE;
import static misc.Nachrichten.A1a_FALSCHER_MODIFIER_ATTRIBUT_NAME;
import static misc.Nachrichten.A1a_FALSCHER_TYP_ATTRIBUT_NAME;
import static misc.Nachrichten.A1a_KEIN_ATTRIBUT_NAME;
import static misc.Nachrichten.A1b_FALSCHER_TYP_ATTRIBUT_ALTER;
import static misc.Nachrichten.A1b_KEIN_ATTRIBUT_ALTER;
import static misc.Nachrichten.A1c_NICHT_INITIALISIERT_NAME;
import static misc.Nachrichten.A2_FALSCHER_TYP_METHODE_NAME;
import static misc.Nachrichten.A2_KEINE_METHODE_NAME;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import static org.junit.Assert.assertThat;
import static org.mockito.Mockito.doCallRealMethod;
import static org.mockito.Mockito.verify;
import static util.TerminalProvider.setTerminal;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

import org.apache.commons.lang3.reflect.FieldUtils;
import org.junit.Before;
import org.junit.runner.RunWith;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.runners.MockitoJUnitRunner;

import util.Terminal;
import aufgabe1.Person;

@RunWith(MockitoJUnitRunner.class)
public class PersonTestHelper {

	@Mock
	protected Terminal terminal;
	protected Person person;

	@Before
	public void setUp() {
		person = new Person();
		setTerminal(terminal);
	}

	protected Field sucheNachAttributName() throws NoSuchFieldException {
		return Person.class.getDeclaredField("name");
	}

	protected void pruefeNameSichtbarkeit(Field field) {
		assertThat(A1a_FALSCHER_MODIFIER_ATTRIBUT_NAME, field.getModifiers(),
				is(PRIVATE));
	}

	protected void pruefeNameTyp(Field field) {
		assertThat(A1a_FALSCHER_TYP_ATTRIBUT_NAME, field.getType(),
				is(equalTo(String.class)));
	}

	protected void pruefeObNamensAttributExistiert(Field field) {
		assertThat(A1a_KEIN_ATTRIBUT_NAME, field, is(not(nullValue())));
	}

	protected void pruefeAlterTyp(Field field) {
		assertThat(A1b_FALSCHER_TYP_ATTRIBUT_ALTER, field.getType(),
				is(equalTo(int.class)));
	}

	protected void pruefeObAlterAttributExistiert(Field field) {
		assertThat(A1b_KEIN_ATTRIBUT_ALTER, field, is(not(nullValue())));
	}

	protected Field sucheNachAttributAlter() throws NoSuchFieldException {
		return Person.class.getDeclaredField("alter");
	}

	protected void pruefeTypVonGibNameAus(Method method) {
		assertThat(A2_FALSCHER_TYP_METHODE_NAME, method.getReturnType(),
				is(equalTo(void.class)));
	}

	protected void pruefeObGibNameAusExistiert(Method method) {
		assertThat(A2_KEINE_METHODE_NAME, method, is(not(nullValue())));
	}

	protected Method sucheNachMethodeGibNameAus() throws NoSuchMethodException {
		return Person.class.getMethod("gibNameAus");
	}

	protected void pruefeObNameGleichMax(Field field)
			throws IllegalAccessException {
		String readField = (String) FieldUtils.readField(field, person, true);
		assertThat(A1c_NICHT_INITIALISIERT_NAME, readField, is("Max"));
	}

	protected void pruefeObKonsolenAusgabeAufgerufen() {
		verify(terminal).gebeAufKonsoleAus(Mockito.anyString());
	}

	protected void pruefeObAusgabeKorrekt() {
		ArgumentCaptor<String> captor = ArgumentCaptor.forClass(String.class);
		doCallRealMethod().when(terminal)
				.gebeAufKonsoleAus(Mockito.anyString());

		// TODO Methode per Reflection aufrufen
		// person.gibNameAus();

		verify(terminal).gebeAufKonsoleAus(captor.capture());
		assertThat(captor.getValue(), is("Max"));
	}

}
