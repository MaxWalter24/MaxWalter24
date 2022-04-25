import discord
import random
from SMSScript import *

TOKEN = "DELETETHISOTY4MjI5OTM1MzgwNTk0NzU4.Ymb0ZQ.PnjOoCwMK7pVOmYEU-N11_3ucz4"

client = discord.Client()

@client.event
async def on_ready():
    print("before")
    print('We have logged in as {0.user}'.format(client))
    print("after")
    
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'general':
        email_alert("Discord",user_message,"8155756424@txt.att.net")
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you alter {username}!')
            return

client.run(TOKEN)


