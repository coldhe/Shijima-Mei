import discord
from discord.ext import commands
import asyncio
import random
import datetime
import embedlinks
import conv
import aidairo

def read_token():
    with open("token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = commands.Bot(command_prefix='m!')


@client.command()
async def hello(ctx):
        await ctx.send(f"Hello~ {ctx.author.name}.")

@client.command()
async def colorpage(ctx):
    chosen_image = random.choice(embedlinks.images)

    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by : {ctx.author.name}")

    await ctx.send(embed=embed)

@client.command()
async def aidairo(ctx):
    chosen_image = random.choice(embedlinks.illust)

    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by : {ctx.author.name}")

    await ctx.send(embed=embed)

@client.command()
async def old(ctx):
    chosen_image = random.choice(embedlinks.old)

    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by : {ctx.author.name}")

    await ctx.send(embed=embed)

@client.command()
async def kitsune(ctx):
    chosen_image = random.choice(embedlinks.kitsune)

    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by : {ctx.author.name}")

    await ctx.send(embed=embed)

@client.command()
async def dmld(ctx):
    chosen_image = random.choice(embedlinks.dmld)

    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by : {ctx.author.name}")

    await ctx.send(embed=embed)
   
@client.command()
async def meichan(ctx):
        await ctx.send(random.choice(conv.reponses))









client.run(token)
