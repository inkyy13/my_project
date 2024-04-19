print("Hello World!")
import discord
import os
from dotenv import load_dotenv
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)
load_dotenv()
TOKEN - os.getenv("DISCORD_TOKEN")
@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run(TOKEN)
