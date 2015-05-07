package util;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class CollectionUtil {

	public static <T> List<T> createList() {
		return new ArrayList<T>();
	}

	public static <T, U> Map<T, U> createMap() {
		return new HashMap<T, U>();
	}

	public static <T> void addIfNotContains(List<T> elements, T element) {
		if (!elements.contains(element)) {
			elements.add(element);
		}

	}

}
