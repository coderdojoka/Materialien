import os
import signal
import subprocess
import time
from http.server import BaseHTTPRequestHandler, HTTPServer, urllib

import sys

aktuelle_millisekunden = lambda: int(round(time.time() * 1000))


def lese_datei(path):
    if not os.path.exists(path):
        return "no such file"

    with open(path, encoding="utf-8") as datei:
        return datei.read()


def schreibe_datei(path, content):
    with open(path, encoding="utf-8", mode="w") as datei:
        datei.write(content)


class MyHandler(BaseHTTPRequestHandler):
    def get_header_value(self, name):
        for key, value in self.headers._headers:
            print(key, value)
            if key.lower() == name.lower():
                return value

        return None

    def do_POST(self):

        length = int(self.get_header_value('Content-Length'))
        postvars = urllib.parse.parse_qs(self.rfile.read(length), keep_blank_values=1)
        code = postvars[b"code"]

        print(postvars, code)
        id = aktuelle_millisekunden()
        script_name = "hochgeladen/%d.py" % id
        schreibe_datei(script_name, code[0].decode())

        ausgabe = open("hochgeladen/%d.out" % id, "w")
        # -u = unbuffered => Ausgabe wird ungebuffert in die Datei geschrieben.
        process = subprocess.Popen(["python3", "-u", script_name], stdout=ausgabe,stderr=ausgabe, preexec_fn=os.setsid)

        schreibe_datei("hochgeladen/%d.pid" % id, str(process.pid))
        self.umleiten('monitor?id=%d' % id)

    def umleiten(self, where):
        self.send_response(301)
        self.send_header('Location', where)
        self.end_headers()

    def do_GET(self):
        parts = self.path.split("?")
        args = ""
        if len(parts) > 1:
            args = parts[1]

        args = urllib.parse.parse_qs(args, keep_blank_values=1)
        print(args)

        if self.path == "/":
            self.index()
        elif self.path[:8] == "/monitor":
            self.ueberwachen(args["id"][0])
        elif self.path[:5] == "/kill":
            self.beenden(args["id"][0])

        else:
            self.statische_datei()

    def index(self):
        self.positive_antwort(lese_datei("web/content.html"))

    def positive_antwort(self, content):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(content, "utf8"))

    def statische_datei(self):

        pfad = self.path[1:]
        if os.path.exists(pfad):
            self.send_response(200)
            # self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(open(pfad).read(), "utf8"))
        else:
            print("No such file: ", pfad)
            self.send_response(404)
            self.wfile.write(bytes("No such file", "utf8"))

    def ueberwachen(self, id):
        inhalt = lese_datei("web/monitor.html")
        ausgabe = lese_datei("hochgeladen/" + id + ".out")
        inhalt = inhalt.replace("$$CONTENT$$", ausgabe)
        inhalt = inhalt.replace("$$ID$$", id)

        self.positive_antwort(inhalt)

    def beenden(self, id):
        pid_file = "hochgeladen/%s.pid" % id
        if os.path.exists(pid_file):
            pid = int(lese_datei(pid_file))
            print("Kill process: ", pid)
            try:
                os.killpg(os.getpgid(pid), signal.SIGTERM)
            except Exception as e:
                print(e)
            finally:
                # os.remove(pid_file)
                self.positive_antwort("killed")
        else:
            self.positive_antwort("no such pid")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        server_address = ('', int(sys.argv[1]))
    else:
        server_address = ('', 8081)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server läuft: http://localhost:%d/" % server_address[1])
    httpd.serve_forever()
