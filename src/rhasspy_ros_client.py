#   Global import
import json
import rospy
from std_msgs.msg import String, Empty
from time import sleep, time
from threading import Thread
#   Local imports
from rhasspy_utils import *

LOG_PREFIX = log_prefix("Ros-Cli")


# Notes
# rospy.loginfo("[ERROR][snips_get_speach_text] " + str(e))
# rospy.Subscriber(ROS_MESSAGE_I_TTS             , String, lambda message: self.callback_ros_on_message(message, ROS_MESSAGE_I_TTS))
# rospy.Subscriber(ROS_MESSAGE_I_ACTIVE_LISTENING, Empty, lambda message: self.callback_ros_on_message(message, ROS_MESSAGE_I_ACTIVE_LISTENING))
# rospy.Subscriber(ROS_TO_NODE_START_LISTENING, Empty, self.callback_ros_on_message)


# noinspection PyUnusedLocal
# noinspection PyMethodMayBeStatic
class RosClient(Thread):
    """ """
    def __init__(self):
        Thread.__init__(self)
        self.mqtt_client = None
        rospy.init_node('wm_rhasspy_service')
        self.ros_pub_stt = rospy.Publisher(RHASSPY_TO_ROS_STT, String, queue_size=10)

    def publish_intent(self, text):
        self.ros_pub_stt.publish(text)

    def set_on_message_callback(self, callback):
        rospy.Subscriber(RHASSPY_TO_ROS_STT, String,
                         lambda message: callback(message, RHASSPY_TO_ROS_STT))

    def run(self):
        ros_log(LOG_PREFIX + "Started")
        rospy.spin()
        ros_log(LOG_PREFIX + "Stopped")
