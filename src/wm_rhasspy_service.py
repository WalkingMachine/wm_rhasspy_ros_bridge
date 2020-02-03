# -*- coding: utf-8 -*-
"""
cd ~/Repo/wm_rhasspy/
source ~/Repo/wm_rhasspy/.pyenv/bin/activate
pip install paho-mqtt pyyaml rospkg requests websockets netifaces

bash -i -c "/snap/pycharm-community/172/bin/pycharm.sh" %f
"""
#   Global import
import json
import rospy
from time import sleep, time
#   Local imports
from hermes_services import HermesServices
from rhasspy_rest_api import RhasspyRestApiClient, RhasspyRestApiServer
from rhasspy_mqtt_client import MqttClient
from rhasspy_ros_client import RosClient
from rhasspy_utils import *

LOG_PREFIX = log_prefix("Main")

RHASSPY_1_REST_URM = "http://0.0.0.0:12101"
RHASSPY_2_REST_URM = "http://0.0.0.0:12102"
WEB_SERVER_1_PORT = 8010
WEB_SERVER_2_PORT = 8011


class CallbackCenter:
    def __init__(self):
        self.function_ros_publish_intent = None
        self.rest_api_client_1 = RhasspyRestApiClient(RHASSPY_1_REST_URM)

    def set_function_ros_publish_intent(self, function):
        self.function_ros_publish_intent = function

    def ros_publish_intent(self, text):
        if self.function_ros_publish_intent is not None:
            self.function_ros_publish_intent(text)
        else:
            ros_log(LOG_PREFIX + "Error Failed to publish on Topic, Ros Client not ready")

    def wait_until_shutdown(self):
        while not rospy.is_shutdown():
            sleep(1)

    def callback_ros_on_message(self, message, ros_topic):
        print("DEBUG ros", ros_topic, message)
        if ros_topic == RHASSPY_TO_ROS_STT:
            # print("[RosSubscriper]: topic: " + ros_topic)
            ros_log(LOG_PREFIX + "Ros Message: " + message.data)
            #RhasspyRestApiClient.say_tts(message.data)
            # if ros_topic == "":

    def callback_mqtt_on_connect(self, mqtt_client, user_data, flags, rc):
        mqtt_client.subscribe("#")
        ros_log(LOG_PREFIX + "MQTT Connected to {0} with result code {1}".format(MQTT_HOST, rc))

    def callback_mqtt_on_message(self, mqtt_client, user_data, msg):
        """ On MQTT message : callback """
        try: #"rhasspy/en/transition/WebrtcvadCommandListener"
            if msg.topic != "hermes/audioServer/default/audioFrame" and not "hermes/audioServer/default/playBytes" in msg.topic:
                0#print(msg.topic, msg.payload)

            if msg.topic == "hermes/asr/textCaptured":
                #print("DEBUG mqtt " + msg.topic, msg.payload)
                rospy.loginfo(msg.topic)
                data = msg.payload.decode("utf-8")
                dic = json.loads(data)
                stt_text = dic["text"]
                ros_log(LOG_PREFIX + " STT: " + stt_text)
                self.ros_publish_intent(stt_text)
        except Exception as e:
            ros_log(LOG_PREFIX + "Error MQTT on_message: " + str(e))

    def callback_local_rest_server_on_post(self, path, dict_data):
        print("DEBUG REST:", path, dict_data)
        if path == "/api/call":
            intent = dict_data["intent"]["name"]
            if len(intent) != 0:
                self.rest_api_client_1.say_tts("I ear, " + dict_data["text"])
                self.rest_api_client_1.say_tts("I understand the intent, " + dict_data["intent"]["name"])
                entities_list = dict_data["entities"]
                for entity in entities_list:
                    self.rest_api_client_1.say_tts("So, the " + entity["entity"] + " is " + entity["value"])

                if len(entities_list) == 0:
                    self.rest_api_client_1.say_tts("There is no indication")
            else:
                self.rest_api_client_1.say_tts("Intent not detected")


if __name__ == "__main__":
    """ Init services """
    callback_center = CallbackCenter()     # Will Process callback from MQTT and Ros

    ros_client1 = RosClient()    # Ros client read and write on Ros Topics
    hermes = HermesServices()    # Hermes services send and receive audio to Rhasspy by MQTT
    mqtt_client1 = MqttClient()  # MQTT client read and write on MQTT Topics (communicate with Rhasspy)
    rest_server = RhasspyRestApiServer(WEB_SERVER_1_PORT)  # Rest server to receive command from Rhasspy

    """ Connect all the services to the callback center """
    # Connect Ros Client callbacks to the "callback_center"
    ros_client1.set_on_message_callback(callback_center.callback_ros_on_message)
    # Connect the function "ros_publisher_intent" to the Roc Client "intent" topic publisher
    callback_center.set_function_ros_publish_intent(ros_client1.publish_intent)
    # Connect MQTT callbacks to the "callback_center"
    mqtt_client1.set_on_connect_callback(callback_center.callback_mqtt_on_connect)
    mqtt_client1.set_on_message_callback(callback_center.callback_mqtt_on_message)
    # Connect Rhasspy Local Rest Server "on_POST" callback
    rest_server.set_remote_post_callback(callback_center.callback_local_rest_server_on_post)

    # Start services
    rest_server.start()
    ros_client1.start()
    sleep(1)
    rhasspy_client = RhasspyRestApiClient(RHASSPY_1_REST_URM)
    rhasspy_client.say_tts("I'm listening")  # Used to sent TTS to Rhasspy
    mqtt_client1.start()

    callback_center.wait_until_shutdown()
    hermes.stop()
    rest_server.stop()

