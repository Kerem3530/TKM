import discord
from discord.ext import commands
import time
import random

özlüSözlerList = ["Özlü Sözler Özlü Sözlerdir", "Bir Gün Herkes Belediye Çukuru Olacak"
                  , "Herkes Kötü Bir İnsan Olabir ama Önemli Olan Cuguli Olmaktır",
                  "Dolar Hep Yükselecektir ama Asıl Önemli Olan ₺'nin İçinden Geçmektir",
                  "En İyi Program code-insiders'tır", "Error: Beyin doesn't exist (404)"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='--', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def bilgi(ctx):
    await ctx.send(f'{bot.user} SmurfCatKerem [keremu960] tarafından bir discord botu')

@bot.command()
async def saatKaç(ctx):
    zaman = time.localtime()
    await ctx.send(f"{zaman}")

@bot.command()
async def özlüSözler(ctx):
    özlüSöz = random.choice(özlüSözlerList)
    await ctx.send(f"Sana Bir Özlü Söz!: {özlüSöz}")

bot.run("TOKENİNİ BURAYA YAZ KOMUTLAR ŞU ŞEKİL ÇALIŞIR: --bilgi")
