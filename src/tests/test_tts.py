from threading import Thread

text = [
    "i'm not able to get the security code",
    "there is no room in the moon",
    "you got the bad jack",
    "turn on the libre stream",
    "security breach in the basement",
    "i sound like a baloune",
    "i'm new here",
    "Threat detected on the system 5",
    "Please wait until i finish the scan",
    "Error",
    "System failure",
    "A I training",
    "learning",
    "I'm learning"
]

text1 = [
    "Error",
    "System failure",
    "A I training",
    "learning",
    "I'm learning"
]


class TestsThread(Thread):
    def __init__(self, mqtt_client):
        Thread.__init__(self)
        self.mqtt_client = mqtt_client.mqtt_client
        self.start()

    def run(self):
        rospy.loginfo("[Snips_Supervisor] run")
        while not rospy.is_shutdown():
            try:
                print("try...")
                # self.mqtt_client.publish("/api/text-to-speech", '{"text": "Hello"}')
                tt = text1[random.randint(0, len(text1) - 1)]
                RhasspyRestApi.say_tts(tt)
            except Exception as e:
                pass
            sleep(2)


TestsThread(mqtt_client1)
