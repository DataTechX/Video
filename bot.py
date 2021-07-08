
import discord
from discord.ext import commands 
import os

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Test"))
    print('Bot Ready')



client.run('DISCORD BOT TOKEN')