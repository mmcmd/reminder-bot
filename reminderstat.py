import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    reminderchannel = client.get_channel(573214438086410240)
    await reminderchannel.send("Hey, it's the first of the month. Monthly reminder to type `s?t` in the <#%s> channel. <@%s>"% (362848533159870474, 109734116034940928))
    await client.close()



client.run('TOKEN')
