# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('##'):
        word = message.content
        if(word.split('##')[1].isnumeric()):
            target = int(word.split('##')[1])
            if(target >= 0 and target < 256):
                result = f'{target:08b}'
                response = '`result: ' + result[0:4] + ' ' + result[4:8] + '`'
            else:
                response = '`Your number is out of range.`'
        else:
            response = '`This is not a number. !!`'
        await message.channel.send(response)

client.run(TOKEN)
