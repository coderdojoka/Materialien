package util;

import java.util.Optional;

public final class TerminalProvider {

	private static Terminal terminal;

	public static void setTerminal(Terminal newTerminal) {
		terminal = newTerminal;
	}

	public static Terminal getTerminal() {
		Optional<Terminal> result = Optional.of(terminal);
		return result.orElse(new Terminal());
	}

}
