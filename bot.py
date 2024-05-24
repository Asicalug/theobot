import os
import sys
import time
import discord
from utils.settings import Settings
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import inspect

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(intents=intents)
bot.startTime = time.time()
bot.settings = Settings()

def reloadcog(path: str):
    bot.reload_extension(path)

load_dotenv()
TOKEN = os.getenv("TOKEN")
if TOKEN == None:
    print("TOKEN not found in the .env file.")
    exit()

def load_cogs():
    print("Loading commands")
    try:
        #admin
        bot.load_extension('commands.admin.todo')
        bot.load_extension('commands.admin.moderation.kick')
        bot.load_extension('commands.admin.moderation.ban')
        bot.load_extension('commands.admin.moderation.case')
        bot.load_extension('commands.admin.moderation.warnuser')

        #user
        bot.load_extension('commands.users.job.jobCommand')
        bot.load_extension('commands.users.ping')
        #tickets
        bot.load_extension("tickets.ticketCommands")

        print("Commands loaded")

        #ai
        bot.load_extension('ai.llama')

        #listeners
        print("Loading listeners")
        bot.load_extension('listeners.on_ready')
        print("Listeners Loaded")
        
    except Exception as e:
        print(f"could not load {e}")
        pass

load_cogs()

bot.run(TOKEN)