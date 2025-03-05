import config
import droplets

class autozenith:
    def __init__(self):
        self.yaml = config.YamlHelper('config.yaml')

        digitalocean_data = self.yaml.digitalocean()


        self.droplets = droplets.Droplet(digitalocean_data.get("token"))

        self.create_droplets(digitalocean_data.get("amount"))
    
    def create_droplets(self, amount):

        for i in range(amount):
            digitalocean = self.yaml.digitalocean()
            cloudconfig = self.yaml.edit_config(i)

            name = f"{digitalocean["prefix"]}{i}"

            print(f"Creating droplet: {name}")

            self.droplets.create_droplet(name, digitalocean["datacenter"], cloudconfig)