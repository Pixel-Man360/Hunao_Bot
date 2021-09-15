import discord
#import requests
#import json
from discord.ext import commands

import nest_asyncio
nest_asyncio.apply()

#intents = discord.Intents.default()
#intents.members = True

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    

@client.command(pass_context = True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    
    else:
        await ctx.send("Vatija tumi voice channel e nai,\n You must be in a voice channel to run this command")
    
@client.command(pass_context = True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Ami jaiga. Leaving forever :)")
    
    else:
        await ctx.send("Ami ghumaitasi vatija")
       
          

client.run('ODg3NzA3ODU1MDU3MjA3MzU3.YUIEXQ.DMtNn64HImdC4Ei47lMdnH7-l7U')