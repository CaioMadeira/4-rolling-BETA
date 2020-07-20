import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
from googlesearch import search

client = commands.Bot(command_prefix="!", case_insensitive=True)
status = cycle(["Earthbound", "Stardew Valley", "D&D", "Final Fantasy", "Undertale", "Warcraft"])

@client.event
async def on_ready():
    change_status.start()
    print(f"{client.user.name} está pronto pra jogar!")
    print("-----------------")

@tasks.loop(seconds=30)
async  def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#---------------------------RPG ------------------------------------

#DADO DE 6 LADOS

@client.command()
async def d6(ctx, *, numero=None):

    numero=eval(numero)

    for _ in range(numero):
        dadoslado = (random.randint(1, 6))
        await ctx.send(f"D6: {dadoslado}")


    await ctx.send("-------------------------------------------------------")



#DADO DE 20 LADOS
@client.command()
async def d20(ctx, *, numero=None):

    numero=eval(numero)


    for _ in range(numero):
        dadoslado = (random.randint(1, 20))
        dadoslado = dadoslado
        await ctx.send(f"D20: {dadoslado}")

    await ctx.send("-------------------------------------------------------")


#::::::::::::::::DADO DE 10 LADOS
@client.command()
async def d10(ctx, *, numero=None):

    numero=eval(numero)


    for _ in range(numero):
        dadoslado = (random.randint(1, 10))
        dadoslado = dadoslado
        await ctx.send(f"D10: {dadoslado}")

    await ctx.send("-------------------------------------------------------")


#:::::::::::::::::;;DADO DE 12 LADOS
@client.command()
async def d12(ctx, *, numero=None):

    numero=eval(numero)


    for _ in range(numero):
        dadoslado = (random.randint(1, 12))
        dadoslado = dadoslado
        await ctx.send(f"D12: {dadoslado}")



    await ctx.send("-------------------------------------------------------")

#:::::::::::::::::;;DADO DE 8 LADOS
@client.command()
async def d8(ctx, *, numero=None):

    numero=eval(numero)


    for _ in range(numero):
        dadoslado = (random.randint(1, 8))
        dadoslado = dadoslado
        await ctx.send(f"D8: {dadoslado}")



    await ctx.send("-------------------------------------------------------")


#::::::::::::BUSCADOR::::::::::::
@client.command()
async def pesquisar(ctx, *, pesquisa=None):

    pesquisa = str(pesquisa)

    for resultado in search(f'"{pesquisa}"google imagens', stop=1):
        await ctx.send(resultado)





client.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
