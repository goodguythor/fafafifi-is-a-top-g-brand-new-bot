import os
import discord
from bot import reply

# Setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  
token = os.getenv("DISCORD_BOT_TOKEN")

bot = discord.Client(intents=intents)

# Login event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Message event
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_input = message.content.strip()
    response = reply(user_input)

    if response:
        await message.channel.send(response)

# Run the bot
bot.run(token)