# MessageBot by Infinite

import discord
from .utils import checks
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

# to expose to the eval command
import datetime
from collections import Counter

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

#eval
@commands.command(pass_context=True, hidden=True)
@checks.is_owner()
async def eval(self, ctx, *, code : str):
        """Evaluates code."""
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.server,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await self.bot.say(python.format(type(e).__name__ + ': ' + str(e)))
            return

        await self.bot.say(python.format(result))
    

bot.run("NDM0MjkyMTM4MzIzNDc2NDgx.DbOazA.mfm51kZvoTXV_tq1d6H2eLn_iKM") # TOKEN
