from ctypes.wintypes import MSG
from distutils.util import change_root
from unicodedata import name
import discord
import random
import asyncio
import os
import json
import urllib
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
from io import BytesIO

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix = '?', intents=intents)
status = cycle(['Use %help', 'Status 2', 'Status 3', 'Status 4', 'Status 5'])

@bot.event
async def on_ready():
    print('Bot is online')

@bot.command(name='8ball') # register bot commands using this decorator
async def eightball(ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful",
            "OUTRIGHT DISGUSTING!",
            "I'm 8ball, not deal with your shit ball.",
            "Dont sass me, BITCH!",
            "I'm busy doing your mom, dont you see!",
            "No, sugma balls instead",
            "Honestly, who cares?",
            "Yes, perhaps",
            "My visions are clouded, ask again.",
            "The universe says 'yes'... ",
            "Signs point to a yes!",
            "NO!, Ew, I'd rather die",
            "UNACCEPTABLE!!",
            "YESSSS!!! :GRIN:",
            "I will ignore you so hard you will start doubting your existence.",
            "Ask god, why ask me? HUH!?",
            "Yesssssssssssssss *slips in parseltongue*"
        ]
        embed = discord.Embed(title="8ball", description=f"Question: {question}\nAnswer: {random.choice(responses)}", color=0x00ff00)
        await ctx.send(embed=embed)

@eightball.error
async def eightball_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(title="Error", description="You need to ask a question!", color=0x00ff00)
                await ctx.send(embed=embed, delete_after=5)

@bot.command()
async def hack(ctx, *, member: discord.Member = None):
        quotes = ["Porn is fun.", "Cats are ew.", "I wanna be a stripper", "John Cena is hot af",
                  "Johhny Sins is my love :smirk:", "I am gay :star_struck: ", "I got no bitches :cry:",
                  "I am horny 24/7 :smirk:"]
        randomWord = ["Cum", "Pussy", "Cake", "Minecraft", "PvP", "Kekw", "UwU"]
        ipAddress = ["59.221.102.32", "150.153.114.26", "57.27.235.106", "158.93.182.76", "81.245.206.76"]
        hack1 = discord.Embed(title=f"**Hacking {member.name} now...**", description=f"Hacking {member.name} now...",
                              color=0xffa980)
        hack2 = discord.Embed(title=f"**Running Command Hack**", description=f"Finding Discord login...(2fa bypassed)",
                              color=0xffa980)
        hack3 = discord.Embed(title=f"**Running Command Hack**",
                              description=f"Fetching important DMS with closest friends... (if you got any that is :rofl:)",
                              color=0xffa980)
        hack4 = discord.Embed(title=f"**Running Command Hack**",
                              description=f""" **Last DMs** '{random.choice(quotes)}' """, color=0xffa980)
        hack5 = discord.Embed(title=f"**Running Command Hack**", description=f"Finding most used word...",
                              color=0xffa980)
        hack6 = discord.Embed(title=f"**Running Command Hack**",
                              description=f"""Most Used Word = '{random.choice(randomWord)}'""", color=0xffa980)
        hack7 = discord.Embed(title=f"**Running Command Hack**",
                              description=f"Injecting Trojan Virus into the discriminator #{member.discriminator}",
                              color=0xffa980)
        hack8 = discord.Embed(title=f"**Running Command Hack**",
                              description=f"Virus injected successfully! Running the virus code...", color=0xffa980)
        hack9 = discord.Embed(title=f"**Running Command Hack**",
                              description=f"Downloading Salwyrr account passwords...", color=0xffa980)
        hack10 = discord.Embed(title=f"**Running Command Hack**",
                               description=f"Nuking servers owned by {member.name}#{member.discriminator}",
                               color=0xffa980)
        hack11 = discord.Embed(title=f"**Running Command Hack**", description=f"Finding IPv4 Address...", color=0xffa980)
        hack12 = discord.Embed(title=f"**Running Command Hack**",
                               description=f"**IPv4 Address**: {random.choice(ipAddress)}", color=0xffa980)
        hack13 = discord.Embed(title=f"**Running Command Hack**", description=f"Stealing stored passwords...",
                               color=0xffa980)
        hack14 = discord.Embed(title=f"**Running Command Hack**", description=f"Selling data to Zachery#3376...",
                               color=0xffa980)
        hack15 = discord.Embed(title=f"**Running Command Hack**",
                               description=f"Reporting account to Discord for DDoS and breaking Discord ToS...",
                               color=0xffa980)
        hack16 = discord.Embed(title=f"**Running Command Hack**",
                               description=f"Downloading Google Search History... (Bro, this shit is susssyyy )",
                               color=0xffa980)
        hack17 = discord.Embed(title=f"**Completed Command Hack**",
                               description=f"Finished hacking {member.name}#{member.discriminator}", color=0xffa980)
        message = await ctx.send(embed=hack1, delete_after=50)

        await asyncio.sleep(1)
        await message.edit(embed=hack2)
        await asyncio.sleep(2)
        await message.edit(embed=hack3)
        await asyncio.sleep(2)
        await message.edit(embed=hack4)
        await asyncio.sleep(2)
        await message.edit(embed=hack5)
        await asyncio.sleep(2)
        await message.edit(embed=hack6)
        await asyncio.sleep(2)
        await message.edit(embed=hack7)
        await asyncio.sleep(2)
        await message.edit(embed=hack8)
        await asyncio.sleep(2)
        await message.edit(embed=hack9)
        await asyncio.sleep(2)
        await message.edit(embed=hack10)
        await asyncio.sleep(2)
        await message.edit(embed=hack11)
        await asyncio.sleep(2)
        await message.edit(embed=hack12)
        await asyncio.sleep(2)
        await message.edit(embed=hack13)
        await asyncio.sleep(2)

        await message.edit(embed=hack14)
        await asyncio.sleep(2)
        await message.edit(embed=hack15)
        await asyncio.sleep(2)
        await message.edit(embed=hack16)
        await asyncio.sleep(2)
        await message.edit(embed=hack17)
        await asyncio.sleep(2)

