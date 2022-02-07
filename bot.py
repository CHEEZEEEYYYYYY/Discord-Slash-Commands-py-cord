import discord #import your packages
from discord.ext import commands
from discord_slash import SlashCommand 
import aiohttp

intents = discord.Intents.all() #make sure that all Priveleged Gateway Intents (Presence Intent, Server Member Intents, and Message Contents Intent) are on to use this line
client = commands.Bot(command_prefix="?", intents=intents)
slash = SlashCommand(client, sync_commands=True)

client.event
async def on_ready():
  print("The bot is now Online!!")#This will print out that your bot is successfully deployed/online
  
#MAKING HELLO COMMAND 
@slash.slash(description="Hi", guild_ids=["YOUR SERVER ID"])#make sure to remove guild_ids if you want to make it global but it will take 1 hour to register your slash command. If you want to test the command right away make sure to put your guild ID by going to you server settings and go to widget and copy your Server ID on guild_ids=[YOUR SERVER ID]
async def hello(ctx):
  await ctx.reply(f"Hello ther {ctx.author.mention} nice to meet you :slight_smile:")
  

client.run('YOUR BOT TOKEN')
             
