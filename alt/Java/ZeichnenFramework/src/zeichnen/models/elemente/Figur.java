package zeichnen.models.elemente;

import java.awt.Color;
import java.awt.Graphics;

import zeichnen.models.Groesse;
import zeichnen.models.Position;

public abstract class Figur implements ZeichenbaresElement {

	@Override
	public abstract Color getColor();

	@Override
	public abstract Position getPosition();

	@Override
	public abstract Groesse getGroesse();

	@Override
	public void zeichne(Graphics graphics) {
		graphics.setColor(getColor());
		Position coordinates = getPosition();
		Groesse dimension = getGroesse();
		zeichneFigur(graphics, coordinates, dimension);
	}

	protected void zeichneFigur(Graphics graphics, Position coordinates,
			Groesse dimension) {
		graphics.fillRect(coordinates.getX(), coordinates.getY(),
				dimension.getBreite(), dimension.getHoehe());
	}

}
