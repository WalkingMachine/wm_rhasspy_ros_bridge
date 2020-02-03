# wm_rhasspy_ros_bridge
rhasspy Speach Assistant wrapper
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

Notes
* Rhasspy docker config file
    * cd ~/.config/rhasspy/profiles/en
* Rhasspy web gui
    * http://0.0.0.0:12101
