import requests
import json
import os
import subprocess
import sys

import os
import subprocess

def create_systemd_service(service_name, command):
    # Define the service unit content
    service_content = f"""[Unit]
Description={service_name}
After=network.target

[Service]
ExecStart={command}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""

    service_path = f"/etc/systemd/system/{service_name}.service"

    if os.path.exists(service_path):
        print(f"The service file {service_name}.service already exists.")
        return

    with open(service_path, 'w') as f:
        f.write(service_content)

    print(f"Service file created at {service_path}")

    try:
        subprocess.run(['sudo', 'systemctl', 'daemon-reload'], check=True)
        print("Systemd daemon reloaded.")

        subprocess.run(['sudo', 'systemctl', 'enable', service_name], check=True)
        print(f"Service {service_name} enabled.")

        subprocess.run(['sudo', 'systemctl', 'start', service_name], check=True)
        print(f"Service {service_name} started.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while managing the systemd service: {e}")
        return

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

    config_file_path = os.path.join(target_dir, 'launch_config.json')

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


service_name = "autozenith"
command = "/bin/bash /root/ZenithProxy/launch.sh"

create_systemd_service(service_name, command)
