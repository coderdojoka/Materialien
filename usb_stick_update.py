__author__ = 'Mark Weinreuter'

import subprocess
import os
import os.path
import shutil
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

# Dieses Skript sollte in dem Ordner liegen, indem auch das Materialien Verzeichnis liegt

def git_pull():
    # Falls bereits vorhanden => pull
    if os.path.isdir(".git"):
        try:
            subprocess.call(["git", "pull"])
            return True
        except OSError as e:
            pass
    return False

def lade_zip():
    # zip datei herrunterladen un direkt entpacken (in memory)
    url = urlopen("https://github.com/coderdojoka/Materialien/archive/usb_stick.zip")

    # eine Ebene höher wechseln
    os.chdir("..")

    # als ZipDatei lesen und entpacken
    zipfile = ZipFile(BytesIO(url.read()))
    zipfile.extractall()

    # ggf. alten Ordner löschen
    if os.path.isdir("Materialien"):
        i = 0
        # find a new name
        while os.path.isdir("Materialien_alt" + str(i)):
            i += 1

        shutil.move("Materialien", "Materialien_alt" + str(i))

    # Ordner umbenennen
    os.replace("Materialien-usb_stick", "Materialien")
    print("Fertig!")

print("Starte Update...")
# Änderungen laden
if not git_pull():
    print("Git ist nicht installiert => Lade zip-Datei.")
    print("Dies kann eine Weile dauern...")
    lade_zip()
