package simulator;

import simulation.simulator.ElementZustand;

public class BerechneNiederlage {

	public boolean niederlageErreicht(ElementZustand element) {
		return element.getKoordinaten().getX() <= 0;
	}

}
