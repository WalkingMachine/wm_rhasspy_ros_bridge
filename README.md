# wm_rhasspy_ros_bridge
Rhasspy Speach Assistant wrapper
* Hotword detection
    * Will start Speech detection
* Speach to text
    * Will generate Phonem speech representation
* Intent parser
    * Web Interface configured
        * All the possible phrase are writted here
    * Will convert the Phonem to intents
        * All intents are automaticaly outputed to MQTT
        * MQTT is converted to ROS message 

Notes:
* Rhasspy docker config file
  * cd ~/.config/rhasspy/profiles/en
* Rhasspy web gui
  * http://0.0.0.0:12101
    
    
## Installation
- Tested on Ubuntu 16.04
### Docker
```
curl -sSL https://get.docker.com | sh 
sudo usermod -a -G docker $USER
# TODO validate next step
sudo docker run -d -p 8000:8000 -p 9000:9000 -v   
```
### Allow docker to connect to local host
```
sudo iptables -A INPUT -i docker0 -j ACCEPT
```
Notes:
* Interface docker0 == 172.17.0.1
### Portainer (docker interface)
```
sudo docker volume create portainer_data
sudo docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce

# Deprecated command (i dont remember why this is here)
/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```
### Run Rhasspy docker image
```
sudo docker run -d -p 12101:12101\
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \      
      synesthesiam/rhasspy-server:latest \
      --user-profiles /profiles \
      --profile en
```
Notes:
- If you want a second Rhasspy server running.
    - Change the port mapping \
    `12101:12101` \
    To \
    "12102:12101"
- If you want a second Rhasspy server with a difrend config
    - Change the target local directory \
    `$HOME/.config/rhasspy/profiles:/profiles` \
    To \
    `$HOME/.config/rhasspy/profiles2:/profiles`
  
### Mosquito MQTT server
```
sudo apt-get update
sudo apt-get install mosquitto
```
### Hermes audio server
Installation of the Hermes audio server.
To send and receive audio to the Rhasspy server within the MWTT server

https://pypi.org/project/hermes-audio-server/
```
sudo apt-get install python3-setuptools
sudo apt-get install python3-pip
pip3 install wheel
sudo pip3 install hermes-audio-server
```
