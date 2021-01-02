# Development Notes
### A set of useful notes to develop Rhasspy_Ros_Bridge program

* Do not conciser notes as perfect, there is none functional things

### Testing Execution

Launch Roscore (2021-01-02)
```
roscore
```

Launch Docker (if on WSL 2.0) (2021-01-02)
```
sudo service docker start
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