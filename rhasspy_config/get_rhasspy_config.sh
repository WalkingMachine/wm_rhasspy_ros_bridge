#!/bin/sh
# Sudo check
if ! [ $(id -u) = 0 ]; then
   echo "Error, run as root"
   exit 1
fi
# Copy config to this folder
this_dir=`basename $PWD`
if [ $this_dir != "rhasspy_config" ]; then
   echo "Error, Please run in rhasspy_config directory"
  exit 1
fi
# Copy files, rsync is like cp with exclude
path=~/.config/rhasspy/profiles
rsync -avr \
 --exclude=profiles/fr \
 --exclude=profiles/en/kaldi \
 --exclude=*/googlewavenet \
 $path ./
# set owner, prevent git trouble ($SUDO_USER get the real user using sudo)
echo "set owner to profiles/"
sudo chown -R $SUDO_USER:$SUDO_USER profiles/
