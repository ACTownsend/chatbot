#BEGINNING OF DRAGOS CODE
import discord
import random
import requests
import json
from features import *
from discord.ext import commands

'''https://www.devdungeon.com/content/make-discord-bot-python, documentation about how to make the chat bot'''

TOKEN = 'NTEwNTU1NTc3ODE1MDA3MjMz.DseD7Q.Q7sdQq4g_BWNxp1qpWNphOrgHOs'
client = commands.Bot(command_prefix = ".")#establishing the Discord client that is connecting do discord
greating =['hello', 'bonjour', 'hey', 'hi', 'sup', 'morning', 'hola', 'ohai', 'yo']
goodbyes =['bye','see you','See ya','see you soon','Take it easy','take care','take care of yourself','hope to see you soon']
prefix = "/"
@client.event
async def on_message(message):
    if message.author == client.user:   # this is for the bot not to reply to itself
        return
    if message.content.lower() in greating:
        msg = random.choice(greating)+" "+'{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.lower() in goodbyes:
        msg = random.choice(goodbyes)+" "+'{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.lower()=="what's up?":
        msg = 'Nothing, just learning about humans...'
        await client.send_message(message.channel, msg)
    args = message.content.split(" ")[1:]
    if message.content.startswith(prefix + "say"):  #making the bot say what you want
        await client.send_message(message.channel, "No I will not say th...")
        await client.delete_message(message)
        await client.send_message(message.channel, " ".join(args))
    if message.content.startswith(prefix+'shutdown'):   #loging out the chatbot
        await client.send_message(message.channel, 'Shutting down. Bye!')
        await client.logout()
        await client.close()
    if message.content.startswith(prefix+'catgif'): #random cat gif
        await client.send_message(message.channel, "Cutenes incoming, or weirdness...")
        await client.send_message(message.channel, cats.getCatGif())
        #http://api.icndb.com/jokes/random? - getting the bad jokes from here json style
    if message.content.startswith(prefix+'joke'):
        await client.send_message(message.channel, "I'm not that good at jokes obvious but ...")
        chuck = requests.get('http://api.icndb.com/jokes/random?')
        if chuck.status_code == 200:
            chuck = chuck.json()['value']['joke']
            await client.send_message(message.channel, chuck)
    if message.content.startswith(prefix+'bitcoin'):
        await client.send_message(message.channel, "Really do you want to invest in that...")
        await client.send_message(message.channel, bitcoin.coin())
    #if message.content.startswith(prefix+'movie'): #trying to give to similar movies
    #    temp = message.split("movie", 1)[1]
    #    await client.send_message(message.channel, movies.movie(temp))
    if message.content.startswith(prefix+'coinflip'):   #50/50 chance
        random_number = random.randint(1, 100)
        if random_number >= 50:
            text = 'It comes up tails'
        else:
            text = 'It comes up heads'
        header = 'Bot has flipped a coin...'
        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await client.send_message(message.channel, embed=embed)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
client.run(TOKEN)
#END OF DRAGOS MAIN CODE
