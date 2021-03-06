import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import os

url = "https://www.doviz.com/"

bot = discord.Client()
bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print("dovizBot online..")
    print(dolardegeri)
    print(str(len(set(bot.get_all_members()))) + " tane kullanıcıya erişiliyor.")

@bot.command(pass_context=True)
async def dolar(ctx):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    gelen_veri = soup.find_all("div", {"class":"market-data"})
    doviztablosu = gelen_veri[0].find_all("div",{"class":"item"})
    dolardeger = doviztablosu[1].find("span",{"class":"value"})
    dolardegeri = dolardeger.text
    await ctx.send("1$ = "+ dolardegeri + " TL")

@bot.command(pass_context=True)
async def euro(ctx):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    gelen_veri = soup.find_all("div", {"class":"market-data"})
    doviztablosu = gelen_veri[0].find_all("div",{"class":"item"})
    eurodeger = doviztablosu[2].find("span",{"class":"value"})
    eurodegeri = eurodeger.text
    await ctx.send("1€ = "+ eurodegeri + " TL")

bot.run(os.environ.get('dovizbot'))