@hack.error
async def hack_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"**Please use **?hack (Username)**",color=0xff6161)
            await ctx.send(embed=embed, delete_after=15)

@bot.command()
async def nuke(ctx, *, member: discord.Member = None):

        nuke1 = discord.Embed(title=f"**Nuking this server now...**", description=f"Nuking in 5...",
                              color=0xffa980)
        nuke2 = discord.Embed(title=f"**Running Command Nuke**", description=f"Nuking in 4...",
                              color=0xffa980)
        nuke3 = discord.Embed(title=f"**Running Command Nuke**",
                              description=f"Nuking in 3...",
                              color=0xffa980)
        nuke4 = discord.Embed(title=f"**Running Command Nuke**",
                              description=f"Nuking in 2...", color=0xffa980)
        nuke5 = discord.Embed(title=f"**Running Command Nuke**", description=f"Nuking in 1...", color=0xffa980)

        nuke6 = discord.Embed(title=f"**Nuke Completed **", description=f"Nuke Completed || This is a joke ||", color=0xffa980)        

        message = await ctx.send(embed=nuke1)

        await asyncio.sleep(1)
        await message.edit(embed=nuke2)
        await asyncio.sleep(1)
        await message.edit(embed=nuke3)
        await asyncio.sleep(1)
        await message.edit(embed=nuke4)
        await asyncio.sleep(1)
        await message.edit(embed=nuke5)
        await asyncio.sleep(1)
        await message.edit(embed=nuke6)
        await asyncio.sleep(1)        

@nuke.error
async def nuke_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"**Please use **?nuke**",color=0xff6161)
            await ctx.send(embed=embed, delete_after=15)    

@bot.command()
async def say(ctx, *, saymsg):
        embed = discord.Embed(title=f"**{ctx.author}**", description=f"{saymsg}", color=discord.Colour.random())
        await ctx.send(embed=embed)

@say.error
async def say_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"**Please use **?say (Message)**",color=0xff6161)
            await ctx.send(embed=embed, delete_after=15)   
            
@bot.command(name = "meme", description = "Sends a meme")
async def meme(ctx):
        memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

        memeData = json.load(memeApi)

        memeUrl = memeData['url']
        memeName = memeData['title']
        memePoster = memeData['author']
        memeSub = memeData['subreddit']
        memeLink = memeData['postLink']

        embed= discord.Embed(title=memeName)
        embed.set_image(url=memeUrl)
        embed.set_footer(text=f"Meme by: {memePoster} | Post: {memeLink}")
        await ctx.send(embed=embed)

@bot.command(name='Ping')
async def ping(ctx):
        embed = discord.Embed(title="Pong!", description=f"My current latency is **{round(bot.latency * 1000)} milliseconds**.", color=0x00ff00)
        await ctx.send(embed=embed)
        
