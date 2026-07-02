import discord
import requests
import os
from dotenv import load_dotenv

MEME_CATEGORIES = {
    "memes": "memes",
    "dank": "dankmemes",
    "funny": "funny",
    "wholesome": "wholesomememes",
    "programming": "ProgrammerHumor",
    "linux": "linuxmemes",
    "pcmasterrace": "pcmasterrace",
    "gaming": "gaming",
    "minecraft": "MinecraftMemes",
    "valorant": "ValorantMemes",
    "cs2": "GlobalOffensive",
    "league": "LeagueOfMemes",
    "anime": "Animemes",
    "animememes": "animememes",
    "football": "soccermemes",
    "nba": "nbamemes",
    "formula1": "formula1",
    "cricket": "CricketShitpost",
    "college": "CollegeMemes",
    "school": "schoolmemes",
    "gym": "GymMemes",
    "cats": "cats",
    "dogs": "dogpictures",
    "dark": "darkmemers",
    "pakistan": "pakistanimemes",
    "history": "HistoryMemes",
    "science": "ScienceMemes",
    "starwars": "PrequelMemes",
    "marvel": "marvelmemes",
    "lotr": "lotrmemes",
    "cars": "carmemes"
}

load_dotenv()
def get_meme(category):
    subreddit = MEME_CATEGORIES[category]
    response = requests.get(f"https://meme-api.com/gimme/{subreddit}")
    json_data = response.json()
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")
        print("Bot started!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello guyzz!')


        if message.content.startswith("$meme"):
            parts = message.content.split()
            if len(parts) != 2:
                await message.channel.send(
                    "\n".join(MEME_CATEGORIES.keys())
                )
                return 
            category = parts[1].lower()
            
            
            if category not in MEME_CATEGORIES:
                await message.channel.send(
                    f"Available categories:\n"
                    f"{", ".join(MEME_CATEGORIES.keys())}"
                )
                return 
            
            
            meme = get_meme(category)
            
            await message.channel.send(meme)

        if self.user in message.mentions:
            print("Mention detected!")
            meme_url = get_meme("pakistan")
            print(meme_url)
            await message.channel.send(meme_url)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
TOKEN = os.getenv("Discord_Token")

print("TOKEN =", TOKEN)

client.run(TOKEN)
