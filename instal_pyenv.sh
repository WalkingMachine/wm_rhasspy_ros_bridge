# Check if in the right folder
this_dir=`basename $PWD`
if [ $this_dir != "wm_rhasspy_ros_bridge" ]; then
   echo "Error, Please run in wm_rhasspy_ros_bridge directory"
  exit 1
fi
mkdir .pyenv
python3.6 -m venv .pyenv
source .pyenv/bin/activate
pip3 install wheel paho-mqtt pyyaml rospkg requests websockets netifaces