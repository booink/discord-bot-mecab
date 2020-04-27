import os
import MeCab
import discord
import traceback
from discord.ext import commands

TOKEN = os.environ["TOKEN"]

bot = commands.Bot(command_prefix='!', description='Output to results of morphological analysis.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def mecab(ctx, *args):
    print("received message: " + str(args))
    if bot.user != ctx.message.author:
        l = list(args)
        content = l.pop() # 末尾は解析対象の文字列として扱う
        print(content)

        option = ' '.join(l)
        mecab = MeCab.Tagger(option)
        m = "```" + mecab.parse(content) + "```"
        print(m)

        # メッセージが送られてきたチャンネルへメッセージを送ります
        await ctx.send(m)

def main():
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        exit(1)

if __name__ == '__main__':
    main()

