package main;

import pong.PongFenster;
import simulator.BallSimulator;
import zeichnen.Ball;
import zeichnen.Schlaeger;
import zeichnen.fenster.FensterMitButtons;
import buttons.PauseButton;
import buttons.StartButton;

public class Pong {

	public static void main(String[] args) {
		FensterMitButtons frame = new PongFenster();

		Schlaeger schlaeger = new Schlaeger();
		frame.fuegeSteuerbaresElementHinzu(schlaeger);
		frame.fuegeSimulierbaresElementHinzu(new Ball());
		frame.fuegeButtonHinzu(new StartButton(frame));
		frame.fuegeButtonHinzu(new PauseButton(frame));
		frame.fuegeSimulatorHinzu(new BallSimulator(schlaeger, frame));

		frame.oeffnen();
	}

}
