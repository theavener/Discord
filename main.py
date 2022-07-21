import discord
import requests
import json
import random


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

client.run('OTk5NTA4MTYzMjIzMTA5Njky.GiuyM6.kIz2XxY5_f1b-37OOCaKzjZ1z5OwJvPdiP7WsE')