@bot.command()
async def invite(ctx):
        embed=discord.Embed(title=f"**Bot Invite**",description=f"Add me to your server by clicking this link! **https://bit.ly/3xPJHMg**",color=0xffcd85)        
        await ctx.send(embed=embed)            

@bot.event
async def on_command_error(ctx, error):
        embed = discord.Embed(title=f"**Unknown Command**", description=f"**Please use ?help**", color=0xff6161)
        sayyEmbed = discord.Embed(title=f"**{ctx.author.name} Issued An Unknown Command**", description=f"**Please tell them to use ?help**", color=0xff6161)
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=embed, delete_after=3)
            await bot.get_channel(984047964110610473).send(embed=sayyEmbed)    

@bot.event
async def on_message_delete(message):
        z = bot.get_channel(984047964110610473)
        embed = discord.Embed(title=f"{message.author}'s Message was Deleted",
                              description=f"Deleted Message: {message.content}\nAuthor: {message.author.mention}\nLocation: {message.channel.mention}",
                              timestamp=datetime.now(), color=discord.Colour.red())
        await z.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
        z = bot.get_channel(984047964110610473)
        embed = discord.Embed(title=f"{before.author} Edited Their Message",
                              description=f"Before: {before.content}\nAfter: {after.content}\nAuthor: {before.author.mention}\nLocation: {before.channel.mention}",
                              timestamp=datetime.now(), color=discord.Colour.blue())
        await z.send(embed=embed)

@bot.event
async def on_member_update(before, after):
        z = bot.get_channel(984047964110610473)
        if len(before.roles) > len(after.roles):
            role = next(role for role in before.roles if role not in after.roles)
            embed = discord.Embed(title=f"{before}'s Role has Been Removed",
                                  description=f"{role.name} was removed from {before.mention}.",
                                  timestamp=datetime.now(), color=discord.Colour.red())
        elif len(after.roles) > len(before.roles):
            role = next(role for role in after.roles if role not in before.roles)
            embed = discord.Embed(title=f"{before} Has been given a new role",
                                  description=f"{role.name} was given to {before.mention}.", timestamp=datetime.now(),
                                  color=discord.Colour.green())
        elif before.nick != after.nick:
            embed = discord.Embed(title=f"{before}'s Nickname Changed",
                                  description=f"Before: {before.nick}\nAfter: {after.nick}", timestamp=datetime.now(),
                                  color=discord.Colour.blue())
        else:
            return
        await z.send(embed=embed)

@bot.event
async def on_guild_channel_create(channel):
        z = bot.get_channel(984047964110610473)
        embed = discord.Embed(title=f"{channel.name} was Created", description=channel.mention,
                              timestamp=datetime.now(), color=discord.Colour.green())
        await z.send(embed=embed)

@bot.event
async def on_guild_channel_delete(channel):
        z = bot.get_channel(984047964110610473)
        embed = discord.Embed(title=f"{channel.name} was Deleted", timestamp=datetime.now(), color=discord.Colour.red())
        await z.send(embed=embed)    

@bot.command() # register bot commands using this decorator
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed=discord.Embed(title=f"**Success**",description=f"Banned {member.name}#{member.discriminator}",color=0xffa980)
        await ctx.send(embed=embed)
@ban.error
async def ban_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"Please use **?ban (Member) (Reason)**",color=0xff6161)
            await ctx.send(embed=embed, delete_after=5)

@bot.command() # register bot commands using this decorator
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
        embed1=discord.Embed(title=f"**Success**",description=f"{member.mention} has been muted in {ctx.guild}\nReason: {reason}",color=0xffa980)        
        embed2=discord.Embed(title=f"**Muted**",description=f"You have been muted in {ctx.guild}\nReason: {reason}",color=0xffa980)        
        embed4=discord.Embed(title=f"**No Mute Role**",description=f"No Mute Role found! Creating one now...",color=0xffa980)             
        guild = ctx.guild
        muteRole = discord.utils.get(guild.roles, name = "Muted")
 
        if not muteRole:
            await ctx.send(embed=embed4)
            muteRole = await guild.create_role(name = "Muted")
 
        for channel in guild.channels:
            await channel.set_permissions(muteRole, speak=False, send_messages=False, read_messages=True, read_message_history=False, view_channel=False)
        await member.add_roles(muteRole, reason=reason)
        await ctx.send(embed=embed1)
        await member.send(embed=embed2)
        return      

