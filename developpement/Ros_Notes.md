# Development Notes
### Usefull notes related to the use of Ros wyth Python

Function use:
```
rospy.loginfo("[ERROR][snips_get_speach_text] " + str(e))
rospy.Subscriber(ROS_MESSAGE_I_TTS             , String, lambda message: self.callback_ros_on_message(message, ROS_MESSAGE_I_TTS))
rospy.Subscriber(ROS_MESSAGE_I_ACTIVE_LISTENING, Empty, lambda message: self.callback_ros_on_message(message, ROS_MESSAGE_I_ACTIVE_LISTENING))
rospy.Subscriber(ROS_TO_NODE_START_LISTENING, Empty, self.callback_ros_on_message)
rospy.Subscriber(RHASSPY_TO_ROS_STT, String, lambda message: callback(message, RHASSPY_TO_ROS_STT))

# Ros service / topic notes
rospy.Service('rhasspy_ctrl_service', rhasspy_ctrl_service, self.ros_service_callback)
self.ros_pub_stt = rospy.Publisher(RHASSPY_TO_ROS_STT, String, queue_size=10)
self.ros_pub_stt.publish(text)
```