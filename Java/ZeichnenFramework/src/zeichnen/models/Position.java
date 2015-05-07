package zeichnen.models;

public class Position {

	private int x;
	private int y;

	public Position(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void add(Position koordinate) {
		x += koordinate.getX();
		y += koordinate.getY();
	}

	public void setY(int y) {
		this.y = y;
	}

}
