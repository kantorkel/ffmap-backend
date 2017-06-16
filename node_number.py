#!/usr/bin/env python
#Bibliotheken importieren
import time
import datetime
import json
import urllib2

#Datei oeffnen
Datei = urllib2.urlopen('https://map.hamburg.freifunk.net/nodes.json')
Datei_Sued = urllib2.urlopen('https://map.hamburg.freifunk.net/hhsued/mv1/nodes.json')

Text = Datei.read()
Knotenzahl = Text.count('"online": true')
Text = Datei_Sued.read()
Knotenzahl = Knotenzahl + Text.count('"online":true')

#Zeit holen
thetime = datetime.datetime.now().isoformat()

ffhh = None

#Freifunk API-Datei einladen und JSON lesen
with open('/var/www/meta/ffhh.json', 'r') as fp:
        ffhh = json.load(fp)

#Attribute Zeitstempel und Knotenanzahl setzen
ffhh['state']['lastchange'] = thetime
ffhh['state']['nodes'] = Knotenzahl

#Freifunk API-Datein mit geaenderten werten schreiben
with open('/var/www/meta/ffhh.json', 'w') as fp:
        json.dump(ffhh, fp, indent=2, separators=(',', ': '))
