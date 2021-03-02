from discord.ext import commands
import os 
from random import choice
import requests
from bs4 import BeautifulSoup

# Bot construído com a subclasse 'bot' do discord.Client
# Tudo que pode-se fazer com discord.Client, também é possível com bot.
# https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client
# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#commands

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print(f'{bot.user.name} está ON!')

# funções que não são do bot, mas usadas por ele. Algo como funções privadas
def frases():
    response = requests.get('https://www.pensador.com/frases_de_otimismo/')
    soup = BeautifulSoup(response.text, 'html.parser')  # Estava escrito hmtl, cuidado!
    frases = []

    busca = soup.find_all('p', class_='frase fr')

    for i in busca:
        frases.append(i.text)

    frase = choice(frases)
    
    return frase
# -------------------------------------------------------------------------------------------- #

# Comando que dá um salve na rapaziada
@bot.command(name='salve')
async def salve(ctx):  # ctx é o contexto do bot, que dá informações do servidor e tal
    await ctx.send('SALVE!')

# Comando que mede o ping (não sei se é o ping com a API)
@ bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'**Pong!** Meu ping com o server é de `{bot.latency:.2f}ms`')
    # Aceita Markdown

# Comando que mostra uma frase foda KKKKKKKKKKK
@bot.command(name='frase')
async def frasefoda(ctx):
    frase = frases()
    await ctx.send(f'_{frase}_')


bot.run(os.getenv('DISCORD_TOKEN'))
