#!/bin/sh
# Sudo check
if ! [ $(id -u) = 0 ]; then
   echo ">> Error, run as root"
   exit 1
fi
# Active directorry check
this_dir=`basename $PWD`
if [ $this_dir != "hermes_config" ]; then
   echo ">> Error, Please run in hermes_config directory"
  exit 1
fi

echo "copy hermes-audio-server.json into /etc/"
cp hermes-audio-server.json /etc/