from pydo import Client
import json

IMAGE="ubuntu-24-10-x64"
SIZE="s-1vcpu-1gb"

class Droplet:

    def __init__(self, token):
        self.client = Client(token)

    def return_projects(self):
        if not self.client:
            return
        
        return self.client.droplets.list()



    def wipe_droplets(self):
        projects = self.return_projects()
        ids = []
        for droplet in projects.get("droplets"):
            ids.append(droplet.get('id'))

        if len(ids) == 0:
            print("No projects to wipe!")
            return

        for id in ids:
            print(f"Destroying id: {id}")
            self.client.droplets.destroy(int(id))
    
    def return_regions(self):
        regions = []
        region_data = self.client.regions.list().get('regions')
        for region in region_data:
            print(region.get('slug'), "available: ", region.get('available'))
        
        return regions

    def create_droplet(self, name, datacenter, cloud_data):

        data = {
            "name": name,
            "region": datacenter,
            "size": SIZE,
            "image": IMAGE,
            "user_data": cloud_data,
        }
        
        resp = self.client.droplets.create(body=data)

        return resp