__author__ = 'Mark Weinreuter'


# Zum Laden von Webseite
import urllib.request


# Lädt den HTML-Text einer Webseite
def lade_webseite(url, cookiejar=None):
    html = ""

    if cookiejar is not None:
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
    else:
        opener = urllib.request.build_opener()

    # Alle Fehler abfangen bei ungültigen Urls
    try:

        with opener.open(url) as response:
            html = response.read()
            # info = response.info()

    except Exception as e:
        print("Fehler beim Laden:", e)

    return html
