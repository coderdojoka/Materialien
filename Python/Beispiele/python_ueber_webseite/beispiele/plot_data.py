import matplotlib.pyplot as plt

name = input("Datei mit Messwerten:")
with open(name) as datei:
    lines = datei.readlines()

werte = list(map(float, lines))

plt.plot(range(len(werte)), werte)
plt.xlabel('Minuten')
plt.ylabel('Tempartur °C')
plt.title('Temparaturverlauf')
plt.gcf().canvas.set_window_title('Temparaturmessung')
plt.grid(True)
plt.savefig("verlauf.png")
plt.show()
