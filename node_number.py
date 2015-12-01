#!/usr/bin/env python
#Bibliotheken importieren
import time
import datetime
import json

#Datei oeffnen
f = open('/var/www/meshviewer/nodelist.json')

#JSON einlesen
data = json.load(f)

#Nodes attribut aussortieren
nodes = data['nodes']

#Zaehler mit Wert 0 anlegen
num_nodes = 0

#Fuer jeden Knoten in nodes
for node in nodes:
        #Status Attribut aussortieren
        status = node['status']

        #Wenn der Status online entaehlt, hochzaehlen
        if status['online']:
                num_nodes += 1

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
