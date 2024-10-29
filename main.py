import asyncio
import random
import discord
from discord.ext import commands
import requests
import keys
from selection import Selection

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx, args):
    repuesta = ' '.join(args)
    await ctx.send(repuesta)

@bot.command()
async def helpmiau(ctx):

    presImg = [
                "https://media.tenor.com/AU6-SVlvHxIAAAAM/tatatattatatatatatattat.gif",
                "https://media1.tenor.com/m/50egAhARCjEAAAAC/cat-shooting.gif",
                "https://i.imgur.com/wDz0gK2.gif",
                "https://media.tenor.com/xCzc4aOrDy0AAAAM/machine-gun-cat.gif",
                "https://cdn.discordapp.com/attachments/1300248545542275102/1300883757292584972/DALLE_2024-10-29_19.07.22_-_A_cute_cartoon_military_cat_in_a_camouflage_uniform_with_a_tiny_gun_crouched_in_an_action_pose_and_looking_determined._Above_the_cat_bold_stylized_.webp?ex=672275e8&is=67212468&hm=08ac926b0e0baf3422cc1e5d26eca5bb42820caec81f25f012aea45c75df3114&"
                ]    
    
    presPhrases = [
                            "Soldado! Hoje a missão é clara: tomar controle absoluto de todos os sofás da casa!",
                            "Alerta máximo: avistado movimento suspeito na cozinha. Operação ‘Pega Frango’ iniciada!",
                            "Recrutas, hora de patrulhar a área... mas primeiro, soneca estratégica de 8 horas!",
                            "Ordem do dia: conquistar o território da cama. Humanos, mantenham distância!",
                            "Missão de hoje: sabotagem da cortina. Código de ataque: unhas afiadas!",
                            "Alvo avistado: passarinho na janela. Silêncio, equipe, estamos em modo furtivo!",
                            "Capitão Miaus ao comando! Tropas, preparar ataque de fofura máxima!",
                            "Atenção! Não se aproxima da ração sem autorização. Estou de guarda!",
                            "Treinamento intensivo de habilidades: três saltos no sofá e duas mordidas no humano!",
                            "Missão de reconhecimento concluída: humanos em território seguro. Hora do cochilo!"
                            ]
    try:
        presentacion=f'''
        Eu Sou O melhor Bot do Discuad
    Gatinho do armas, {random.choice(presPhrases)}

        
        ***-$info*** para saber informacion enemiga
        ***-$info*** server ("sph" o "lex" por defecto sph) para cambiar de servidor

            {random.choice(presImg)}
        '''
        await ctx.send(presentacion)
    except Exception as e:
            await ctx.send("Ha ocurrido un error inesperado al ejecutar el comando.")
            print(f"Error en el comando: {e}")
@bot.command()
async def info(ctx, arg: str = ""):
    try:
        
        selection = Selection(arg)
        team1 = selection.Team1
        team2 = selection.Team2

        message = await ctx.send(f"Mapa: {selection.getMapName()}\nLayer: {selection.map}\n\nElije tu facción:")

        flagsDic = {selection.facciones_squad[team1[:team1.find("_")]][0]: team1,
                    selection.facciones_squad[team2[:team2.find("_")]][0]: team2}
    except Exception as e:
        await ctx.send("Ha ocurrido un error inesperado al ejecutar el comando.")
        print(f"Error en el comando: {e}")
    
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