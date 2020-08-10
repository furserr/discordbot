import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

gelen_veri = soup.find_all("div", {"class":"market-data"})
doviztablosu = gelen_veri[0].find_all("div",{"class":"item"})
dolardeger = doviztablosu[1].find("span",{"class":"value"})
eurodeger = doviztablosu[2].find("span",{"class":"value"})
dolardegeri = dolardeger.text
eurodegeri = eurodeger.text

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
    await ctx.send("1$ = "+ dolardegeri + " TL")

@bot.command(pass_context=True)
async def euro(ctx):
    await ctx.send("1€ = "+ eurodegeri + " TL")

bot.run("NzQyMDY0NTU0MjcxMzA5OTk2.XzAreA.zhyZ0ZiKtt7Q-2SrKIYktiYPSU4")
