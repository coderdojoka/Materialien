package loesung;

import util.TerminalProvider;

public class Person {

	private String name = "Max";
	private int alter;
	private double groesse;

	public Person(double groesse) {
		this.groesse = groesse;
	}

	public void gibNameAus() {
		TerminalProvider.getTerminal().gebeAufKonsoleAus(name);
	}

	public int getAlter() {
		return alter;
	}

}
