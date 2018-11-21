#BEGINNING OF DRAGOS CODE
import discord
from discord.ext import commands

TOKEN = 'NTEwNTU1NTc3ODE1MDA3MjMz.DseD7Q.Q7sdQq4g_BWNxp1qpWNphOrgHOs'
'''https://www.devdungeon.com/content/make-discord-bot-python, documentation about how to make the chat bot'''
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')

client.run(TOKEN)
#BEGINNING OF DRAGOS CODE
