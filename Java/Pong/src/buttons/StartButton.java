package buttons;

import steuerelemente.buttons.ZeichenflaecheButton;
import zeichnen.fenster.FensterMitButtons;

public class StartButton extends ZeichenflaecheButton {

	private static final long serialVersionUID = 1L;
	private FensterMitButtons frame;

	public StartButton(FensterMitButtons frame) {
		super("Start");
		this.frame = frame;
	}

	@Override
	public void fuehreAktionAus() {
		frame.starteSimulation();
	}

}
