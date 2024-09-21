# importing os module for environment variables
import os

import discord
from discord.ext import commands

# importing necessary functions from dotenv library
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()

# accessing and printing value


# Create bot with command prefix and intents
intents = discord.Intents.default()
# intents = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def history(ctx, limit: int = 10):
    # Fetch message history from the channel where the command is used
    messages = await ctx.channel.history(limit=limit).flatten()

    # Print the messages for testing (you can later feed these into your model)
    for message in messages:
        print(f"{message.author}: {message.content}")

    await ctx.send(f"Retrieved {len(messages)} messages from history.")


bot.run(os.getenv("DISCORD_API_KEY"), reconnect=True)
# 274877978688
