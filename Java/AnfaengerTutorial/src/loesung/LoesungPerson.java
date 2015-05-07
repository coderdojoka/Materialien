package loesung;

import util.TerminalProvider;

public class LoesungPerson {

	private String name = "Max";
	private int alter;

	public void gibNameAus() {
		TerminalProvider.getTerminal().gebeAufKonsoleAus("Max");
	}

}
