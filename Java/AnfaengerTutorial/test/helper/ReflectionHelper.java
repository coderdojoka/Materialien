package helper;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

import aufgabe.Person;

public final class ReflectionHelper {

	public static Field getField(String name) throws Exception {
		return Person.class.getDeclaredField(name);
	}

	public static Method getMethod(String name) throws Exception {
		return Person.class.getDeclaredMethod(name);
	}

}
