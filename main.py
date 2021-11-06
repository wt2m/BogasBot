from asyncio.windows_events import NULL
import discord
from discord.ext import commands
import json
import dotenv
import os

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
        await message.reply("https://tenor.com/view/femboy-skirt-maid-outift-maid-outfit-gif-21382375")
        
    if message.author.id == 359163391375441920:
        await message.reply("Vai se fude gamer fedorento")
        await message.reply("https://tenor.com/view/aaaaa-aaaaaaa-shout-yell-rat-gif-14860400")  '''
    if "teste" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, quica na minha pica! {message}"
        )
        await message.delete()
    await bot.process_commands(message)

@bot.command(name="msg")
async def send_msg(ctx):
    name = ctx.author.name

    response = "asdfojsadf " + name

    await ctx.send(response)

@bot.command(name="gifs")
async def send_gifs(ctx):
    gifs = [
        'https://tenor.com/view/lithiumare-kiracord-nerd-marbellu-gif-22666819',
        'https://media.discordapp.net/attachments/786466436448780308/832346839365713981/a_e33526630f9c39bb2a1203bf01fe564a.gif',
        'https://tenor.com/view/baguncinha-we-do-a-little-guei-gif-21158523',
        'https://tenor.com/view/cum-the-cum-here-comes-the-cum-gif-18740280',
        'https://tenor.com/view/kioo-gif-19634683',
        'https://tenor.com/view/the-j-spongebob-gif-21742603',
        'https://tenor.com/view/femboy-dance-dance-gif-cute-meme-gif-20533959',
        'https://tenor.com/view/poop-massive-sump-naked-animation-ew-gif-17920176',
        'https://tenor.com/view/squid-game-gi-hun-gi-hun-squid-game-seong-gi-hun-seung-gi-hun-gif-23386383',
        'https://tenor.com/view/kitten-spoon-milk-drinking-milk-drinking-gif-19025805',
        'https://media.discordapp.net/attachments/427586051079536640/893778269940350996/image0-18.gif',
        'https://tenor.com/view/mustache-guy-crazy-mostacho-guy-with-crazy-mustache-gif-22094888',
        'https://tenor.com/view/eq4a-humor-gif-22020263',
        'https://tenor.com/view/momasoz-diego-2blocked-2blocked-messages-kaan%C3%B6zgal-%C3%B6mer-kaan%C3%B6zgal-gif-21824400',
        'https://tenor.com/view/giant-cockroach-escaping-speedrun-bedrun-cockroach-ucd-gif-21935230',
        'https://tenor.com/view/femboy-skirt-maid-outift-maid-outfit-gif-21382375',
        'https://tenor.com/view/saudades-meu-amor-heart-love-couple-in-love-gif-16336939',
        'https://tenor.com/view/aaaaa-aaaaaaa-shout-yell-rat-gif-14860400',
    ]
    for gif in gifs:
        await ctx.send(gif)

with open('utils\inconvenientes.json') as f:
    inconvenientes = json.load(f)
    print(inconvenientes)

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