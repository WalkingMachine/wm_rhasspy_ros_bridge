# Check if in the right folder
this_dir=`basename $PWD`
if [ $this_dir != "wm_rhasspy_ros_bridge" ]; then
   echo "Error, Please run in wm_rhasspy_ros_bridge directory"
  exit 1
fi

sudo apt-get install -y python3-venv
mkdir .pyenv
python3 -m venv .pyenv
source .pyenv/bin/activate
pip3 install wheel --user
pip3 install pyyaml --user
pip3 install paho-mqtt pyyaml roslibpy rospkg requests netifaces websocket_client --user

