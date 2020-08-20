"""
Common functions and globals for all the project class
    * Is the only module allowed to use "Ros" Class/function, after "rhasspy_ros_client.py" module
"""
import rospy

#   MQTT constants
MQTT_HOST = 'localhost'
MQTT_PORT = 1883
#   Ros Messages
RHASSPY_TO_ROS_STT = "/wm_rhasspy/intent"
#   Log
LOG_MSG = "[Rhasspy-Bridge]: "
ROS_RHASSPY_NODE = 'wm_rhasspy_service'
ROS_TOPIC_LISTEN = "/wm_rhasspy/listen"
ROS_TOPIC_CONTROL = "/wm_rhasspy/control"


def log_prefix(name):
    return "[" + "{:<8}".format(name) + "] "


def ros_log(text):
    """ Function to log info on ros """
    rospy.loginfo(LOG_MSG + text)
