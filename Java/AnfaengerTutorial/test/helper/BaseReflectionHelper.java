package helper;

import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class BaseReflectionHelper {

	protected <T> void pruefeFieldTyp(Field field, Class<T> clazz, String message) {
		assertThat(message, field.getType(), is(equalTo(clazz)));
	}

	protected <T> void pruefeMethodType(Method method, Class<T> clazz, String message) {
		assertThat(message, method.getReturnType(), is(equalTo(clazz)));
	}

}
