import discord
import os
import sys
import json


def get_config():
    # grab ./config.json if it is existed
    config = None
    if os.path.exists('config.json'):
        # load config file
        with open('config.json', 'r') as f:
            config = json.load(f)
    return config


CONFIG = get_config()
if not CONFIG:
    message = "Please create a config.json config file in the same directory with remiderstat.py\n" \
              "Below is an example of the config.json file.\n"\
              "{\n" \
              "\t\"token\":\"<token>\",\n" \
              "\t\"channel\":\"<channel>\",\n" \
              "\t\"message\":\"<message>\"\n" \
              "}"
    print(message)
    sys.exit()

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    reminderchannel = client.get_channel(int(CONFIG['channel']))
    await reminderchannel.send(CONFIG['message'])
    await client.close()

client.run(CONFIG['token'])
