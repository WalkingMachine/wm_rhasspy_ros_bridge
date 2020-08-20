import requests
import json
# from SocketServer import TCPServer  # Depend of python version
from socketserver import TCPServer
from http.server import BaseHTTPRequestHandler
from threading import Thread
from time import sleep
from rhasspy_utils import *
from hermes_services import HermesProcess

# Global constant
RHASSPY_1_REST_URM = "http://0.0.0.0:12101"
RHASSPY_2_REST_URM = "http://0.0.0.0:12102"
WEB_SERVER_1_PORT = 8010
WEB_SERVER_2_PORT = 8011

API_SAY = "/api/text-to-speech?repeat=false&play=true"
API_LISTEN = "/api/listen-for-command?nohass=true"
API_RESTART = "/api/restart"
API_WAV_TO_INTENT = "/api/speech-to-intent?nohass=true"
API_TRAIN = "/api/train"
LOG_PREFIX = log_prefix("Rest-api")


# noinspection PyMethodMayBeStatic
class RhasspyRestApiClient:
    def __init__(self, url):
        self.url = url

    """ RhasspyRestApiClient is user to send request to the Rhasspy Server """
    def say_tts(self, tts_text):
        try:
            ros_log(LOG_PREFIX + ">>> Sending TTS: " + str(tts_text))
            r = requests.post(url=self.url + API_SAY, data=tts_text, timeout=1)
        except Exception as e:
            ros_log(LOG_PREFIX + "Error Failed to send TTS to Rhasspy: " + str(e))

    def listen(self):
        try:
            ros_log(LOG_PREFIX + ">>> Sending Command: start listening: ")
            r = requests.post(url=self.url + API_LISTEN, timeout=1)
        except Exception as e:
            ros_log(LOG_PREFIX + "Error Failed to send listen to Rhasspy: " + str(e))

    def restart(self):
        try:
            ros_log(LOG_PREFIX + ">>> Sending Command: restart Rhasspy")
            r = requests.post(url=self.url + API_RESTART, timeout=1)
        except Exception as e:
            ros_log(LOG_PREFIX + "Error Failed to send restart to Rhasspy: " + str(e))

    def train(self):
        try:
            ros_log(LOG_PREFIX + ">>> Sending Command: train intent")
            r = requests.post(url=self.url + API_RESTART, timeout=1)
        except Exception as e:
            ros_log(LOG_PREFIX + "Error Failed to send train to Rhasspy: " + str(e))

    def wav_to_intent(self):
        #try:
        ros_log(LOG_PREFIX + ">>> Sending Command: wav to intent")
        file = open("/home/jimmy/Desktop/hey_sara.wav", 'rb')
        dataa = file.read()
        jj = {"Accept": "application/json",
              "Accept-Language": "en-US,en;q=0.5",
              "Content-Type": "audio/wav",
              "Referer": "http://0.0.0.0:12102/api/",
              "DNT": "1"
              }

        r = requests.post(url=self.url + API_WAV_TO_INTENT, data=dataa, headers=jj, timeout=5)  # timeout=5,
        file.close()
        print(r.text)
        #except Exception as e:
        #    print("ERROR ",e)
        #    ros_log(LOG_PREFIX + "Error Failed to send TTS to Rhasspy: " + str(e))


class RhasspyRestApiServer(Thread):
    """ RhasspyRestApiClient is user to receive request from Rhasspy Server """
    def __init__(self, port):
        self.port = port
        Thread.__init__(self)
        self.remote_post_callback = None
        self.http_server = None

    def set_remote_post_callback(self, post_callback):
        self.remote_post_callback = post_callback

    def post_callback(self, path, dict_data):
        # Call the remote callback with the request
        if self.remote_post_callback is not None:
            self.remote_post_callback(path, dict_data)

    def stop(self):
        if self.http_server is not None:
            self.http_server.shutdown()
            self.http_server.server_close()

    def run(self):
        # noinspection PyMethodParameters
        class RequestHandler(BaseHTTPRequestHandler):
            """
            Setup the POST callback
                This is effectively not a beautiful code...
                Implement locally "BaseHTTPRequestHandler" to give the "self" to the callback
                To prevent "self" override, "_self" is used
            """
            # noinspection PyPep8Naming
            def do_POST(_self):
                content_length = int(_self.headers['Content-Length'])  # Get the size of data
                post_data = _self.rfile.read(content_length)  # Get the data itself
                dic = json.loads(post_data.decode())                   # Convert to dictionary
                self.post_callback(_self.path, dic)           # Call the remote callback
                dic["hass_event"] = {"event_type": "...", "event_data": {"key": "value"} }
                #print("XXX", json.dumps(dic))
                _self.send_header("Content-type", "application/json")
                _self.send_response(code=200)
                _self.wfile.write(json.dumps(dic).encode())
                _self.end_headers()


        # Start the Http server
        self.http_server = TCPServer(("", self.port), RequestHandler, bind_and_activate=False)
        self.http_server.allow_reuse_address = True
        # noinspection PyBroadException
        try:
            self.http_server.server_bind()
            self.http_server.server_activate()
            print("serving at port", self.port)
            self.http_server.serve_forever()
        except:
            self.http_server.shutdown()
            self.http_server.server_close()


##############################################################
# Tests
def test_send_wave():
    _rhasspy_client = RhasspyRestApiClient(RHASSPY_2_REST_URM)
    _rhasspy_client.wav_to_intent()


def test_():
    def callback_example(path, dict_data):
        print("Example Callback: ", path, dict_data)
        # RhasspyRestApiClient.say_tts(dict_data["text"])  # ! Must start "bash hermes-audio-player" before
        if "stop" in dict_data["text"]:
            rhasspy_client.say_tts("I'm stopping")  # ! Must start "bash hermes-audio-player" before
            rhasspy_client.listen()
        else:
            rhasspy_client.listen()

    hermes = HermesProcess()    # Hermes services send and receive audio to Rhasspy by MQTT

    rhasspy_client = RhasspyRestApiClient(RHASSPY_2_REST_URM)
    rest_server = RhasspyRestApiServer(WEB_SERVER_2_PORT)
    rest_server.set_remote_post_callback(callback_example)
    rest_server.start()
    sleep(2)
    rhasspy_client.say_tts("test text")  # ! Must start "bash hermes-audio-player" before
    rhasspy_client.listen()  # ! Must start "bash hermes-audio-recorder" before
    for n in range(100):
        sleep(1)
    #sleep(5)
    #RhasspyRestApiClient.restart()
    #sleep(600)

    hermes.stop()
    rest_server.stop()


# Tests purpose only
if __name__ == '__main__':
    test_send_wave()
