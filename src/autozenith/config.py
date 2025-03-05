import yaml
import os

ASSETS_DIR = os.path.join(os.getcwd(), 'src', 'assets')
CLOUD_DIR = os.path.join(ASSETS_DIR, "cloud-init.yaml")

class YamlHelper:
    def __init__(self, filename):
        self.cached_config = yaml.full_load(open(filename))
        self.cloud_config = open(CLOUD_DIR, 'r').read()

    def return_fields(self, index):

        discord_fields = {
            "channel": self.cached_config.get("discord-config").get("discord-channels")[index],
            "token": self.cached_config.get("discord-config").get("discord-tokens")[index],
            "role": self.cached_config.get("discord-config").get("discord-role")
        }

        return discord_fields

    def digitalocean(self):
        root = self.cached_config.get("droplet-config")
        digitalocean = {
            "token": root.get("auth-token"),
            "prefix": root.get("droplet-prefix"),
            "datacenter": root.get("droplet-datacenter"),
            "amount": root.get("droplet-amount")
        }
    
        return digitalocean
    
    
    def edit_config(self, index):
        fields = self.return_fields(index)
        
        channel = fields["channel"]
        token = fields["token"]
        role = fields["role"]

        modified_cloud_config = self.cloud_config
        modified_cloud_config = modified_cloud_config.replace('TOKEN', token)
        modified_cloud_config = modified_cloud_config.replace('CHANNEL', str(channel))
        modified_cloud_config = modified_cloud_config.replace('ROLE', str(role))

        

        return modified_cloud_config