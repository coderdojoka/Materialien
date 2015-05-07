package steuerelemente.buttons;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JPanel;

public class ButtonReihe extends JPanel {

	private static final long serialVersionUID = 1L;

	private static final int HOEHE = 30;
	private static final int BREITE = 500;

	public ButtonReihe() {
		this.setLayout(new FlowLayout());
		this.setSize(BREITE, HOEHE);
	}

	public void fuegeButtonHinzu(ZeichenflaecheButton button) {
		this.add(button);
		fuegeListenerHinzu(button);
	}

	private void fuegeListenerHinzu(ZeichenflaecheButton button) {
		button.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent event) {
				button.fuehreAktionAus();
			}

		});
	}

}
