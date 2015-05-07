package zeichnen.fenster;

import steuerelemente.elemente.SteuerbaresElement;
import zeichnen.models.elemente.ZeichenbaresElement;

public interface ZeichenflaecheContainer {

	void fuegeZeichenbaresElementHinzu(ZeichenbaresElement element);

	void fuegeSteuerbaresElementHinzu(SteuerbaresElement element);

}
