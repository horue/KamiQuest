import discord
from discord.ext import commands
import os
import requests
import json
import random
from dc_token import *



intents = discord.Intents.default()
intents.message_content = True
bot = client = commands.Bot(command_prefix = "k!", case_insensitive = True, activity=discord.Game(name="k!a para ajuda."), status=discord.Status.online, intents=intents)
versao = ('0.0.2')


@bot.command()
async def test(ctx):
    await ctx.send('Este é um comando de teste.')








client.run(key)