#!/bin/bash
PATH='/opt/ffmap-backend/'
PEERS="/etc/fastd/ffhh-mesh-vpn/peers"

python2 $PATH/generate_aliases.py $PEERS > $PATH/aliases.json
python3 $PATH/backend.py -d /var/www/meshviewer/data/ -a $PATH/aliases.json --vpn de:ad:be:ff:01:01
