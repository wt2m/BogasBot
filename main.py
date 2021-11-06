from asyncio.windows_events import NULL
import discord
from discord.ext import commands
import json
import dotenv
import os
import random

dotenv.load_dotenv(dotenv.find_dotenv());

bot = commands.Bot("bg!")

@bot.event
async def on_ready():
    print("Bot iniciado!!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    '''if message.author.id == 204350761616932865:
        await message.reply("https://tenor.com/view/femboy-skirt-maid-outift-maid-outfit-gif-21382375")'''
        
    if message.author.id == 359163391375441920:
        r = random.randint(0,50)
        if r == 21:
            await message.reply("Vai se fude gamer fedorento")
        if r == 40:
            await message.reply("https://tenor.com/view/aaaaa-aaaaaaa-shout-yell-rat-gif-14860400")
    if "Hiro" in message.content:
        await message.reply(
            f"Por favor, {message.author.name}, quica na minha pica e nunca mais cite esse random odiador de pobres!"
        )
    r = random.randint(0,400)
    if r == 321:
        await message.channel.send(
            "aaaaaaaaaaaaaaaa cala a bocaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        )
    await bot.process_commands(message)

@bot.command(name="msg")
async def send_msg(ctx):
    name = ctx.author.name

    response = "asdfojsadf " + name

    await ctx.send(response)

@bot.command(name="gifs")
async def send_gifs(ctx):
    fileObj = open('utils\gifs.txt', "r") #opens the file in read mode
    gifs = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    
    for gif in gifs:
        await ctx.send(gif)

@bot.command(name="addgif")
async def add_gif(ctx, *, arg):
    fileObj = open("utils\gifs.txt")
    old = fileObj.read();
    print(old);
    fileObj = open("utils\gifs.txt", "w")
    fileObj.write(old)
    fileObj.write(f"{arg}\n")
    fileObj.close()
    await ctx.message.reply('Armazenado meu truta')

with open('utils\inconvenientes.json') as f:
    inconvenientes = json.load(f)

@bot.command(name="inconveniente")
async def inconveniente(ctx, *, arg):
    if arg != NULL:
        arg = arg.lower()
        aux = False
        auxQnt = NULL  
        for inconveniente in inconvenientes:
            inc = json.loads(inconveniente)
            if inc['nome'] == arg:
                inc['qnt'] += 1
                auxQnt = inc['qnt']
                inconvenientes.remove(inconveniente)
                inconvenientes.append(json.dumps(inc))
                aux = True
        if aux:
            await ctx.send(f"**{arg}** foi inconveniente **{auxQnt}** vezes hoje. Alguém para esse retardado.")
        else:
            jsonInc = {
                "nome": arg,
                "qnt": 1
            }
            inconvenientes.append(json.dumps(jsonInc))
            await ctx.send('Inconveniente adicionado a lista de inconvenientes :))')

        jsonString = json.dumps(inconvenientes)
        jsonFile = open("utils\inconvenientes.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        
    else:
        await ctx.send('Insira um nome de algum macaco pora! (bg!inconveniente <nome>)')

@bot.command(name="inconvenientes")
async def inconvenientes_list(ctx):
    embed=discord.Embed(
    title="Lista de inconvenientes xD",
        #url="https://realdrewdata.medium.com/",
        description="Só os mais macacos do xet",
        color=discord.Color.blue())
    embed.set_thumbnail(url="https://m.media-amazon.com/images/I/61rPwT+t2PL._SS500_.jpg")
    for inconveniente in inconvenientes:
        inc = json.loads(inconveniente)
        nome = inc['nome']
        qnt = inc['qnt']
        embed.add_field(name=f"**{nome}**", value=f"O sequelado já retardou {qnt} vezes", inline=True)
    await ctx.send(embed=embed)
bot.run(os.getenv('DISCORD_BOT_TOKEN'))