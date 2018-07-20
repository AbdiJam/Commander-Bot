import discord
from discord.ext import commands
import asyncio
import random

command_prefix = "%"
TOKEN = "NDYzNTMwODUxNjM3MTMzMzEy.Dhx9Ww.m4uUWjlxC-nq3Il9locWmW-ESi0"
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
    print("The BOT has been activated")
    print(bot.User.name)
    print(bot.User.id)

@bot.event
async def on_message(messagelol):
    if message.content.lower() == "smile":
        await bot.send_message(message.channel, ":smiley:")
    elif message.content.lower() == "get buried":
        await bot.send_message(message.channel, ":skull_crossbones: :coffin:")
        

bot.run(TOKEN)
