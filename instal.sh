#!/bin/bash
# Sudo check
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
# Check if in the right folder
this_dir=`basename $PWD`
if [ $this_dir != "wm_rhasspy_ros_bridge" ]; then
   echo "Error, Please run in wm_rhasspy_ros_bridge directory"
  exit 1
fi
# Install docker
sudo apt-get update
sudo apt-get install docker.io
# Portainer Docker (GUI docker manager)
sudo docker volume create portainer_data
sudo docker run -d -p 8000:8000 -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
# Rhasspi docker !!!!
sudo iptables -A INPUT -i docker0 -j ACCEPT
sudo docker run -d --name rhasspy_server_en -p 12101:12101\
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \
      --device /dev/snd:/dev/snd \
      synesthesiam/rhasspy-server:latest \
      --user-profiles /profiles \
      --profile en
# Install mosquitto MQTT server
sudo apt-get update
sudo apt-get install mosquitto

