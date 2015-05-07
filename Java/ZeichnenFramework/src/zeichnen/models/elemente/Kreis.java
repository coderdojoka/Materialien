package zeichnen.models.elemente;

import java.awt.Graphics;

import zeichnen.models.Groesse;
import zeichnen.models.Position;

public abstract class Kreis extends Figur {

	@Override
	protected void zeichneFigur(Graphics graphics, Position coordinates,
			Groesse dimension) {
		graphics.fillOval(coordinates.getX(), coordinates.getY(),
				dimension.getBreite(), dimension.getHoehe());
	}

}
