import discord
import os 


client = discord.Client()   # Instanciando a conexão com o discord 

@client.event  # Decorador para "escutar" eventos do servidor 
async def on_ready():  # Método que responde o evento. "Callback" 
    print('Nos estamos logados com {0.user}!'.format(client))  # 0 é uma máscara para client. 
    
@client.event 
async def on_message(message):  # Responde ao evendo "mensagem" 
    if message.author == client.user:  # Se o autor da mensagem for o bot, não faz nada
        return

    if message.content.startswith('*salve'):
        await message.channel.send('SALVE!') 

    # Tô na dúvida desse await, mas se eu não me engano ele espera isso terminar pra poder 
    # # Executar as outras coisas 

client.run(os.getenv('TOKEN'))  # Token do BOT no portal do desenvolvedor Discord 
# Se for usar o repl.it, lembre-se que tudo é público por lá, menos o arquivo .env

# O nome dos métodos são pré-setados. Se mudarmos o nome deles, não funcionam.
