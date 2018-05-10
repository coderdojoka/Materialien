package simulation.zeichnen;

import simulation.simulator.Simulator;
import simulation.simulator.SimulierbaresElement;

public interface SimulatorContainer {

	void fuegeSimulierbaresElementHinzu(SimulierbaresElement element);

	void starteSimulation();

	void stoppeSimulation();

	void fuegeSimulatorHinzu(Simulator simulator);

	void zeigeNachrichtAn(String nachricht);

}
