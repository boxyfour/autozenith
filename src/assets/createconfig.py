import requests
import json
import os
import sys

# TODO: FIX


current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

if not os.path.exists(os.path.join(parent_dir, 'launch_config.json')):
    with open("launch_config.json", "x") as f:
        f.write("")

if not os.path.exists(os.path.join(parent_dir, 'config.json')):
    with open("launch_config.json", "x") as f:
        f.write("")

def launch_config():
    config = {}
    release_channel = "linux"
    minecraft_version = "1.21.0"
    
    config["auto_update"] = True
    config["auto_update_launcher"] = True
    config["release_channel"] = release_channel + "." + minecraft_version
    config["version"] = "0.0.0"
    config["local_version"] = "0.0.0"
    config["repo_owner"] = "rfresh2"
    config["repo_name"] = "ZenithProxy"

    os.chdir(parent_dir)

    with open("launch_config.json", "w") as f:
        f.write(json.dumps(config, indent=2))

        print("launch_config.json written successfully!")

def create_config(token, channel, role, relaychannel):
    config = {}
    
    if relaychannel == None:
        print("woah")
        
    ip = requests.get("https://api.ipify.org", timeout=10)

    proxy_address = ip.text

    config["server"] = {
        "bind": {
            "port": 25565,
        },
        "proxyIP": proxy_address,
    }

    if token:
        config["discord"] = {
            "enable": True,
            "token": token,
            "channelId": channel,
            "accountOwnerRoleId": role,
        }
        if relaychannel:
            config["discord"]["chatRelay"] = {
                "enable": True,
                "channelId": relaychannel
            }

    os.chdir(parent_dir)

    with open("config.json", "w") as f:
        f.write(json.dumps(config, indent=2))

        print("config.json written successfully!")


args = sys.argv

for i in args:
    print(i)

if len(args) > 5:
    relay = args[4]
else:
    relay = None

launch_config()
create_config(args[1], args[2], args[3], relay)
