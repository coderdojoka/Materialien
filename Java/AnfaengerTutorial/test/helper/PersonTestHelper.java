package helper;

import static helper.ReflectionHelper.getField;
import static helper.ReflectionHelper.getMethod;
import static java.lang.reflect.Modifier.PRIVATE;
import static java.lang.reflect.Modifier.PUBLIC;
import static misc.Nachrichten.A1a_FALSCHER_MODIFIER_ATTRIBUT_NAME;
import static misc.Nachrichten.A1a_FALSCHER_TYP_ATTRIBUT_NAME;
import static misc.Nachrichten.A1a_KEIN_ATTRIBUT_NAME;
import static misc.Nachrichten.A1b_FALSCHER_MODIFIER_ATTRIBUT_ALTER;
import static misc.Nachrichten.A1b_FALSCHER_TYP_ATTRIBUT_ALTER;
import static misc.Nachrichten.A1b_KEIN_ATTRIBUT_ALTER;
import static misc.Nachrichten.A1c_NICHT_INITIALISIERT_NAME;
import static misc.Nachrichten.A1d_FALSCHER_MODIFIER_ATTRIBUT_GROESSE;
import static misc.Nachrichten.A1d_FALSCHER_TYP_ATTRIBUT_GROESSE;
import static misc.Nachrichten.A1d_KEIN_ATTRIBUT_GROESSE;
import static misc.Nachrichten.A2_FALSCHER_MODIFIER_NAME;
import static misc.Nachrichten.A2_FALSCHER_TYP_METHODE_NAME;
import static misc.Nachrichten.A2_KEINE_METHODE_NAME;
import static misc.Nachrichten.A3_FALSCHER_MODIFIER_ALTER;
import static misc.Nachrichten.A3_FALSCHER_TYP_METHODE_ALTER;
import static misc.Nachrichten.A3_FALSCHE_RUECKGABE;
import static misc.Nachrichten.A3_KEINE_METHODE_ALTER;
import static misc.Nachrichten.A4a_KEIN_KONSTRUKTUR_ALTER;
import static misc.Nachrichten.A4b_KONSTRUKTUR_FALSCHE_PARAMETERANZAHL;
import static misc.Nachrichten.A4c_KONSTRUKTUR_FALSCHER_PARAMETERTYP;
import static misc.Nachrichten.A4d_GROESSE_NICHT_INITIALISIERT;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import static org.junit.Assert.assertThat;
import static org.mockito.Mockito.doCallRealMethod;
import static org.mockito.Mockito.verify;
import static util.TerminalProvider.setTerminal;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import org.apache.commons.lang3.reflect.FieldUtils;
import org.junit.Before;
import org.junit.runner.RunWith;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.runners.MockitoJUnitRunner;

import util.Terminal;
import aufgabe.Person;

@RunWith(MockitoJUnitRunner.class)
public abstract class PersonTestHelper extends BaseReflectionHelper {

	private static final String EXPECTED_METHOD_GETALTER = "getAlter";
	private static final String EXPECTED_METHOD_GIBNAMEAUS = "gibNameAus";
	private static final String EXPECTED_NAME = "Max";
	private static final String EXPECTED_FIELD_ALTER = "alter";
	private static final String EXPECTED_FIELD_GROESSE = "groesse";
	private static final String EXPECTED_FIELD_NAME = "name";

	protected static final double EXPECTED_GROESSE = 174.3;

	@Mock
	protected Terminal terminal;
	protected Person person;

	@Before
	public void setUp() throws Exception {
		Constructor<?> constructor = findeKonstruktoren()[0];
		if (constructor.getParameterCount() == 1) {
			person = (Person) constructor.newInstance(EXPECTED_GROESSE);
		} else {
			person = (Person) constructor.newInstance();
		}
		setTerminal(terminal);
	}

	protected Field sucheNachAttributName() throws Exception {
		return getField(EXPECTED_FIELD_NAME);
	}

	protected Field sucheNachAttributGroesse() throws Exception {
		return getField(EXPECTED_FIELD_GROESSE);
	}

	protected Field sucheNachAttributAlter() throws Exception {
		return getField(EXPECTED_FIELD_ALTER);
	}

	protected void pruefeNameTyp(Field field) {
		pruefeFieldTyp(field, String.class, A1a_FALSCHER_TYP_ATTRIBUT_NAME);
	}

	protected void pruefeAlterTyp(Field field) {
		pruefeFieldTyp(field, int.class, A1b_FALSCHER_TYP_ATTRIBUT_ALTER);
	}

	protected void pruefeGroesseTyp(Field field) {
		pruefeFieldTyp(field, double.class, A1d_FALSCHER_TYP_ATTRIBUT_GROESSE);
	}

	protected void pruefeObNamensAttributExistiert(Field field) {
		pruefeObAttributExistiert(field, A1a_KEIN_ATTRIBUT_NAME);
	}

