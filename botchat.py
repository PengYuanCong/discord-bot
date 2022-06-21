from email import message
import discord
client = discord.Client()
@client.event

async def on_ready():
    print(f'目前登入身份:{client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
      return
    
    if message.content == '好聽':
        await message.channel.send('謝謝!!')
        
client.run('OTY4NDc3OTA5MTg0NTQ0Nzk4.GirQpQ.jwJI-ZERRlT1S68ghUVqU-8tK6uSA7gTSc7cQ8')