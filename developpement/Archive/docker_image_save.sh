#!/bin/sh
# Sudo check
if ! [ $(id -u) = 0 ]; then
   echo ">> Error, run as root"
   exit 1
fi
# Check if its the right folder
this_dir=`basename $PWD`
if [ $this_dir != "rhasspy_config" ]; then
   echo ">> Error, Please run in rhasspy_config directory"
  exit 1
fi
echo ">> copy rhasspy docker image"
sudo docker save synesthesiam/rhasspy-server > rhasspy-server.tar