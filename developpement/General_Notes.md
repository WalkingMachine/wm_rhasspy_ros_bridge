
# General Notes

Docker  
https://hub.docker.com/r/synesthesiam/rhasspy-server/tags   
KALDI   
https://github.com/synesthesiam/rhasspy-profiles/releases/download/v1.0-en/en_kaldi-zamia.tar.gz 

Install
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

Launch
```
rosdep update
catkin_make -- Using PYTHON_EXECUTABLE: /usr/bin/python3
catkin_make -- Using PYTHON_EXECUTABLE: /usr/bin/python3.5

sudo gedit ~/.bashrc
source /home/jimmy/ROS-WS/devel/setup.sh
```

Launch
```
catkin_make
source devel/setup.bash
rosrun wm_rhasspy_ros_bridge wm_rhasspy_service.py

roslaunch wm_rhasspy_ros_bridge
rosrun wm_rhasspy_ros_bridge

catkin_make wm_rhasspy_ros_bridge -- Using PYTHON_EXECUTABLE: /usr/bin/python3.5

catkin_find_pkg wm_rhasspy_ros_bridge
rosrun wm_rhasspy_ros_bridge wm_rhasspy_service.py
roslaunch wm_rhasspy_ros_bridge wm_rhasspy_service.launch
```

Debug
```
rostopic list
rostopic echo /wm_rhasspy/intent
```