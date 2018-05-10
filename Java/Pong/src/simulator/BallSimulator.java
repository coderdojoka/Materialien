package simulator;

import simulation.simulator.ElementZustand;
import simulation.simulator.Simulator;
import zeichnen.Schlaeger;
import zeichnen.fenster.FensterMitButtons;

public class BallSimulator implements Simulator {

	private BerechneKollisionMitWand kollisionMitWand;
	private BerechneKollisionMitSchlaeger kollisionMitSchlaeger;
	private BerechneNiederlage berechneNiederlage;
	private FensterMitButtons frame;

	public BallSimulator(Schlaeger schlaeger, FensterMitButtons frame) {
		this.frame = frame;
		kollisionMitWand = new BerechneKollisionMitWand();
		kollisionMitSchlaeger = new BerechneKollisionMitSchlaeger(schlaeger);
		berechneNiederlage = new BerechneNiederlage();
	}

	@Override
	public void simuliereElement(ElementZustand element) {
		kollisionMitWand.aktualisiereElement(element);
		kollisionMitSchlaeger.aktualisereElement(element);
		pruefeNiederlage(element);
	}

	private void pruefeNiederlage(ElementZustand element) {
		if (berechneNiederlage.niederlageErreicht(element)) {
			frame.zeigeNachrichtAn("Du hast leider verloren :(");
			frame.stoppeSimulation();
		}
	}
}
