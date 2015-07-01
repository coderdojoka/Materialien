__author__ = 'Mark Weinreuter'

import subprocess
import os
import os.path
import shutil
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

# Dieses Skript sollte in dem Ordner liegen, indem auch das Materialien Verzeichnis liegt

def loesche_unnoetige_dateien(base):

    for root, dirs, files in os.walk(base):
        for file in files:
            if any(file.lower().endswith(ext) for ext in [".tex", ".cls", ".sty"]):
                print("Removing: ", file)
                os.remove(os.path.join(root, file))

def git_pull():

    # Falls bereits vorhanden => pull
    if os.path.isdir("Materialien/.git"):
        os.chdir("Materialien")
        try:
            subprocess.call(["git", "pull"])
            os.chdir("..")
            return True
        except OSError as e:
            os.chdir("..")
            return False

    # Ansonsten klonen wir das Repo neu
    else:

        # ggf. alten Ordner löschen
        if os.path.isdir("Materialien"):
            shutil.rmtree("Materialien")

        try:
            subprocess.call(["git", "clone", "https://github.com/coderdojoka/Materialien"])
        except OSError as e:
            return False

    return True

def lade_zip():
    # zip datei herrunterladen un direkt entpacken (in memory)
    url = urlopen("https://github.com/coderdojoka/Materialien/archive/master.zip")

    # als ZipDatei lesen und entpacken
    zipfile = ZipFile(BytesIO(url.read()))
    zipfile.extractall()

    # ggf. alten Ordner löschen
    if os.path.isdir("Materialien"):
        shutil.rmtree("Materialien")

    # Ordner umbenennen
    os.replace("Materialien-master", "Materialien")
    print("Fertig!")


# Änderungen laden
if not git_pull():
    print("Git ist nicht installiert => Lade zip-Datei.")
    print("Dies kann eine Weile dauern...")
    lade_zip()

# Lösche unnötige Dateien, z.B. tex files
loesche_unnoetige_dateien("Materialien")

# Update-Skript ersetzen
shutil.copy("Materialien/Python/usb_stick_update.py", "usb_stick_update.py")
