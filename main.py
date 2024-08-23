import discord
from discord.ext import commands
from model import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            name = i.filename
            url = i.url
            await i.save( f"./img/{name}" )
    else:
        await ctx.send("Olvidaste adjuntar una imagen :face_with_raised_eyebrow:")

bot.run("TOKEN")