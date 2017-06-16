#!/usr/bin/env python
#Bibliotheken importieren
import time
import datetime
import json
import urllib2

#Datei oeffnen
Datei = urllib2.urlopen('https://map.hamburg.freifunk.net/nodes.json')
Datei_Sued = urllib2.urlopen('https://map.hamburg.freifunk.net/hhsued/mv1/nodes.json')

#Zaehler mit Wert 0 anlegen
num_nodes = 0

Text = Datei.read()
n = Text.count('"online": true')
Text = Datei_Sued.read()
n_Sued = Text.count('"online":true')
num_nodes = n + n_Sued

#Zeit holen
thetime = datetime.datetime.now().isoformat()

ffhh = None

#Freifunk API-Datei einladen und JSON lesen
with open('/var/www/meta/ffhh.json', 'r') as fp:
        ffhh = json.load(fp)

#Attribute Zeitstempel und Knotenanzahl setzen
ffhh['state']['lastchange'] = thetime
ffhh['state']['nodes'] = num_nodes

#Freifunk API-Datein mit geaenderten werten schreiben
with open('/var/www/meta/ffhh.json', 'w') as fp:
        json.dump(ffhh, fp, indent=2, separators=(',', ': '))
