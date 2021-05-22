import os
import discord

my_secret = os.environ['TOKEN']

##instance of client - connection to discord 
client = discord.Client() 

## using client.event to register an event
@client.event 
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(my_secret)



