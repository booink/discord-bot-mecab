import os
import MeCab
import discord

TOKEN = os.environ["TOKEN"]
PREFIX = "mecab "

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print("received message: " + str(message))
    if message.content.startswith(PREFIX):
        # 送り主がBotだった場合反応しない
        if client.user != message.author:
            print(message.content)

            splited_message = message.content.split() # スペースで分割する
            splited_message.pop(0) # 先頭は "mecab" なので不要
            content = splited_message.pop() # 末尾は解析対象の文字列として扱う
            option = ' '.join(splited_message) # "mecab " から "{対象文字列}" の間の文字列をスペースで連結する
            mecab = MeCab.Tagger(option)
            m = "```" + mecab.parse(content) + "```"
            print(m)

            # メッセージが送られてきたチャンネルへメッセージを送る
            await message.channel.send(m)

client.run(TOKEN)
