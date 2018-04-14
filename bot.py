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

#eval
@commands.command(pass_context=True, hidden=True, name='eval')
async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')
    

bot.run("tomato") # TOKEN
