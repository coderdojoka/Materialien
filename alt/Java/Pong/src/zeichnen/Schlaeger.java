package zeichnen;

import static util.Farben.WEISS;
import static util.Tasten.PFEIL_OBEN;
import static util.Tasten.PFEIL_UNTEN;

import java.awt.Color;

import steuerelemente.elemente.SteuerbaresElement;
import steuerelemente.elemente.TastenAktion;
import steuerelemente.elemente.TastenAktionsContainer;
import zeichnen.models.Groesse;
import zeichnen.models.Position;
import zeichnen.models.elemente.Rechteck;

public class Schlaeger extends Rechteck implements SteuerbaresElement {

	private static final int STEPS = 5;
	private TastenAktionsContainer aktionen;
	private Position position;

	public Schlaeger() {
		aktionen = new TastenAktionsContainer();
		position = new Position(20, 100);
		erstelleTastenAktionen();
	}

	private void erstelleTastenAktionen() {
		fuegePfleilUntenAktionHinzu();
		fuegePfleilObenAktionHinzu();
	}

	private void fuegePfleilUntenAktionHinzu() {
		aktionen.fuegeAktionHinzu(PFEIL_UNTEN, new TastenAktion() {

			@Override
			public void fuehreAus() {
				position.setY(position.getY() + STEPS);
			}
		});
	}

	private void fuegePfleilObenAktionHinzu() {
		aktionen.fuegeAktionHinzu(PFEIL_OBEN, new TastenAktion() {

			@Override
			public void fuehreAus() {
				position.setY(position.getY() - STEPS);
			}
		});
	}

	@Override
	public Color getColor() {
		return WEISS;
	}

	@Override
	public Position getPosition() {
		return position;
	}

	@Override
	public Groesse getGroesse() {
		return new Groesse(10, 100);
	}

	@Override
	public TastenAktion getTastenAktion(int taste) {
		return aktionen.getAktion(taste);
	}

}
