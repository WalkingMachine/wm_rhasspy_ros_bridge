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

# Download rhasspy-server image from Walking machine Google drive
curl

# install rhasspy-server.tar image from tar
echo "install docker image from rhasspy-server.tar"
sudo docker load rhasspy-server.tar

# configure docker container
sudo docker run -d -p 12101:12101\
--name rhasspy1 \
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \
      --device /dev/snd:/dev/snd \
      synesthesiam/rhasspy-server:latest \
      --user-profiles /profiles \
      --profile en