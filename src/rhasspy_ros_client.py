#   Global import
import json
import rospy
from std_msgs.msg import String, Empty
from time import sleep, time
from threading import Thread
#   Local imports
from rhasspy_utils import *

#   Generated imports
# noinspection PyUnresolvedReferences
from wm_rhasspy_ros_bridge.msg import listen as ListenMsg
# noinspection PyUnresolvedReferences
from wm_rhasspy_ros_bridge.msg import wm_rhasspy_ctrl
# noinspection PyUnresolvedReferences
from wm_rhasspy_ros_bridge.srv import rhasspy_service, rhasspy_ctrl_service

#   Global constant
LOG_PREFIX = log_prefix("Ros-Cli")

# noinspection PyUnusedLocal
# noinspection PyMethodMayBeStatic
class RosClientThread(Thread):
    """ Ros abstraction
            All class to communicate with Ros Core
            -Topic publisher
            -Topic subscriber
    """
    def __init__(self):
        Thread.__init__(self)
        self.mqtt_client = None
        # Ros core connection initialisation
        rospy.init_node(ROS_RHASSPY_NODE)
        self.listen_msg = rospy.Publisher(ROS_TOPIC_LISTEN, ListenMsg, queue_size=1)

    # Topic callback function
    def control_callback(self, data):
        """ Callback of Ros Subscriber "control" """
        print("debug:", data)

    def publish_intent(self, text):

        msg = ListenMsg()
        msg.intent = "intent_1"
        msg.target = "target_1"
        self.listen_msg.publish(msg)

    def set_on_message_callback(self, callback):
        rospy.Subscriber(ROS_TOPIC_CONTROL, data_class=wm_rhasspy_ctrl, callback=self.control_callback, queue_size=1)

        rospy.Subscriber(RHASSPY_TO_ROS_STT, String, lambda message: callback(message, RHASSPY_TO_ROS_STT))

    def run(self):
        ros_log(LOG_PREFIX + "Started")
        rospy.spin()
        ros_log(LOG_PREFIX + "Stopped")

