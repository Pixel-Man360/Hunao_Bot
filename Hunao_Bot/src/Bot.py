import discord
#import requests
#import json
from discord.ext import commands

import nest_asyncio
nest_asyncio.apply()

client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    
    
@client.event
async def on_message(message):
    musicTextChannel = client.get_channel(748512761503416400)
    if message.content.lower().startswith('-'):
        if message.channel.id == musicTextChannel.id:
            await client.process_commands(message)
        else:
            await message.channel.send('music channel e command dao. Hisab bujho na? dudu khao?')
    

@client.command(pass_context = True)
async def join(ctx):
    
    if ctx.author.voice and not ctx.voice_client:
        channel = ctx.author.voice.channel
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