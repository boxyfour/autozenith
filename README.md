# autozenith

> a way to automate the creation of proxies

# Installation

Go to the releases tab over [here](https://github.com/boxyfour/autozenith/releases/), download the zip, and unzip it. Afterwards, go to /scripts and run your respective script (.sh for linux, .bat for windowss

# Usage

First of all, make sure to fill out the `auth-token`! Digital ocean provides you with an apikey you can use to create / delete droplets which is what this requires.

Afterwards, provide `droplet-amount` (the amount of droplets / servers), `droplet-datacenter` (the closest datacenter / server location to you), and `droplet-prefix` (what the droplet should start with, e.g auth-zenith-0)

`discord-config` contains all of your discord bot tokens, channels, and role ids (you can leave a shared role-id) for each proxy. Leave each respective token and id for the bot!

Create the amount of tokens, channels, etc, for the discord bot, and place them into the config file like how the example says to.

Afterwards, go the the droplet homepage on digital ocean, and ssh into each droplet. Because you're creating a droplet from the api, you have to reset the root password. The password will be in your email.

Reset the password, log in, and run:
```tmux
cd /root/ZenithProxy
./launch
```
and press ctrl b + ctrl d. Do this for each instance.

# Credits

[rfresh2](https://github.com/rfresh2)'s [ZenithProxy](https://github.com/rfresh2/ZenithProxy)
