import discord
import random

TOKEN = "OTY4MjI5OTM1MzgwNTk0NzU4.Ymb0ZQ.7y1oZM0TMqryVEWIjSWhcNhmTyg"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run(TOKEN)


