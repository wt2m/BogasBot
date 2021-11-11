from asyncio.windows_events import NULL
from logging import NullHandler
import discord
from discord.ext import commands
import json
import dotenv
import os
from os import walk
import random
import requests
import shutil



dotenv.load_dotenv(dotenv.find_dotenv());

bot = commands.Bot("bg!")

@bot.event
async def on_ready():
    print("Bot iniciado!!")
    #RPC
    await bot.change_presence(activity=discord.Game(name="e cheirando pó"))




#Ao receber mensagens
@bot.event
async def on_message(message):

    # Evitar ler as próprias mensagens
    if message.author == bot.user:
        return
    
    lowerMessage = message.content.lower();

    # Roubar gifs enviados no xet
    try:
        extension = requests.head(message.content).headers['Content-Type'];
        if extension == "image/gif" or message.content.find("tenor.com/view") != -1:
            fileObj = open('data\gifs.txt', "r")
            gifs = fileObj.read().splitlines() #puts the file into an array
            fileObj.close()
            if message.content in gifs:
                NullHandler
            else:
                fileObj = open("data\gifs.txt")
                old = fileObj.read();
                fileObj = open("data\gifs.txt", "w")
                fileObj.write(old)
                fileObj.write(f"{message.content}\n")
                fileObj.close()   
                await message.reply('Your gif got **NHOINC**ed')

        
    except:
        NullHandler
                
    
    # Xingar o gamer a toa
    if message.author.id == 359163391375441920:
        r = random.randint(0,50)
        if r == 21:
            await message.reply("Vai se fude gamer fedorento")
        if r == 40:
            await message.reply("https://tenor.com/view/aaaaa-aaaaaaa-shout-yell-rat-gif-14860400")

    # Diminuir menções ao Hiro
    if "Hiro" in message.content:
        await message.reply(
            f"Por favor, {message.author.name}, quica na minha pica e nunca mais cite esse random odiador de pobres!"
        )
    # Caso me pinguem ou me chamem responder automático
    if message.author.id != 204350761616932865:
        mention = False
        try:
            mentions = message.mentions
            for m in mentions:
                if 204350761616932865 == m.id:
                    mention = True  
        except:
            NullHandler
        if "boga" in lowerMessage or "bogas" in lowerMessage or "mogas" in lowerMessage or "moguives" in lowerMessage or "boguives" in lowerMessage or "miguel" in lowerMessage or mention == True:
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
                'sz',
                'To seno tunelado relppppppp 2 gancho 2 minutooooooo',
                'Oi caralhooOoOoO aaaaaaaaaaaaaaa',
                'Fodase?',
                'Sim, eu como terra, como descobriu?',
                'dando a foda fora :wind_blowing_face: :wind_blowing_face: :wind_blowing_face: ',
                '†☺☼♀♂♠♣♥♦♪♫†☺☼♀♂♠♣♥♦♪♫†☺☼♀♂♠♣♥♦♪♫†☺☼♀♂♠♣♥♦♪♫†☺☼♀♂♠♣♥♦♪♫†☺☼♀♂♠♣♥♦♪♫†☺☼♀♂♠♣♥♦♪♫',
                'Não sei, pergunta pro <@442076414800298009>'
            ]
            r = random.randint(0, len(replies))
            await message.reply(f"{replies[r]}")
            
            #Counter
            aux = True
            with open('data\pings.json') as f:
                pings = json.load(f)
                
            for ping in pings:
                pingAUX = json.loads(ping)
            if pingAUX['nome'] == 'cobrafazmiau':
                pingAUX['qnt'] += 1
                pings.remove(ping)
                pings.append(json.dumps(pingAUX))
                aux = False
            
            if aux:
                jsonPing = {
                "nome": 'cobrafazmiau',
                "qnt": 1
                }
                pings.append(json.dumps(jsonPing))
                
            jsonString = json.dumps(pings)
            jsonFile = open("data\pings.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            
            #remove ping
            if mention:
                await message.delete()
            

        
    
    #Funções pra responder a pipas
    if message.author.id == 361675337811230725:
        if "vida" in lowerMessage:
            await message.reply("Oi vidaahahah te amo  :fallen_leaf: :fallen_leaf: ")
            await message.reply("https://tenor.com/view/saudades-meu-amor-heart-love-couple-in-love-gif-16336939")
        r = random.randint(0, 30)
        if r == 23:
            await message.reply("Oi bebê")
        if "bebe" in lowerMessage:
            await message.reply ("Oi :flushed:")
        if "casa" in lowerMessage or "casar" in lowerMessage:
            await message.reply ("Sim, eu quero casa co vc <@361675337811230725>")
    
    # Função meme pro bot mandar o povo calar a boca
    r = random.randint(0,400)
    if r == 321:
        await message.channel.send(
            "aaaaaaaaaaaaaaaa cala a bocaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        )
    await bot.process_commands(message)


# ------------------------ COMANDOS ---------------------------

@bot.command(name="msg")
async def send_msg(ctx):
    name = ctx.author.name

    response = "asdfojsadf " + name

    await ctx.send(response)

@bot.command(name="gifs")
async def send_gifs(ctx):
    fileObj = open('data\gifs.txt', "r") #opens the file in read mode
    gifs = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    
    for gif in gifs:
        await ctx.send(gif)

@bot.command(name="addgif")
async def add_gif(ctx, *, arg):
    fileObj = open("data\gifs.txt", "r")
    old = fileObj.read();
    fileObj.close()
    if arg in old:
        await ctx.message.reply("Esse gif já tá salvo burrão")
    else:
        fileObj = open("data\gifs.txt", "w")
        fileObj.write(old)
        fileObj.write(f"{arg}\n")
        fileObj.close()
        await ctx.message.reply('Armazenado meu truta')

@bot.command(name="gif")
async def send_gif(ctx):
    fileObj = open('data\gifs.txt', "r")
    gifs = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    lenGifs = len(gifs) - 1
    r = random.randint(0, lenGifs)
    await ctx.message.reply(gifs[r])


with open('data\inconvenientes.json') as f:
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
        jsonFile = open("data\inconvenientes.json", "w")
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

@bot.command(name="video", pass_context=True)
async def send_video(ctx):
    filenames = next(walk("videos"), (None, None, []))[2]
    split = ctx.message.content.split(" ")
    if len(split) == 1:
        text = ""
        for file in filenames:
            if text == "":
                text = f"{file}"
            else:
                text += f"\n{file}"
        embed=discord.Embed(
            #title="Lista de inconvenientes xD",
            #url="https://realdrewdata.medium.com/",
            description=f"{text}",
            color=discord.Color.blue())
        embed.set_footer(text="bg!video <video_name>")
        await ctx.message.reply(embed=embed)
    else:
        if len(split) == 2:
            if split[1] in filenames:
                await ctx.message.reply(file=discord.File(f'videos\{split[1]}'))
            else:
                await ctx.message.reply("Erro inesperado. Video não encontrado no sistema.")
        else:
            await ctx.message.reply("Erro inesperado. Mais de um parâmetro enviado.")

@bot.command(name="addvideo", pass_context=True)
async def save_video(ctx):
    filenames = next(walk("videos"), (None, None, []))[2]         
    if(len(ctx.message.attachments) > 0):
        if ctx.message.attachments[0].filename in filenames:
            await ctx.message.reply("Vídeo com mesmo nome já cadastrado!")
        else:        
            print(ctx.message.attachments[0].url)
            r = requests.get(ctx.message.attachments[0].url, stream=True)
            with open(f"videos\{ctx.message.attachments[0].filename}", 'wb') as out_file:
                print('Saving image: ' + ctx.message.attachments[0].filename)
                shutil.copyfileobj(r.raw, out_file) 
            await ctx.message.reply("Vídeo cadastrado!") 
            

@bot.command(name="git")
async def send_git(ctx):
    await ctx.send('https://github.com/wt2m/BogasBot')
    
@bot.command(name="spamPing")
async def spam_ping(ctx):
    mention = False
    try:
        mentions = ctx.message.mentions
        for m in mentions:
            mention = m 
    except:
        NullHandler
    if mention != False:
        if mention == 204350761616932865:
            for x in range(0, 50):
                await ctx.send(f'<@{ctx.message.author.id}>')
            await ctx.message.reply('Sério que tu tentou usar meu bot pra me pingar? Macaco d+')
        else:
            for x in range(0, 50):
                await ctx.send(f'oi {mention.mention}')
    else: 
        await ctx.message.reply('Pinga alguém burrão')
    

@bot.command(name="MCserver")
async def mc_server(ctx):
    response = requests.get("https://api.mcsrvstat.us/2/br7.purplehost.com.br:10359");
    serverInfo = response.json()
    players = f"Playerlist: "
    for player in serverInfo['players']['list']:
        players += f"\n{player}"
    '''icon = ":red_circle:"
    if serverInfo['online']:
        icon = ":green_circle:"'''
    embed=discord.Embed(
    title=  serverInfo['motd']['clean'][0] + " [" + str(serverInfo['players']['online']) +"/"+ str(serverInfo['players']['max']) + "]",
        description=players,
        color= discord.Color.green() if serverInfo['online'] else discord.Color.red())
    embed.set_footer(text="Online: " + str(serverInfo['online']))
    await ctx.send(embed=embed)
        
@bot.command(name="commands")
async def commands(ctx):
    await ctx.send('Tem os comando gif, gifs, addgif, inconveniente <nome>, inconvenientes, git e msg. Se vira pra descobrir oq cada uma faz ;D ')

bot.run(os.getenv('DISCORD_BOT_TOKEN'))

