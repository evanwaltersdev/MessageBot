# MessageBot by Infinite

import discord
import re
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix= '~')

@bot.event
async def on_ready():
    print ("Online boi :P") # Indicates that the bot is online
    await bot.change_presence(game=discord.Game(name='wip - eta son')) # Sets the Playing status (Presence) 

# Ping Command
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")


# The exclusive message command
@bot.command(pass_context=True)
async def msg(ctx, channel : discord.Channel, *, content): # Converts a regular #channel to a specialised ID
    await bot.send_message(channel, content.replace("`", "")) # This sends the message but removes ` that is used for code. This is so if you use the bot for announcemnts you can `@everyone` and the bot mentions @everyone to avoid double ping

@bot.command(pass_context=True)
async def announce(ctx, channel : discord.Channel, role : discord.Role, *, content):
    if not channel.permissions_for(ctx.message.author).send_messages:
        return
    msg = "{} {}".format(role.mention, content.replace("`", ""))
    await bot.send_message(channel, msg)
    

bot.run("pickle") # TOKEN
