package simulation.zeichnen;

import static util.CollectionUtil.addIfNotContains;
import static util.CollectionUtil.createList;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;
import java.util.function.Consumer;

import javax.swing.JOptionPane;
import javax.swing.Timer;

import simulation.simulator.ElementZustand;
import simulation.simulator.LeererSimulator;
import simulation.simulator.Simulator;
import simulation.simulator.SimulierbaresElement;
import zeichnen.fenster.ZeichenfleachePanel;

public class ZeichenflaecheMitSimulator extends ZeichenfleachePanel implements
		ActionListener, SimulatorContainer {

	private static final int SEKUNDE_IN_MS = 1000;

	private static final long serialVersionUID = 1L;

	private List<ElementZustand> simulierteElemente;
	private Simulator simulator;
	private Timer timer;

	public ZeichenflaecheMitSimulator(
			SimulierteZeichenflaecheEinstellung einstellung) {
		super(einstellung);

		timer = new Timer(berechneFPS(einstellung), this);
		simulierteElemente = createList();
		simulator = new LeererSimulator();
	}

	private int berechneFPS(SimulierteZeichenflaecheEinstellung einstellung) {
		return SEKUNDE_IN_MS / einstellung.getFramesProSekunde();
	}

	@Override
	public void fuegeSimulierbaresElementHinzu(SimulierbaresElement element) {
		simulierteElemente.add(new ElementZustand(element));
		addIfNotContains(zuZeichnendeElemente, element);
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		simuliere();
		repaint();
	}

	@Override
	public void starteSimulation() {
		timer.start();
	}

	@Override
	public void stoppeSimulation() {
		timer.stop();
	}

	private void simuliere() {
		simulierteElemente.stream().forEach(simuliereEinElement());
	}

	private Consumer<ElementZustand> simuliereEinElement() {
		return new Consumer<ElementZustand>() {

			@Override
			public void accept(ElementZustand element) {
				simulator.simuliereElement(element);
			}

		};
	}

	@Override
	public void fuegeSimulatorHinzu(Simulator simulator) {
		this.simulator = simulator;
	}

	@Override
	public void zeigeNachrichtAn(String nachricht) {
		JOptionPane.showMessageDialog(this, nachricht);
	}

}
