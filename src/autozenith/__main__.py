from autozenith import autozenith
from droplets import Droplet
import yaml
import os

if not os.path.exists('config.yaml'):
    open('config.yaml', 'x+').write("")

config = input("Have you already created a configuration before running this script? (y/n) ")

if config == 'y':

    autozenith()

elif config == 'n':

    autozenith_data = {
        'digital-ocean-token': input("Enter your DigitalOcean API token: "),
        'prefix': input("Enter the droplet's prefix: "),
        'datacenter': None,
        'amount': int(input("Enter the number of droplets: ")),
        'roleid': input("Enter the role ID: "),
        'discord-tokens': input("Enter your Discord tokens (comma-separated): ").split(','),
        'discord-channels': input("Enter your Discord channels (comma-separated): ").split(',')
    }

    Droplet(autozenith_data['digital-ocean-token']).return_regions()
    autozenith_data['datacenter'] = input("The above slugs are available to be used. Please select one (use nyc1 if you don't know which to use.): ")

    with open('config.yaml', 'w+') as file:
        yaml.dump(autozenith_data, file, default_flow_style=False, indent=4)

