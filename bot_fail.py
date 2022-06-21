import discord
from discord.ext import commands
import json
import random
import os
from core.test_classes import Cog_Extension


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

@commands.Cog.listener()
async def on_voice_state_update(self, member, before, after):
        print ('yes')
        if after.channel != None:
            guild = self.bot.get_guild(after.channel.guild.id)
            for channel in guild.channels:
                if str(channel.type) == "text":
                    text_channel = self.bot.get_channel(channel.id)
                    break
        if before.channel == None and after.channel != None and member.bot != True:
            SayHello = ['Hi ❤', 'Hey！','Welcome!(◍•ᴗ•◍)']
            flag = False
            for user in jdata['user']:
                # print(user)
                tmp = jdata['user'][user]
                if member.id == tmp['id']:
                    pic = tmp['hello']
                    random_hello = random.choice(SayHello)
                    await text_channel.send(f'{member.mention} {random_hello}')
                    if tmp['hello'] != "":
                        pic = tmp['hello']
                        await text_channel.send(pic)
                    else:
                        filepath = "C:\Users\zxc39\OneDrive\Documents\github\discord-bot\picture" #圖庫路徑
                        imagelist = os.listdir(filepath)
                        pic = random.choice(imagelist)
                        # 若跟上次的圖片一樣則繼續選
                        while pic == self.last_random_pic:
                            pic = random.choice(imagelist)
                        self.last_random_pic = pic
                        filepath = filepath + '/' + pic
                        pic = discord.File(os.getcwd()+"/"+filepath)
                        await text_channel.send(file = pic)
                        
                    flag = True
                    break
            # 沒找到相對應的使用者名稱
            if flag == False:
                filepath = "C:\Users\zxc39\OneDrive\Documents\github\discord-bot\picture" #圖庫路徑
                imagelist = os.listdir(filepath)
                pic = random.choice(imagelist)
                # 若跟上次的圖片一樣則繼續選
                while pic == self.last_random_pic:
                    pic = random.choice(imagelist)
                self.last_random_pic = pic
                filepath = filepath + '/' + pic
                pic = discord.File(os.getcwd()+"/"+filepath)
                random_hello = random.choice(SayHello)
                await text_channel.send(f'{member.mention} {random_hello}')
                await text_channel.send(file = pic)
                
                
        elif before.self_stream == False and after.self_stream ==True:
            await text_channel.send(f'{member.mention} is streaming now!')
