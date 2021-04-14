import asyncio, discord, datetime, pytz
from discord.ext import commands

token = 'ODE3NDI3NTkyOTgxMjUwMDQ5.YEJWxQ.Fv9MKIntVBN2pLUMouFR7s68CJs'
print('Token_key : ', token)

game = discord.Game('>도움말')

bot = commands.Bot(command_prefix='>', status=discord.Status.online, activity=game, help_command=None)

time_table = ['',
'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n'),

'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n'),

'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n'),

'''일본어 문학 물리 웹프 웹프 한국사 주제
일본어 영어B 운동 서버구축 서버구축 진로 문학
수학 공업수학 웹프 웹프 자료구조 자료구조 동아리
한국사 수학 물리 영어A 문학 서버구축 서버구축
자료구조 자료구조 영어A 한국사 수학 자율'''.split('\n'),

'''자료구조 자료구조 영어IA 문학A 한국사 서버구축 서버구축
영어IA 문학B 웹프 웹프 영어IB 수학I 한국사
물리1 일본어 한국사 공업수학 주제 수학I 동아리
자료구조 자료구조 문학A 운동 웹프 웹프 일본어
물리1 수학I 진로2 서버구축 서버구축 자율'''.split('\n'),

'''영어IA 수학I 일본어 서버구축 서버구축 자료구조 자료구조
주제 한국사 물리1 영어IB 문학A 웹프 웹프
운동 문학B 수학I 물리1 한국사 영어IA 동아리
서버구축 서버구축 공업수학 수학I 자료구조 자료구조 한국사
문학A 일본어 진로2 웹프 웹프 자율'''.split('\n'),

'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n'),

'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n'),

'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n'),

'''스콘 스콘 한국사 운동 시디 시디 시디
영어A 문학 진로 주제 수학 한국사 통과
스콘 스콘 수학 통과 시디 시디 동아리
영어 웹프 일본어 문학 한국사 수학 영어B
웹프 웹프 통과 일본어 문학 자율'''.split('\n'),

'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n'),

'''몰랑
몰랑
몰랑
몰랑
몰랑'''.split('\n')]

day_list = {'월' : 0, '화' : 1, '수' : 2, '목' : 3, '금' : 4}

file = discord.File("classroom.png")

@bot.event
async def on_ready():
    print('kyr_min')

@bot.command(name='응애')
async def engae(ctx, *number):
    print('응애')
    if number:
        num = int(number[0])
        ans = ''
        for i in range(num):
            ans += '나 아기 경록\n'
        try:
            await ctx.send(ans)
        except:
            await ctx.send('적당히 해')
    else:
        await ctx.send('나 아기 경록')

@bot.command(name='반복')
async def runrun(ctx, number, *word):
    print('반복')
    ans = ''
    num = int(number)
    for i in range(num):
        l = len(word)
        ans += ' '.join(word) + '! '
    try:
        await ctx.send(ans)
    except:
        await ctx.send('적당히 해')

@bot.command(name='민경록은')
async def bt(ctx):
    print('민경록은')
    await ctx.send('변태가 맞습니다')

@bot.command(name='도움말')
async def helphelp(ctx):
    print('도움말')
    await ctx.send('명령어 모음\n>응애 [반복 횟수]\n>반복 [반복 횟수] [반복할 문장]\n>민경록은\n>시간표 [반 번호] [요일 | 입력하지 않으면 오늘 시간표 출력]\n>검색 [검색어] [연관검색어 | 여러 개 입력 가능]')

@bot.command(name='시간표')
async def printshow(ctx, got_class, *got_day):
    print('시간표')
    nowday = ''
    if got_day:
        nowday = got_day[0]
    else:
        print(datetime.datetime.now(pytz.timezone('Asia/Seoul')))
        nowday = "월화수목금토일"[datetime.datetime.now(pytz.timezone('Asia/Seoul')).weekday()]
    if nowday[0] in day_list:
        class_num = int(got_class)
        if 1 <= class_num <= 12:
            await ctx.send(time_table[class_num][day_list[nowday[0]]])
        else:
            await ctx.send('아잇씨팔 반이 틀렸잖아')
    elif nowday == '토' or nowday == '일':
        await ctx.send(nowday + '요일이잖아')
    else:
        await ctx.send('아잇씨팔 요일이 틀렸잖아')

@bot.command(name='검색')
async def print_search(ctx, word, *related):
    print('검색')

    bar = '''┌──────────┐
 ⌕ %s           　            
└──────────┘''' % word

    rel = '''연관 검색어'''
    for i in related:
        rel += '\n↳%s' % i

    keyboard = '''__
  ㅣ  ¹     ·   ²    ㅡ³    ⌫
ㄱㅋ ⁴ ㄴㄹ⁵  ㄷㅌ⁶     ↲
ㅂㅍ ⁷  ㅅㅎ⁸   ㅈㅊ⁹     ?! ,.'''
    await ctx.send(bar + '\n' + rel + '\n' + keyboard)

@bot.command(name='이동')
async def print_classroom(ctx):
    print('이동')
    await ctx.send(file=file)

bot.run(token)
