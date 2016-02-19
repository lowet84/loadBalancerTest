#!/bin/bash
VMS=$1
COUNTER=1
while [  $COUNTER -le $VMS ]; do
  PORT=$((8080+$COUNTER))
  sed -i "5i server 10.0.2.2:$PORT;" /etc/nginx/nginx.conf
  COUNTER=$((COUNTER+1))
done
nginx -s reload
