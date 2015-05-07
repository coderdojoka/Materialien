package zeichnen.models;

public enum Richtung {
	VORWAERTS(1), RUCKWARTS(-1);

	private int value;

	private Richtung(int value) {
		this.value = value;
	}

	public int getValue() {
		return value;
	}

	public static Richtung invertiereRichtung(Richtung direction) {
		if (VORWAERTS.equals(direction)) {
			return RUCKWARTS;
		}
		return VORWAERTS;
	}

}
