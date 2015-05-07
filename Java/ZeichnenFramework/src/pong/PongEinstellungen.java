package pong;

import static util.Farben.SCHWARZ;

import java.awt.Color;
import java.awt.Dimension;

import simulation.zeichnen.SimulierteZeichenflaecheEinstellung;

public class PongEinstellungen implements SimulierteZeichenflaecheEinstellung {

	@Override
	public Color getHintergrundfarbe() {
		return SCHWARZ;
	}

	@Override
	public int getFramesProSekunde() {
		return 60;
	}

	@Override
	public Dimension getGroesse() {
		return new Dimension(500, 500);
	}

	@Override
	public String getFensterTitel() {
		return "Pong";
	}

}
