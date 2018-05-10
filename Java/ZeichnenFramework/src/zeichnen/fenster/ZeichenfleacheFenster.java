package zeichnen.fenster;

import static javax.swing.BoxLayout.Y_AXIS;

import java.awt.Component;

import javax.swing.BoxLayout;
import javax.swing.JFrame;
import javax.swing.JPanel;

import zeichnen.einstellungen.ZeichenflaecheEinstellungen;

public class ZeichenfleacheFenster extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel panel;

	public ZeichenfleacheFenster(ZeichenflaecheEinstellungen einstellungen) {
		initFenster(einstellungen);
	}

	private void initFenster(ZeichenflaecheEinstellungen einstellungen) {
		this.setTitle(einstellungen.getFensterTitel());
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setSize(einstellungen.getGroesse());
		erstellePanel();
		verschiebeFensterInMitte();
	}

	private void erstellePanel() {
		panel = new JPanel();
		panel.setLayout(new BoxLayout(panel, Y_AXIS));
		this.add(panel);
	}

	private void verschiebeFensterInMitte() {
		this.setLocationRelativeTo(null);
	}

	public void fuegePanelHinzu(Component component) {
		panel.add(component);
	}

}
