import droplets
import config

yaml = config.YamlHelper('config.yaml')

token = yaml.cached_config.get('droplet-config').get('auth-token')

droplets.Droplet(token).wipe_droplets()
