import discord

import asyncio

import random

from discord.ext import commands, tasks

from discord.utils import get

token = "NzQwNzg2NDQxMjI3MDc1Njc2.XyuFIg.0VwQdSdQttLhYXZ3GitqJHkhH6I"

client = commands.Bot(command_prefix = "m!")

praypuns = [
'Remember to pray!',
'Pray, boys!',
'Ding dong guys, pray!',
'For the love of my horrible animations, pray!',
'I am the one that stands at the pinnacle of all races, prayscanor',
'Pray lol',
"Roses are red, I have an itch, Merlin's thighs are https://cdn.discordapp.com/attachments/656490287090237450/740113811574489158/tenor-117.gif",
]


async def runpend():
    while True:
        channel = client.get_channel(656490287090237450)
        await channel.send(f"<@&655892806035963951>, {random.choice(praypuns)}")
        await asyncio.sleep(21600000)


@client.event
async def on_ready():
    print("Online!")
    print("Logged in as "+ str(client.user.name))
    print("ID: " + str(client.user.id))
    print('------')
    #client.change_presence(game=discord.Game("Use o!help"))

@client.command()
async def oof(ctx):
    await ctx.send("Yes, that's me")

@client.command()
async def oo(ctx):
    await ctx.send("Yes, that's me...2?")

@client.command()
async def pray(ctx):
    channel = client.get_channel(740792288858603633)
    await channel.send('Starting!')
    client.loop.create_task(runpend())

client.run(token)