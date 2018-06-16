package pong;

import simulation.simulator.Simulator;
import simulation.simulator.SimulierbaresElement;
import simulation.zeichnen.SimulierteZeichenflaecheEinstellung;
import simulation.zeichnen.ZeichenflaecheMitSimulator;
import steuerelemente.buttons.ButtonReihe;
import steuerelemente.buttons.ZeichenflaecheButton;
import steuerelemente.elemente.SteuerbaresElement;
import zeichnen.fenster.FensterMitButtons;
import zeichnen.fenster.ZeichenfleacheFenster;
import zeichnen.models.elemente.ZeichenbaresElement;

public class PongFenster implements FensterMitButtons {

	private ZeichenfleacheFenster zeichenflaecheFenster;
	private ZeichenflaecheMitSimulator zeichenflaechePanel;
	private ButtonReihe buttonReihe;

	private SimulierteZeichenflaecheEinstellung einstellung;

	public PongFenster() {
		einstellung = new PongEinstellungen();
		erstelle();
	}

	public PongFenster(SimulierteZeichenflaecheEinstellung einstellung) {
		this.einstellung = einstellung;
		erstelle();
	}

	private void erstelle() {
		erstelleFenster();
		erstelleSimulierbareZeichenflaeche();
		erstelleButtonReihe();
	}

	private void erstelleFenster() {
		zeichenflaecheFenster = new ZeichenfleacheFenster(einstellung);
	}

	private void erstelleSimulierbareZeichenflaeche() {
		zeichenflaechePanel = new ZeichenflaecheMitSimulator(einstellung);
		zeichenflaecheFenster.fuegePanelHinzu(zeichenflaechePanel);
	}

	private void erstelleButtonReihe() {
		buttonReihe = new ButtonReihe();
		zeichenflaecheFenster.fuegePanelHinzu(buttonReihe);
	}

	@Override
	public void oeffnen() {
		zeichenflaecheFenster.setVisible(true);
	}

	@Override
	public void fuegeZeichenbaresElementHinzu(ZeichenbaresElement element) {
		zeichenflaechePanel.fuegeZeichenbaresElementHinzu(element);
	}

	@Override
	public void fuegeSimulierbaresElementHinzu(SimulierbaresElement element) {
		zeichenflaechePanel.fuegeSimulierbaresElementHinzu(element);
	}

	@Override
	public void fuegeSteuerbaresElementHinzu(SteuerbaresElement element) {
		zeichenflaechePanel.fuegeSteuerbaresElementHinzu(element);
	}

	@Override
	public void fuegeButtonHinzu(ZeichenflaecheButton button) {
		buttonReihe.fuegeButtonHinzu(button);
	}

	@Override
	public void fuegeSimulatorHinzu(Simulator simulator) {
		zeichenflaechePanel.fuegeSimulatorHinzu(simulator);
	}

	@Override
	public void starteSimulation() {
		zeichenflaechePanel.starteSimulation();
	}

	@Override
	public void stoppeSimulation() {
		zeichenflaechePanel.stoppeSimulation();
	}

	@Override
	public void zeigeNachrichtAn(String nachricht) {
		zeichenflaechePanel.zeigeNachrichtAn(nachricht);
	}

}
