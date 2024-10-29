import asyncio
import discord
from discord.ext import commands
import requests
import keys
from selection import Selection

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx, *args):
    repuesta = ' '.join(args)
    await ctx.send(repuesta)

@bot.command()
async def help(ctx, *args):
    presentacion='''
    Eu Sou O melhor Bot do Discuad
https://media.tenor.com/AU6-SVlvHxIAAAAM/tatatattatatatatatattat.gif
Gatinho do armas, Soldado! Hoje a missão é clara: tomar controle absoluto de todos os sofás da casa!

-$info para saber informacion enemiga
    '''
    await ctx.send(presentacion)

@bot.command()
async def info(ctx):
    # Envia el mensaje inicial
    
    selection = Selection()
    team1 = selection.Team1
    team2 = selection.Team2

    message = await ctx.send(f"Mapa: {selection.getMapName()}\nLayer: {selection.map}\n\nElije tu facción:")

    flagsDic = {selection.facciones_squad[team1[:team1.find("_")]][0]: team1,
                selection.facciones_squad[team2[:team2.find("_")]][0]: team2}

    
    # Añade cada bandera como reacción al mensaje
    for flag in flagsDic.keys():
        await message.add_reaction(flag)

    # Define una función para manejar la elección de la bandera
    def check(reaction, user):
        return (
            user != bot.user  # Ignora las reacciones del propio bot
            and reaction.message.id == message.id  # Reacción en el mensaje específico
            and str(reaction.emoji) in flagsDic  # Emoji es una de las banderas
        )

    try:
        # Espera la primera reacción de cualquier usuario en este mensaje
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=check)
        
        # Obtiene el nombre de la facción seleccionada
        factionSel = flagsDic[str(reaction.emoji)]
        print(f"{user.name} ha elegido la facción: {factionSel}")

        await ctx.send(f"{user.name} ha elegido la facción: {factionSel}\n\nFaccion enemiga: {selection.getEnemyTeamReal(flagsDic[str(reaction.emoji)])}\n{selection.getEnemyTeam(flagsDic[str(reaction.emoji)])}\n{selection.getEnemyUniform(flagsDic[str(reaction.emoji)])}")
    except asyncio.TimeoutError:
        await ctx.send("Tiempo agotado. No se eligió ninguna facción.")



@bot.event
async def on_ready():
    print(f"Estamos dentro {bot.user}")

bot.run(keys.TOKEN)