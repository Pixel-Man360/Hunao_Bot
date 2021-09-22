import os
import youtube_dl

from discord.ext import commands
from keep_alive import keep_alive



from Music import Music

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''

bot = commands.Bot(command_prefix='kaka ')
bot.add_cog(Music(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    
@bot.event
async def on_message(message):
     message.content = message.content.lower()
     await bot.process_commands(message)
    
keep_alive()
bot.run(os.getenv("TOKEN"))


