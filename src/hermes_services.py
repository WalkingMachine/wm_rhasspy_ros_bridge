
#   Global import
import subprocess
from threading import Thread
from time import sleep
from rhasspy_utils import *

LOG_PREFIX = log_prefix("Hermes")


class BashProcess(Thread):
    def __init__(self, command, output_log):
        Thread.__init__(self)
        self.command = command
        self.output_log = output_log
        self.alive = True
        self.sp = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=False
        )
        self.start()
        ros_log(LOG_PREFIX + "Started " + str(self.command))

    def run(self):
        # Print the stdout
        while self.alive:
            # noinspection PyBroadException
            try:
                line = self.sp.stdout.readline()
                if len(line) == 0:
                    self.alive = False
                else:
                    if self.output_log:
                        print("[" + self.command + "] ", line)
            except Exception:
                self.alive = False

    def stop(self):
        self.alive = False
        # kill process
        try:
            self.sp.kill()
            self.sp.wait()
        except AttributeError:
            ros_log("Error while killing Hermes service: " + str(e))


class HermesServices:
    def __init__(self, output_log=False):
        self.s1 = BashProcess("hermes-audio-player", output_log)
        self.s2 = BashProcess("hermes-audio-recorder", output_log)

    def stop(self):
        self.s1.stop()
        self.s2.stop()
        ros_log(LOG_PREFIX + "Stopped")


# For testing purpose only
if __name__ == "__main__":
    h = HermesServices(output_log=True)
    sleep(5)  # Stop after N seconds
    h.stop()
    sleep(50)

