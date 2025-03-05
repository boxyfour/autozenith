#!/bin/bash

# zenith download

cd /root 
mkdir ZenithProxy 
cd ZenithProxy 

wget https://github.com/rfresh2/ZenithProxy/releases/download/launcher-v3/ZenithProxy-launcher-linux-amd64.zip
unzip ZenithProxy-launcher-linux-amd64.zip

# autozenith

ZENITH_PATH='/root/ZenithProxy'

cd "$ZENITH_PATH/autozenith"

python3 -m venv venv

/root/ZenithProxy/autozenith/src/assets/venv/bin/pip install . 

cd /root/ZenithProxy 
git clone https://github.com/boxyfour/autozenith 
cd autozenith 
mv src/assets $ZENITH_PATH 

cd $ZENITH_PATH
rm -r autozenith

assets/install.sh