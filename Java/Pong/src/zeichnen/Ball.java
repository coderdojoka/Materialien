package zeichnen;

import static util.Farben.WEISS;

import java.awt.Color;

import simulation.simulator.SimulierbaresElement;
import zeichnen.models.Groesse;
import zeichnen.models.Position;
import zeichnen.models.elemente.Kreis;

public class Ball extends Kreis implements SimulierbaresElement {

	private Position position;

	public Ball() {
		position = new Position(40, 20);
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
		return new Groesse(20, 20);
	}

	@Override
	public int getSpeed() {
		return 3;
	}

}
