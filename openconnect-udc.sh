#!/bin/bash

HOST=https://vpn.udc.es
FILE=$HOME/downloads/vpn.udc.es.DSID
DSID=$(<$FILE)

openconnect -b --protocol=pulse -C $DSID $HOST

rm $FILE
