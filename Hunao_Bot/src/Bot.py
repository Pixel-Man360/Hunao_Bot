import discord
import nest_asyncio

nest_asyncio.apply()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
     if message.author == client.user:
         return
     
     if message.content.startswith('Kire vatija?'):
         await message.channel.send('Ho kaka asi!')
         

client.run('ODg3NzA3ODU1MDU3MjA3MzU3.YUIEXQ.DMtNn64HImdC4Ei47lMdnH7-l7U')