__author__ = 'Mark Weinreuter'


def lese_datei_text(datei_name, option="r", zeichensatz="utf-8"):
    # Öffnet die Datei mit dem Name aus der Variablen: 'datei_name'. Die Datei muss existieren :)
    # Die Datei wird zum Lesen geöffnet: "r" und als Zeichensatz 'utf-8' (Für komische Zeichen)
    datei = open(datei_name, option, encoding=zeichensatz)

    # Angegebene Datei einlesen und in die Variable 'text' speichern
    text = datei.read()

    # Datei schließen
    datei.close()

    return text


def lese_datei_zeilen(datei_name, option="r", entferne_newline=True, zeichensatz="utf-8"):
    # Öffnet die Datei mit dem Name aus der Variablen 'datei_name'.
    # Die Datei wird zum Lesen geöffnet: "r" (für read) und als Zeichensatz 'utf-8' (Für komische Zeichen)
    datei = open(datei_name, option, encoding=zeichensatz)

    # Einzelne Zeilen aus der angegebene Datei einlesen und in die Variable 'zeilen' (als Liste) speichern
    zeilen = datei.readlines()

    if entferne_newline:
        zeilen = [zeile.strip() for zeile in zeilen]

    # Datei schließen
    datei.close()

    return zeilen


def schreibe_datei_text(datei_name, text, option="w", zeichensatz="utf-8"):
    # Öffnet die die Datei mit dem Name aus der Variablen 'datei_name' zum Schreiben: "w" (für write).

    datei = open(datei_name, option, encoding=zeichensatz)

    # Schreibt den Text in die Datei
    datei.write(text)

    # Datei schließen
    datei.close()


def schreibe_datei_zeilen(datei_name, zeilen, zeilenende="\n", option="w", zeichensatz="utf-8"):
    # Öffnet die die Datei mit dem Name aus der Variablen 'datei_name' zum Schreiben: "w" (für write).

    datei = open(datei_name, option, encoding=zeichensatz)

    # Die Liste der Zeilen mit dem Zeilenende in einen Text umwandeln
    text = zeilenende.join(zeilen)

    # Schreibt den Text in die Datei
    datei.writelines(text)

    # Datei schließen
    datei.close()


if __name__ == "__main__":
    # Text lesen, einmal am Stück, einmal zeilenweise
    text = lese_datei_text("datei_helfer.py")
    zeilen = lese_datei_zeilen("datei_helfer.py")
    print(text)
    print(zeilen)

    # Text schreiben, einmal am Stück, einmal zeilenweise
    schreibe_datei_text("helfer_kopie.txt", text)
    schreibe_datei_zeilen("helfer_kopie.txt", zeilen)
