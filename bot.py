# MessageBot by Infinite
#!/usr/bin/python

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix= '~')
bot.remove_command("help") # Got my own help boi

@bot.event
async def on_ready():
    print ("Online boi :P") # Indicates that the bot is online
    await bot.change_presence(game=discord.Game(name='wip - eta son')) # Sets the Playing status (Presence) 

#help
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="help", colour=discord.Colour(0x15a56b), url="https://messagebot.evanw.uk", description="This bot was made to make annoucements more unified but can also be used for other purposes")

    embed.set_image(url="https://cdn.discordapp.com/avatars/434292138323476481/924aa0d98f2b6a9f6169c9975b8b5f17.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/434292138323476481/924aa0d98f2b6a9f6169c9975b8b5f17.png")
    embed.set_author(name="MessageBot", url="https://messagebot.evanw.uk", icon_url="https://cdn.discordapp.com/avatars/434292138323476481/924aa0d98f2b6a9f6169c9975b8b5f17.png")
    embed.set_footer(text="© Evan Walters (Infinite) 2018", icon_url="https://cdn.discordapp.com/avatars/434292138323476481/924aa0d98f2b6a9f6169c9975b8b5f17.png")

    embed.add_field(name="`~msg`", value="Can be used by all users\nEXAMPLE : `~msg #general This is a message`\n OUTPUT (IN GENERAL): `This is a message` ")
    embed.add_field(name="`~announce`", value="Can be used by admins\nEXAMPLE : `~announce #announcements everyone This is a message`\n OUTPUT (IN ANNOUNCEMENTS): `@everyone This is a message`")
    embed.add_field(name="`~ping`", value=":ping_pong:")

    await bot.say(embed=embed)

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


    

with open("token.txt") as f:
    token = f.read().strip()
# now use token

bot.run(token)  
