package zeichnen.fenster;

import static util.CollectionUtil.addIfNotContains;
import static util.CollectionUtil.createList;

import java.awt.Graphics;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.List;
import java.util.function.Consumer;

import javax.swing.JPanel;

import steuerelemente.elemente.SteuerbaresElement;
import zeichnen.einstellungen.ZeichenflaecheEinstellungen;
import zeichnen.models.elemente.ZeichenbaresElement;

public class ZeichenfleachePanel extends JPanel implements
		ZeichenflaecheContainer {

	private static final long serialVersionUID = 1L;

	protected List<ZeichenbaresElement> zuZeichnendeElemente;
	protected List<SteuerbaresElement> steuerbareElement;

	public ZeichenfleachePanel(ZeichenflaecheEinstellungen einstellungen) {
		initPanel(einstellungen);
		zuZeichnendeElemente = createList();
		steuerbareElement = createList();
	}

	private void initPanel(ZeichenflaecheEinstellungen einstellungen) {
		setBackground(einstellungen.getHintergrundfarbe());
		setPreferredSize(einstellungen.getGroesse());
		this.setFocusable(true);
	}

	@Override
	public void fuegeZeichenbaresElementHinzu(ZeichenbaresElement element) {
		zuZeichnendeElemente.add(element);
	}

	@Override
	public void paintComponent(Graphics graphics) {
		super.paintComponent(graphics);

		zeichneElemente(graphics);
	}

	private void zeichneElemente(Graphics graphics) {
		zuZeichnendeElemente.stream().forEach(zeichneElement(graphics));
	}

	private Consumer<ZeichenbaresElement> zeichneElement(Graphics graphics) {
		return new Consumer<ZeichenbaresElement>() {

			@Override
			public void accept(ZeichenbaresElement element) {
				element.zeichne(graphics);
			}
		};
	}

	@Override
	public void fuegeSteuerbaresElementHinzu(SteuerbaresElement element) {
		steuerbareElement.add(element);
		fuegeKeyListenerHinzu(element);
		addIfNotContains(zuZeichnendeElemente, element);
	}

	private void fuegeKeyListenerHinzu(SteuerbaresElement element) {
		this.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent event) {
				element.getTastenAktion(event.getKeyCode()).fuehreAus();
				paintComponent(getGraphics());
			}
		});
	}

}
