package steuerelemente.buttons;

import javax.swing.JButton;

public abstract class ZeichenflaecheButton extends JButton {

	private static final long serialVersionUID = 1L;

	public ZeichenflaecheButton(String beschriftung) {
		this.setText(beschriftung);
	}

	public abstract void fuehreAktionAus();

}
