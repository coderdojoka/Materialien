package simulator;

import simulation.simulator.ElementZustand;

public class BerechneKollisionMitWand {

	private static final int WAND_LINKS = 0;
	private static final int WAND_OBEN = 0;
	private static final int WAND_RECHTS = 470;
	private static final int WAND_UNTEN = 410;

	public void aktualisiereElement(ElementZustand element) {
		dreheRichtungWennBeruehreWand(element);
		element.bewegeUm(element.getGeschwindigkeit());
	}

	private void dreheRichtungWennBeruehreWand(ElementZustand element) {
		dreheXRichtungWennWand(element);
		dreheYRichtungWennWand(element);
	}

	private void dreheYRichtungWennWand(ElementZustand element) {
		int yPosition = element.getKoordinaten().getY();
		if (beruehrtObereWand(yPosition) || beruehrtUntereWand(yPosition)) {
			element.dreheYRichtung();
		}
	}

	private void dreheXRichtungWennWand(ElementZustand element) {
		int xPosition = element.getKoordinaten().getX();
		if (beruehrtLinkeWand(xPosition) || beruehrtRechteWand(xPosition)) {
			element.dreheXRichtung();
		}
	}

	private boolean beruehrtUntereWand(int yPosition) {
		return yPosition > WAND_UNTEN;
	}

	private boolean beruehrtObereWand(int yPosition) {
		return yPosition < WAND_OBEN;
	}

	private boolean beruehrtRechteWand(int xPosition) {
		return xPosition > WAND_RECHTS;
	}

	private boolean beruehrtLinkeWand(int xPosition) {
		return xPosition < WAND_LINKS;
	}

}
