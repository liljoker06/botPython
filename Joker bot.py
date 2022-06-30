import asyncio
from http import client
from sqlite3 import Timestamp
from turtle import color, title
import discord 
import random
from discord.ext import commands
import json 
import time 

bot = commands.Bot(command_prefix = ".")

#evenement le bot est en marche message dans le terminal 
@bot.event
async def on_ready() :
    print("I am ready bro !")

#evenement un nouvau memebre qui rejoins 
@bot.event
async def on_member_join(member) :
    print(f'{member} welcome in server')

#evennement quand un membre quitte le serv 
@bot.event
async def on_member_remove(member) :
    print (f'{member} Good bye !')

#commande qui donne le ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round (bot.latency * 1000)}ms')


# mini jeu qui utilise la bibliotheques  
@bot.command(aliases =['8ball','test']) 
async def _8ball(ctx, *, question):
    responses = ['Il est certain.',
                    'C est décidément ainsi.',
                    'Sans aucun doute.',
                    'Oui definitivement.',
                    'Vous pouvez compter dessus.',
                    'Comme je le vois, oui.',
                    'Probablement.',
                    'Les perspectives sont bonnes.',
                    'Oui.',
                    'Les signes pointent vers oui.',
                    'Réponse brumeuse réessayer.',
                    'Demmander à nouveau plus tard.,'
                    'Mieux vaut ne pas te dire maintenant.',
                    'Ne peut pas prédire maintenant.',
                    'Ne compte pas dessus.',
                    'Ma réponse est non.',
                    'Ma source dit non.',
                    'Les perspectives ne sont pas si bonnes.',
                    'Très douteux.']
    await ctx.send(f'Questions: {question}\n reponse: {random.choice(responses)}')                    

#commande pour supprimer les messages 
@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#commande pour expulser un membre 
@bot.command()
async def kick(ctx,member : discord.Member,*, reason = None):
    await member.kick(reason=reason)

#commande pour bannir un membre 
@bot.command()
async def ban(ctx,member : discord.Member,*, reason = None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member. mention}')

#commande unban mais a revoir quelques problemes 
@bot.command()
async def unban(ctx, *, member):
    banned_users =  await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.id}')


#commande mute 
@bot.command(pass_context = True)
async def mute(ctx, member : discord.Member) :
    if ctx.message.Server_permissions.administrator :
        role = discord.utils.get(member.server.roles, name = 'Muted')
        await ctx.add_roles(member, role)
        embed = discord.Embed(title = "membre il est mute ")
        await ctx.send(embed = embed)
    else :
        embed = discord.embed(title = "erreur de permission", description = " vous n'avez pas de permission !", color = 0xff00f6)
        


#commande pour afficher les information du serveur
@client.command()
async def serverinfo(ctx) :
    role_count = len(ctx.guild.role)
    liste_de_bot = [bot.mention for boy in ctx.guild.members if bot.bot]

    serverinfoEmbed = discord.Embed(Timestamp = ctx.message.created_at, color = ctx.author.color)
    serverinfoEmbed.add_field(name= 'Nom du Serveur', value=f"{ctx.guildname}", inline= False)
    serverinfoEmbed.add_field(name= 'Nombre de membre', value=ctx.guild.member_count, inline= False)
    


bot.run("add you token bot ")