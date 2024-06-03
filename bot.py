import discord
import botKey
import time
import math

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('?sa'):
        await message.channel.send(f"As {message.author}!")

    if message.content.startswith("?clock"):
        await message.channel.send(f"{time.localtime()}")

    if message.content.startswith('?bb'):
        await message.channel.send(f"Görüşürüz {message.author}!")

    if message.content.startswith('?piSayısı'):
        await message.channel.send(f"{math.pi}")

client.run(botKey.TOKEN)