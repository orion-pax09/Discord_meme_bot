import discord
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = response.json()
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello guyzz!')
        
        if self.user in message.mentions:
            meme_url = get_meme()
            await message.channel.send(meme_url)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
TOKEN = os.getenv("Discord_Token")

print("TOKEN =", TOKEN)

client.run(TOKEN)
