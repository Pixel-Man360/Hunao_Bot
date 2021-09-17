import discord
from discord.ext import commands
import youtube_dl
import os
import nest_asyncio
from keep_alive import keep_alive 
nest_asyncio.apply()

client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print('Logged as {0.user}'.format(client))
    
    
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
            

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
        
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    
@client.command(pass_context = True)
async def leave(ctx):
    
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Ami jaiga. Leaving forever :)")
    
    else:
        await ctx.send("Ami ghumaitasi vatija")
my_secret = os.environ['TOKEN']

keep_alive()
client.run(my_secret)