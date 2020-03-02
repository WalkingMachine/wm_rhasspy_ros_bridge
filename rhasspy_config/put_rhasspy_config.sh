#!/bin/bash
# Sudo check
if ! [ $(id -u) = 0 ]; then
   echo ">> Error, run as root"
   exit 1
fi
# Copy config to this folder
this_dir=`basename $PWD`
if [ $this_dir != "rhasspy_config" ]; then
   echo ">> Error, Please run in rhasspy_config directory"
  exit 1
fi

# Copy files
echo ">> Coppy config to Rhasspy"
sudo cp -r profiles ~/.config/rhasspy/
echo ">> Extract and prepare Kaldi library"

echo extract kaldi

echo ">> * Expected error, tar: kaldi/model/model/utils: Cannot open: File exists"
echo ">> * Eexpected error, tar: Exiting with failure status due to previous errors"
cd ~/.config/rhasspy/profiles/en/
sudo tar -xf download/en_kaldi-zamia.tar.gz

