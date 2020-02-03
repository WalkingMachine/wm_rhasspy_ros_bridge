
from threading import Thread
import paho.mqtt.client as mqtt
from rhasspy_utils import *

LOG_PREFIX = log_prefix("MQTT-Cli")


# Notes
# rospy.ROSInterruptException ???
# rospy.is_shutdown()
# m = msg.payload.decode("utf-8")
# self.mqtt_client.publish("hermes/hotword/default/detected", MQTT_ENABLE_LISTENING)


class MqttClient(Thread):
    def __init__(self):
        Thread.__init__(self)
        try:
            self.mqtt_client = mqtt.Client()
        except Exception as e:
            ros_log(LOG_PREFIX + "Error Can't create mqtt client. " + str(e))

    def set_on_connect_callback(self, callback):
        self.mqtt_client.on_connect = callback

    def set_on_message_callback(self, callback):
        self.mqtt_client.on_message = callback

    def run(self):
        try:
            connected = self.mqtt_client.connect(MQTT_HOST, MQTT_PORT, 60)  # connected if 0
        except Exception as e:
            ros_log(LOG_PREFIX + "Error Can't connect to mqtt server." + str(e))
        try:
            ros_log(LOG_PREFIX + "Started")
            while not rospy.is_shutdown():
                self.mqtt_client.loop()
            ros_log(LOG_PREFIX + "Stopped")
        except Exception as e:
            ros_log(LOG_PREFIX + "Error Can't connect to mqtt server. " + str(e))