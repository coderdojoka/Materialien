package simulator;

import simulation.simulator.ElementZustand;
import zeichnen.Schlaeger;
import zeichnen.models.Position;

public class BerechneKollisionMitSchlaeger {

	private Schlaeger schlaeger;

	public BerechneKollisionMitSchlaeger(Schlaeger schlaeger) {
		this.schlaeger = schlaeger;
	}

	public void aktualisereElement(ElementZustand element) {
		dreheXRichtungWennWand(element);
	}

	private void dreheXRichtungWennWand(ElementZustand element) {
		if (beruehrtSchlaeger(element.getKoordinaten())) {
			element.dreheXRichtung();
		}
	}

	private boolean beruehrtSchlaeger(Position position) {
		return istAufHoeheVonSchlaeger(position.getY())
				&& beruehrtFlaeche(position.getX());
	}

	private boolean istAufHoeheVonSchlaeger(int yPosition) {
		return untereSchlaegerKante() > yPosition
				&& obereSchlaegerKante() < yPosition;
	}

	private int untereSchlaegerKante() {
		return obereSchlaegerKante() + schlaeger.getGroesse().getHoehe();
	}

	private int obereSchlaegerKante() {
		return schlaeger.getPosition().getY();
	}

	private boolean beruehrtFlaeche(int xPosition) {
		return rechteSchlaegerSeite() > xPosition;
	}

	private int rechteSchlaegerSeite() {
		return schlaeger.getPosition().getX()
				+ schlaeger.getGroesse().getBreite() - 1;
	}

}
