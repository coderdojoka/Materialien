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
    if os.path.isdir("Materialien"):
        os.chdir("Materialien")
        try:
            subprocess.call(["git", "pull"])
        except OSError as e:
            os.chdir("..") # Wir müssen wieder eins hoch :D
            return False

    # Ansonsten klonen wir das Repo neu
    else:
        try:
            subprocess.call(["git", "clone", "https://github.com/coderdojoka/Materialien"])
        except OSError as e:
            return False

    return True

# Änderungen laden
if not git_pull():
    print("Git ist nicth installiert => Lade zip-Datei.")
    print("Dies kann eine Weile dauern...")

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


# Dateien entfernen


# Update-Skript ersetzen
shutil.move("Materialien/Python/coderdojo_update.py", "coderdojo_update.py")