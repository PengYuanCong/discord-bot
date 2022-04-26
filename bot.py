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
    
    if message.content == 'spyXfamily':
        await message.channel.send('hello!')
        
client.run('OTY4NDc3OTA5MTg0NTQ0Nzk4.YmfbVg.M4ZnlBJtiQ4cY9BjLst-FbKj9zg')