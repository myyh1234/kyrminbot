import asyncio, discord
from discord.ext import commands

token = '여기에 토큰 넣기'
print('Token_key : ', token)

game = discord.Game('>도움말')

bot = commands.Bot(command_prefix='>', status=discord.Status.online, activity=game, help_command=None)

@bot.event
async def on_ready():
    print('kyr_min')

@bot.command(name='응애')
async def engae(ctx, number):
    num = int(number)
    ans = ''
    for i in range(num):
        ans += '나 아기 경록\n'
    await ctx.send(ans)

@bot.command(name='반복')
async def runrun(ctx, number, *word):
    ans = ''
    num = int(number)
    for i in range(num):
        l = len(word)
        ans += ' '.join(word) + '! '
    await ctx.send(ans)

@bot.command(name='민경록은')
async def bt(ctx):
    await ctx.send('변태가 맞습니다')

@bot.command(name='도움말')
async def helphelp(ctx):
    await ctx.send('명령어 모음\n>응애 [반복 횟수]\n>반복 [반복 횟수] [반복할 문장]\n>민경록은')

bot.run(token)
