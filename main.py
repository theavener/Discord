import discord
import requests
import json
import random

from discord.ext import commands


GUILD = 999507725769773187
bot = commands.Bot(command_prefix='!')


client = discord.Client()
 

sad_words = ["sad", "rip", "madbcbad", "angry", "tilt", "titled"]

starter_encouragements = [
  "Get good!",
  "walking ward.",
  ":)"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name} hail to the bot'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice :int, number_of_sides :int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
    



client.run('OTk5NTA4MTYzMjIzMTA5Njky.GiuyM6.kIz2XxY5_f1b-37OOCaKzjZ1z5OwJvPdiP7WsE')

