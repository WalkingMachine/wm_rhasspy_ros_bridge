
import rospy

#   MQTT constants
MQTT_HOST = 'localhost'
MQTT_PORT = 1883
#   Ros Messages
RHASSPY_TO_ROS_STT = "/wm_rhasspy/intent"
#   Log
LOG_MSG = "[Rhasspy-Bridge]: "


def log_prefix(name):
    return "[" + "{:<8}".format(name) + "] "


def ros_log(text):
    rospy.loginfo(LOG_MSG + text)
