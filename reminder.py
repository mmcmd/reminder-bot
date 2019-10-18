import discord
import os
import sys
import json
import argparse


def get_config(config_path):
    print(config_path)
    # grab ./config.json if it is existed
    config = None
    if os.path.exists(config_path):
        # load config file
        with open(config_path, 'r') as f:
            config = json.load(f)
    return config


def main():
    argparser = argparse.ArgumentParser(
        formatter_class=lambda prog:
        argparse.HelpFormatter(prog, max_help_position=40))
    argparser.add_argument("-c", "--config", help="config file path", type=str,
                           default="./config/config.json")
    args = argparser.parse_args()
    print(args.config)
    CONFIG = get_config(args.config)
    if not CONFIG:
        message = "Please create a /config/config.json config file in the same"\
                  "directory with remiderstat.py\n" \
                  "Below is an example of the config.json file.\n"\
                  "{\n" \
                  "\t\"token\":\"your-token\",\n" \
                  "\t\"channel\":\"your-channel-id\",\n" \
                  "\t\"message\":\"your-message\"\n" \
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


if __name__ == '__main__':
    main()
