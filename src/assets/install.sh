#!/bin/bash

# zenith download

cd /root 
mkdir ZenithProxy 
cd ZenithProxy 

wget https://github.com/rfresh2/ZenithProxy/releases/download/launcher-v3/ZenithProxy-launcher-linux-amd64.zip
unzip ZenithProxy-launcher-linux-amd64.zip

# autozenith

ZENITH_PATH='/root/ZenithProxy'

cd $ZENITH_PATH

git clone https://github.com/boxyfour/autozenith 

cd autozenith 

mv src/assets $ZENITH_PATH 

ls -a

cd "$ZENITH_PATH/assets"

python3 -m venv venv

venv/bin/pip install . 

