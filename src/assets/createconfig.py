import requests
import json
import os
import sys

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

    target_dir = '/root/ZenithProxy/'

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    config_file_path = os.path.join(target_dir, 'config.json')

    with open(config_file_path, "w") as f:
        f.write(json.dumps(config, indent=2))

    print(f"config.json written successfully to {config_file_path}")


args = sys.argv

for i in args:
    print(i)

if len(args) > 5:
    relay = args[4]
else:
    relay = None

create_config(args[1], args[2], args[3], relay)
