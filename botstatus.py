from xmlrpc import client
import discord
client = discord.Client()

@client.event
async def on_ready():
    print('目前登入身分:',client.user)
    status_w = discord.Status.dnd
    
    activity_w = discord.Activity(type=discord.ActivityType.listening, name="季節は次々死んでいく")
    await client.change_presence(status=status_w, activity=activity_w)
         
client.run('OTY4NDc3OTA5MTg0NTQ0Nzk4.YmfbVg.M4ZnlBJtiQ4cY9BjLst-FbKj9zg')