import discord
from discord.ext import commands
import os
import requests
import json
import random
from dc_token import *
from samples import *


intents = discord.Intents.default()
intents.message_content = True
bot = client = commands.Bot(command_prefix = "k!", case_insensitive = True, activity=discord.Game(name="k!a para ajuda."), status=discord.Status.online, intents=intents)
versao = ('0.0.2')


@bot.command()
async def test(ctx):
    await ctx.send('Este é um comando de teste.')



@bot.command(aliases=['s'])
async def id(ctx):
  id = ctx.message.guild.id
  add_server(sn=id)
  await ctx.send(id)



client.run(key)