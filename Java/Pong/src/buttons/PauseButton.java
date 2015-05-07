package buttons;
import steuerelemente.buttons.ZeichenflaecheButton;
import zeichnen.fenster.FensterMitButtons;

public class PauseButton extends ZeichenflaecheButton {

	private FensterMitButtons fenster;

	public PauseButton(FensterMitButtons fenster) {
		super("Pause");
		this.fenster = fenster;
	}

	private static final long serialVersionUID = 1L;

	@Override
	public void fuehreAktionAus() {
		fenster.stoppeSimulation();
	}

}