@mute.error
async def mute_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"Please use **?mute (Member) (Reason)**",color=0xff6161)
            await ctx.send(embed=embed)        
        elif isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title=f"**Insufficient Permissions**",description=f"You do not have **required** permissions",color=0xff6161) 

@bot.command(case_insensitive=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
        embed1=discord.Embed(title=f"**Success**",description=f"{member.mention} has been unmuted in {ctx.guild}",color=0xffa980)        
        embed2=discord.Embed(title=f"**Success**",description=f"You have been unmuted in {ctx.guild}",color=0xffa980)
        guild = ctx.guild
        muteRole = discord.utils.get(guild.roles, name = "Muted")
 
        if not muteRole:
            await ctx.send("The Mute role can\'t be found! Please check if there is a mute role or if the user already has it!")
            return
        await member.remove_roles(muteRole, reason=reason)
        await ctx.send(embed=embed1)
        await member.send(embed=embed2)            

@bot.command() # register bot commands using this decorator
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f"**Success**",description=f"Kicked {member.name}#{member.discriminator}",color=0xffa980)
        await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"Please use **?kick (Member) (Reason)**",color=0xff6161)
            await ctx.send(embed=embed, delete_after=5)

@bot.command() # register bot commands using this decorator
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int=5):
        await ctx.channel.purge(limit=amount+1)
        embed1=discord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 5 seconds",color=0xffa980)
        embed2=discord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 4 seconds",color=0xffa980)
        embed3=discord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 3 seconds",color=0xffa980)
        embed4=discord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 2 seconds",color=0xffa980)
        embed5=discord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 1 second",color=0xffa980)
        
        message = await ctx.send(embed=embed1, delete_after=6)
        await asyncio.sleep(1)
        await message.edit(embed=embed2)
        await asyncio.sleep(1)
        await message.edit(embed=embed3)
        await asyncio.sleep(1)
        await message.edit(embed=embed4)
        await asyncio.sleep(1)
        await message.edit(embed=embed5)
        await asyncio.sleep(1)

@purge.error
async def purge_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"Please use **?purge (Amount)**",color=0xff6161)
            await ctx.send(embed=embed, delete_after=5)
        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed(title="Invalid Command Usage", description="This command does not support non-number values as purge amounts", color=0xff6161)
            await ctx.send(embed=embed, delete_after=5)     

@bot.command() # register bot commands using this decorator
@commands.has_permissions(administrator=True, manage_roles=True)
async def reactrole(ctx, emoji, role: discord.Role, *, message):

        emb = discord.Embed(description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emoji)
        with open('reactrole.json') as json_file:
            data = json.load(json_file)
            new_react_role = {'role_name': role.name,
                              'role_id': role.id,
                              'emoji': emoji,
                              'message_id': msg.id}
            data.append(new_react_role)
        with open('reactrole.json', 'w') as f:
            json.dump(data, f, indent=4)

@reactrole.error
async def reactrole_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f"**Invalid Command Usage**",description=f"Please use **?reactrole (Emoji) (Role) (Message)**",color=0xff6161)
            await ctx.send(embed=embed, delete_after=15)
@bot.event
async def on_raw_reaction_add(payload):

        if payload.member.bot:
            pass

        else:
            with open('reactrole.json') as react_file:
                data = json.load(react_file)
                for x in data:
                    if x[
                        'message_id'] == payload.message_id:  # checks if the found member id is equal to the id from the
                        # message where a reaction was added
                        if x['emoji'] == payload.emoji.name:  # checks if the found emoji is equal to the reacted emoji
                            role = discord.utils.get(bot.get_guild(
                                payload.guild_id).roles, id=x['role_id'])
                        await payload.member.add_roles(role)
@bot.event
async def on_raw_reaction_remove(payload):

        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:

                if x['message_id'] == payload.message_id:  # checks if the found member id is equal to the id from the
                    # message where a reaction was added
                    if x['emoji'] == payload.emoji.name:  # checks if the found emoji is equal to the reacted emoji
                        role = discord.utils.get(bot.get_guild(
                            payload.guild_id).roles, id=x['role_id'])

                    await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)   

@tasks.loop(seconds=5)
async def change_status():
        await bot.change_presence(activity=discord.Game(next(status)))                   

bot.run('YOUR BOT TOKEN')