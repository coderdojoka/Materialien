import atexit
import os
import signal
import time

import RPi.GPIO as GPIO

__author__ = 'Mark Weinreuter'


def __wenn_SIGTERM(code, frame):
    # print(code, frame)
    print("Beenden Signal erhalten. Beende...")
    __beenden()
    exit()


__pins_benutzt = 0


def __setup(pin, wie, **kwargs):
    global __pins_benutzt
    __pins_benutzt += 1
    GPIO.setup(pin, wie, **kwargs)


def __beenden():
    # Um die nervige Warunung zu behandeln
    if __pins_benutzt > 0:
        GPIO.cleanup()


_temparatur_sensor_wert_pfad = "/sys/devices/w1_bus_master1/%s/w1_slave"
_mein_sensor = None
_bekannte_serien_nummern = ["28-000005fe54fd",  # Weiß
                            "28-000005fee758",  # Gelb
                            "28-000005ac8bf6",  # Blau
                            "28-000005fe46ce"  # Grün
                            ]


def finde_serien_nummer():
    global _mein_sensor

    for nummer in _bekannte_serien_nummern:
        if os.path.exists(_temparatur_sensor_wert_pfad % nummer):
            _mein_sensor = _temparatur_sensor_wert_pfad % nummer
            return True

    return False


def temparatur():
    """
    Format:
    ea 00 4b 46 7f ff 06 10 f0 : crc=f0 YES
    ea 00 4b 46 7f ff 06 10 f0 t=14625
    """

    if _mein_sensor is None:
        if not finde_serien_nummer():
            print("Kein Temparatursensor gefunden!")
            return "Kein Temparatursensor gefunden!"
    try:
        with open(_mein_sensor) as datei:
            text = datei.read()
            if text.find("YES") != -1:
                pos = text.find("t=")
                temp = int(text[pos + 2:])
                temp //= 100  # Letzen zwei stellen entfernen
                return temp / 10

    except Exception as e:
        print(e)
        return "Fehler beim Auslesen!"


def sage(*was, sep=' ', end='\n'):
    print(*was, sep=sep, end=end)


def warte(t):
    time.sleep(t)


def eingang(n):
    __setup(n, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def ausgang(n):
    __setup(n, GPIO.OUT)


def pin_ein(n):
    GPIO.output(n, GPIO.HIGH)


def pin_aus(n):
    GPIO.output(n, GPIO.LOW)


# Board initialisieren
GPIO.setmode(GPIO.BOARD)

# Falls per Signal terminiert
signal.signal(signal.SIGTERM, __wenn_SIGTERM)

# Falls normal beendet
atexit.register(__beenden)
