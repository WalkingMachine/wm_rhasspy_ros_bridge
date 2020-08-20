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
/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```
### Run Rhasspy docker image
```
docker run -d -p 12101:12101\
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \      --device /dev/snd:/dev/snd \
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
### Notes personnel
https://hub.docker.com/r/synesthesiam/rhasspy-server/tags
KALDI \
https://github.com/synesthesiam/rhasspy-profiles/releases/download/v1.0-en/en_kaldi-zamia.tar.gz 

Install \
sudo apt install python-pip \
pip install --upgrade pip \
pip install -r requirements.txt \
*Si un bug de ssl \
sudo python -m easy_install --upgrade pyOpenSSL
*Pyaudio error
sudo apt install libasound-dev portaudio19-dev libportaudiocpp0
pip3 install pyaudio
pip3 install hermes-audio-server
sudo apt-get install mosquitto

Launch:
rosdep update
catkin_make -- Using PYTHON_EXECUTABLE: /usr/bin/python3
catkin_make -- Using PYTHON_EXECUTABLE: /usr/bin/python3.5

sudo gedit ~/.bashrc
source /home/jimmy/ROS-WS/devel/setup.sh

Launch:
catkin_make
source devel/setup.bash
rosrun wm_rhasspy_ros_bridge wm_rhasspy_service.py

roslaunch wm_rhasspy_ros_bridge
rosrun wm_rhasspy_ros_bridge

catkin_make wm_rhasspy_ros_bridge -- Using PYTHON_EXECUTABLE: /usr/bin/python3.5

catkin_find_pkg wm_rhasspy_ros_bridge
rosrun wm_rhasspy_ros_bridge wm_rhasspy_service.py
roslaunch wm_rhasspy_ros_bridge wm_rhasspy_service.launch


Debug:
rostopic list
rostopic echo /wm_rhasspy/intent