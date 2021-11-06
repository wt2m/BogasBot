from asyncio.windows_events import NULL
from logging import NullHandler
import discord
from discord.ext import commands
import json
import dotenv
import os
import random
import requests

dotenv.load_dotenv(dotenv.find_dotenv());

bot = commands.Bot("bg!")

@bot.event
async def on_ready():
    print("Bot iniciado!!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    lowerMessage = message.content.lower();
    try:
        extension = requests.head(message.content).headers['Content-Type'];
        if extension == "image/gif":
            fileObj = open('utils\gifs.txt', "r")
            gifs = fileObj.read().splitlines() #puts the file into an array
            fileObj.close()
            
            if message.content in gifs:
                NullHandler
            else:
                fileObj = open("utils\gifs.txt")
                old = fileObj.read();
                print(old);
                fileObj = open("utils\gifs.txt", "w")
                fileObj.write(old)
                fileObj.write(f"{message.content}\n")
                fileObj.close()
                await message.reply('Your gif got **NHOINC**ed')

        
    except:
        NullHandler
                
        
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
    
    if "bogas" in lowerMessage or "mogas"  in lowerMessage or "moguives"  in lowerMessage or "boguives"  in lowerMessage or "miguel" or '204350761616932865' in message.mentions.members:
        replies = [
            'Oi, eu sou o atendente dele e vou responder por ele',
            'Bom dia, para de encher o saco',
            'Oi, ele tá ocupado gadando a pietra',
            'não, ele não vai ler sua mensagem',
            'Tá ocupado jogando dbd, pede pra namorada dele passar a informação',
            ':flushed:',
            'É pra chamar pra jogar dbd? Sim? Bora. É pra falar do servidor? Sim? Vai se foder.',
            'Se ele não tá na call ou ele tá trabaiando ou gadando, não enche',
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa para de me pingaaaaaaaaaa',
            '>:C',
            'Oi galera do frifaire, fale com o bot pessoal do boga',
            'Foda-se se o servidor caiu alalalalalala',
            'Meu zap é (37) 98835-2002 me chama lá que semana q vem eu te respondo',
            'sz'
        ]
        r = random.randint(0, len(replies))
        await message.reply(f"{replies[r]}")
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

@bot.command(name="gif")
async def send_gif(ctx):
    fileObj = open('utils\gifs.txt', "r")
    gifs = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    lenGifs = len(gifs) - 1
    r = random.randint(0, lenGifs)
    await ctx.message.reply(gifs[r])


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

@bot.command(name="git")
async def send_git(ctx):
    await ctx.send('https://github.com/wt2m/BogasBot')

bot.run(os.getenv('DISCORD_BOT_TOKEN'))

    