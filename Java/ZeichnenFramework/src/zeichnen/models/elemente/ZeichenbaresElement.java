package zeichnen.models.elemente;

import java.awt.Color;
import java.awt.Graphics;

import zeichnen.models.Groesse;
import zeichnen.models.Position;

public interface ZeichenbaresElement {

	Color getColor();

	Position getPosition();

	Groesse getGroesse();

	void zeichne(Graphics graphics);

}