	private void pruefeObAttributExistiert(Field field, String message) {
		assertThat(message, field, is(not(nullValue())));
	}

	protected void pruefeObAlterAttributExistiert(Field field) {
		pruefeObAttributExistiert(field, A1b_KEIN_ATTRIBUT_ALTER);
	}

	protected void pruefeObGroesseAttributExistiert(Field field) {
		pruefeObAttributExistiert(field, A1d_KEIN_ATTRIBUT_GROESSE);
	}

	protected void pruefeNameSichtbarkeit(Field field) {
		assertThat(A1a_FALSCHER_MODIFIER_ATTRIBUT_NAME, field.getModifiers(),
				is(PRIVATE));
	}

	protected void pruefeAlterSichtbarkeit(Field field) {
		assertThat(A1b_FALSCHER_MODIFIER_ATTRIBUT_ALTER, field.getModifiers(),
				is(PRIVATE));
	}

	protected void pruefeSichtbarkeitGibNameAus(Method method) {
		assertThat(A2_FALSCHER_MODIFIER_NAME, method.getModifiers(), is(PUBLIC));
	}

	protected void pruefeSichtbarkeitGetAlter(Method method) {
		assertThat(A3_FALSCHER_MODIFIER_ALTER, method.getModifiers(),
				is(PUBLIC));
	}

	protected void pruefeGroesseSichtbarkeit(Field field) {
		assertThat(A1d_FALSCHER_MODIFIER_ATTRIBUT_GROESSE,
				field.getModifiers(), is(PRIVATE));
	}

	protected void pruefeObGibNameAusExistiert(Method method) {
		assertThat(A2_KEINE_METHODE_NAME, method, is(not(nullValue())));
	}

	protected void pruefeObGetAlterExistiert(Method method) {
		assertThat(A3_KEINE_METHODE_ALTER, method, is(not(nullValue())));
	}

	protected Method sucheNachMethodeGibNameAus() throws Exception {
		return getMethod(EXPECTED_METHOD_GIBNAMEAUS);
	}

	protected Method sucheNachMethodeGetAlter() throws Exception {
		return getMethod(EXPECTED_METHOD_GETALTER);
	}

	protected void pruefeTypVonGibNameAus(Method method) {
		pruefeMethodType(method, void.class, A2_FALSCHER_TYP_METHODE_NAME);
	}

	protected void pruefeTypVonGetAlter(Method method) {
		pruefeMethodType(method, int.class, A3_FALSCHER_TYP_METHODE_ALTER);
	}

	protected void pruefeObNameGleichMax(Field field)
			throws IllegalAccessException {
		String readField = (String) FieldUtils.readField(field, person, true);
		assertThat(A1c_NICHT_INITIALISIERT_NAME, readField, is(EXPECTED_NAME));
	}

	protected void pruefeObKonsolenAusgabeAufgerufen() {
		verify(terminal).gebeAufKonsoleAus(Mockito.anyString());
	}

	protected void pruefeObAusgabeKorrekt() throws Exception {
		ArgumentCaptor<String> captor = ArgumentCaptor.forClass(String.class);
		doCallRealMethod().when(terminal)
				.gebeAufKonsoleAus(Mockito.anyString());

		Method method = sucheNachMethodeGibNameAus();
		method.invoke(person);

		verify(terminal).gebeAufKonsoleAus(captor.capture());
		assertThat(captor.getValue(), is(EXPECTED_NAME));
	}

	protected void pruefeRueckgabewert(Method method)
			throws IllegalAccessException, InvocationTargetException {
		int result = (int) method.invoke(person);
		assertThat(A3_FALSCHE_RUECKGABE, result, is(0));
	}

	protected void pruefeAnzahlKonstruktoren(Constructor<?>[] constructors) {
		assertThat(A4a_KEIN_KONSTRUKTUR_ALTER, constructors.length, is(1));
	}

	protected Constructor<?>[] findeKonstruktoren() {
		return Person.class.getConstructors();
	}

	protected void pruefeKonstruktorParameterTyp(Constructor<?> constructors) {
		Class<?>[] parameterTypes = constructors.getParameterTypes();

		assertThat(A4b_KONSTRUKTUR_FALSCHE_PARAMETERANZAHL,
				parameterTypes.length, is(1));
		assertThat(A4c_KONSTRUKTUR_FALSCHER_PARAMETERTYP, parameterTypes[0],
				is(equalTo(double.class)));
	}

	protected void pruefeObGroesseInitialisiert(Field field)
			throws IllegalAccessException {
		double readField = (double) FieldUtils.readField(field, person, true);
		assertThat(A4d_GROESSE_NICHT_INITIALISIERT, readField,
				is(EXPECTED_GROESSE));
	}

}
