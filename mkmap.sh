#!/bin/bash
FFMAPPATH='/opt/ffmap-backend/'
PEERS="/etc/fastd/ffhh-mesh-vpn/peers"

python2 $FFMAPPATH/generate_aliases.py $PEERS > $FFMAPPATH/aliases.json
#python3 $FFMAPPATH/backend.py -d /var/www/meshviewer/ --aliases $FFMAPPATH/aliases.json $FFMAPPATH/gateway.json -m bat0:/var/run/alfred.sock -p 30 --vpn de:ad:be:ff:01:01 --vpn de:ad:be:ff:05:05 --vpn de:ad:be:ff:05:06 --vpn de:ad:be:ff:03:03 --vpn de:ad:be:ff:22:22 --vpn de:ad:be:ff:22:23 --vpn de:ad:be:ff:88:88 --vpn de:ad:be:ff:88:89 --vpn de:ad:bf:ff:88:88 --vpn de:ad:bf:ff:22:22 --vpn de:ad:bf:ff:03:03 --vpn de:ad:bf:ff:05:05 --vpn de:ad:bf:ff:01:01 --vpn de:ad:be:fc:03:03 --vpn 00:16:3e:53:75:0d --vpn de:ad:be:fc:05:05 --vpn de:ad:be:fc:01:01 --vpn de:ad:be:ef:03:03 --vpn de:ad:be:ef:01:01 --vpn de:ad:be:ef:05:05 --vpn 00:16:3e:fb:9d:8d --vpn 00:16:3e:fb:9d:9d
python3 $FFMAPPATH/backend.py -d /var/www/meshviewer/ --aliases $FFMAPPATH/aliases.json $FFMAPPATH/gateway.json -m bat0:/var/run/alfred.sock -p 30 --vpn de:ad:be:ff:01:01 de:ad:be:ff:05:05 de:ad:be:ff:05:06 de:ad:be:ff:03:03 de:ad:be:ff:22:22 de:ad:be:ff:22:23 de:ad:be:ff:88:88 de:ad:be:ff:88:89 de:ad:bf:ff:88:88 de:ad:bf:ff:22:22 de:ad:bf:ff:03:03 de:ad:bf:ff:05:05 de:ad:bf:ff:01:01 de:ad:be:fc:03:03 00:16:3e:53:75:0d de:ad:be:fc:05:05 de:ad:be:fc:01:01 de:ad:be:ef:03:03 de:ad:be:ef:01:01 de:ad:be:ef:05:05 00:16:3e:fb:9d:8d 00:16:3e:fb:9d:9d
