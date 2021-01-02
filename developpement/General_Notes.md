
# General Notes

Docker  
https://hub.docker.com/r/synesthesiam/rhasspy-server/tags   
KALDI   
https://github.com/synesthesiam/rhasspy-profiles/releases/download/v1.0-en/en_kaldi-zamia.tar.gz 

Install (to be tested)
```
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
```
Launch Ros Core
```
roscore
```

Install (2020-08-30) (WSL 2.0)
```
sudo apt install python-pip
sudo apt install python3-pip
pip3 install paho-mqtt pyyaml rospkg requests netifaces
sudo apt-get install mosquitto mosquitto-clients
sudo systemctl restart mosquitto
# use the install script if no service
sudo apt install libasound-dev portaudio19-dev libportaudiocpp0
pip3 install pyaudio
pip install pathlib
sudo pip3 install hermes-audio-server
```



Launch Rhasspy ROS Bridge (2021-01-02)
```
cd $HOME/ROS-WS
catkin_make
source devel/setup.bash
rosrun wm_rhasspy_ros_bridge wm_rhasspy_service.py
```

Open Rhasspy Web UI (2021-01-02)
```
http://localhost:12101/
```

Open Portainer Web UI (2021-01-02)
```
http://localhost:9000/#/auth
```


Debug
```
rostopic list
rostopic echo /wm_rhasspy/intent
```

Launch (not working)
```
rosdep update
catkin_make -- Using PYTHON_EXECUTABLE: /usr/bin/python3
catkin_make -- Using PYTHON_EXECUTABLE: /usr/bin/python3.5
sudo gedit ~/.bashrc
source /home/jimmy/ROS-WS/devel/setup.sh
```
```
roslaunch wm_rhasspy_ros_bridge
rosrun wm_rhasspy_ros_bridge
catkin_make wm_rhasspy_ros_bridge -- Using PYTHON_EXECUTABLE: /usr/bin/python3.5
catkin_find_pkg wm_rhasspy_ros_bridge
rosrun wm_rhasspy_ros_bridge wm_rhasspy_service.py
roslaunch wm_rhasspy_ros_bridge wm_rhasspy_service.launch
```

