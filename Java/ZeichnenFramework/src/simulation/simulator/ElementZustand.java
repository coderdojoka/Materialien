package simulation.simulator;

import static zeichnen.models.Richtung.VORWAERTS;
import static zeichnen.models.Richtung.invertiereRichtung;
import zeichnen.models.Richtung;
import zeichnen.models.Position;

public class ElementZustand {

	private SimulierbaresElement element;
	private Richtung xRichtung;
	private Richtung yRichtung;

	public ElementZustand(SimulierbaresElement element) {
		this.element = element;
		xRichtung = VORWAERTS;
		yRichtung = VORWAERTS;
	}

	public int getGeschwindigkeit() {
		return element.getSpeed();
	}

	public Position getKoordinaten() {
		return element.getPosition();
	}

	public void bewegeUm(int step) {
		int newX = berechneNeuenWert(step, xRichtung.getValue());
		int newY = berechneNeuenWert(step, yRichtung.getValue());
		getKoordinaten().add(new Position(newX, newY));
	}

	private int berechneNeuenWert(int step, int value) {
		return step * value;
	}

	public Richtung getxRichtung() {
		return xRichtung;
	}

	public Richtung getyRichtung() {
		return yRichtung;
	}

	public void dreheXRichtung() {
		xRichtung = invertiereRichtung(xRichtung);
	}

	public void dreheYRichtung() {
		yRichtung = invertiereRichtung(yRichtung);
	}

}
