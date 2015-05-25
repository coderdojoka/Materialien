bestesMaterial = ""
besteStärke = -1

material = input("Material: ")
while material != "fertig":
    stärke = int(input("Stärke: "))
    if stärke > besteStärke:
        besteStärke = stärke
        bestesMaterial = material
    material = input("Material: ")
print(bestesMaterial)
