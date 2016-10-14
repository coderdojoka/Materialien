import time, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "algos"))

from arena import Arena, SPIELFELD_BREITE, SPIELFELD_HOEHE

__author__ = 'Mark Weinreuter'

print("Willkommen zum Kampf der Programme\n")
print("Der heutige Kampf wird ausgetragen zwischen:")
runden = input("Anzahl der Runden (9):")
try:
    runden = int(runden)
except ValueError:
    runden = 9
    pass

algo1 = input("In der linken Ecke (zufall.Zufall1): ").strip()
algo2 = input("In der rechten Ecke (liner.Liner): ").strip()

# Annahme modul.name
if len(algo1) < 2:
    algo1 = "zufall.Zufall1"
if len(algo2) < 2:
    algo2 = "liner.Liner"

algo1_mod, algo1_name = algo1.split(".")
algo2_mod, algo2_name = algo2.split(".")

algo1_stats = {"name": algo1_name, "siege": 0, "punkte": [], "zuege": []}
algo2_stats = {"name": algo2_name, "siege": 0, "punkte": [], "zuege": []}

w = SPIELFELD_BREITE
h = SPIELFELD_HOEHE

scale = 9
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0)]

img_support = True
try:
    import os
    from PIL import Image

    background = Image.new('RGBA', (w * scale, h * scale), (255, 255, 255, 255))
    if not os.path.exists("imgs"):
        os.mkdir("imgs")

except ImportError as e:
    img_support = False
    print("\n\n", e)
    print("Install pillow first: pip3 install pillow\n\n")

for runde in range(0, runden):

    # Immer abwechselnd Spieler1 und Spieler2 laufen lassen
    if runde % 2 == 0:
        arena = Arena(algo1_mod, algo1_name, algo2_mod, algo2_name)
        a1 = algo1_stats
        a2 = algo2_stats
    else:
        arena = Arena(algo2_mod, algo2_name, algo1_mod, algo1_name)
        a1 = algo2_stats
        a2 = algo1_stats

    arena.start()

    punkte1 = []
    punkte2 = []

    print()
    print("Runde: ", runde)

    while arena.laueft_noch():
        p1, p2 = arena.aktualisiere()
        punkte1.extend(p1)
        punkte2.extend(p2)
        # print("Punkte: %s = %d, %s = %d" % (a1["name"], len(punkte1), a2["name"], len(punkte2)))
        time.sleep(.01)

    if img_support:
        img = Image.new('RGB', (w * scale, h * scale))

        data = [(0, 0, 0)] * h * w * scale * scale
        for i, b in enumerate(arena.felder):
            x = i % w
            y = i // w
            for k in range(0, scale):
                for j in range(0, scale):
                    index = (y * scale + k) * (scale * w) + x * scale + j
                    data[index] = colors[b]

        img.putdata(data)
        img.save('imgs/runden_%d.png' % runde)
        img.putalpha(200)

        background = Image.blend(img, background, .5)

    print()
    print("Züge gesamt: %d, augeteilt: %d|%d" % tuple(arena.zuege_uebersicht))
    print("Punkte: %d|%d" % tuple(arena.punkte))

    if arena.punkte[0] > arena.punkte[1]:
        print(a1["name"], "gewinnt!")
        a1["siege"] += 1

    else:
        print(a2["name"], "gewinnt!")
        a2["siege"] += 1

    a1["zuege"].append(arena.zuege_uebersicht[1])
    a2["zuege"].append(arena.zuege_uebersicht[2])

    a1["punkte"].append(arena.punkte[0])
    a2["punkte"].append(arena.punkte[1])

if img_support:
    background.save('imgs/runden_blend.png')

print("\n\nZusammenfassung: %s gewinnt" % (algo1_stats["name"] if algo1_stats["siege"] > algo2_stats["siege"] else algo2_stats["name"]))
print("%s %d:%d %s" % (algo1_stats["name"], algo1_stats["siege"], algo2_stats["siege"], algo2_stats["name"]))

