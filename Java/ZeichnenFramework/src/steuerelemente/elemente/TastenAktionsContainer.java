package steuerelemente.elemente;

import static util.CollectionUtil.createMap;

import java.util.Map;

public class TastenAktionsContainer {

	private Map<Integer, TastenAktion> aktionen;

	public TastenAktionsContainer() {
		aktionen = createMap();
	}

	public void fuegeAktionHinzu(int taste, TastenAktion aktion) {
		aktionen.put(taste, aktion);
	}

	public TastenAktion getAktion(int taste) {
		return aktionen.getOrDefault(taste, new LeereTastenAktion());
	}

}
