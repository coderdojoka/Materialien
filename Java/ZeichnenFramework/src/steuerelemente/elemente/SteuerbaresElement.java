package steuerelemente.elemente;

import zeichnen.models.elemente.ZeichenbaresElement;

public interface SteuerbaresElement extends ZeichenbaresElement {

	TastenAktion getTastenAktion(int taste);

}
