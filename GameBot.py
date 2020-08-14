import discord
import asyncio
import random

client = discord.Client()
virus_done = []


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("도움")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    #안내
    if message.content.startswith("?도움"):
        embed = discord.Embed(title="명령어 목록", description="설치마법사는 이것을 할 수 있습니다:",color=0x394de4)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721057536416940198/740398195343097935/8476ead61564aee0.png")
        embed.add_field(name="?주사위\n굴릴횟수d면의갯수",value="주사위를 굴립니다.",inline=True)
        embed.add_field(name="?랜덤답변 질문",value="설치마법사가 예/아니오로 대답해줍니다",inline=True)
        embed.add_field(name="?뽑기 추첨리스트",value="리스트에서 하나를 추첨해줍니다.",inline=True)
        embed.add_field(name="?야바위",value="세 개의 컵중 하나에 공을 넣고 섞습니다. 결과는 디엠으로 발송됩니다.",inline=True)
        embed.add_field(name="?동전",value="동전을 던집니다. 앞면/뒷면 중 하나가 나옵니다.",inline=True)
        embed.add_field(name="?퀴즈 1, 2, 3",value="설치마법사가 퀴즈를 냅니다. 이틀에 한 번씩 업데이트 되며, 답변은 여러분이 정답을 맞혔을 때나 PIL에게 직접 물었을 때에 공개됩니다.")
        embed.add_field(name="?힌트 1, 2, 3",value="설치마법사가 번호에 따른 퀴즈의 힌트를 줍니다. 퀴즈가 어렵다면 물어보세요! 추가 힌트는 PIL에게 물어보면 받을지도?")
        embed.add_field(name="?젠가",value="여러분이 아는 바로 그 젠가입니다. 확률에 따라 탑이 무너질수도, 무너지지 않을 수도 있겠죠. 여러분의 운을 시험해보세요!")
        await message.channel.send(embed=embed)
        return
    #주사위
    if message.content.startswith("?주사위"):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(0, int(rolld[0])):
            dice = dice + random.randint(1, int(rolld[1]))
        await message.channel.send(str(dice))
        return
    #8ball
    elif message.content.startswith("?랜덤답변"):
        user = message.author.mention
        ans_list = ["이 마법사는 확신합니다","분명히 그렇습니다","이 마법사는 의심하지 않습니다","네, 그렇습니다","믿어도 괜찮습니다","제 주견으론 그러합니다","그럴 듯 합니다만", "보기엔 괜찮습니다","예","화살표가 네를 가리키는 것 같습니다", "이해할 수 없는 명령어 입니다", "나중에 다시 시도하여 주십시오", "지금은 대답을 실행 할 수 없습니다", "지금은 결과를 도출 할 수 없습니다","다시 명령하려면 명령어를 입력해주십시오", "게시자를 알 수 없는 질문입니다","이 마법사의 결론은 아니오 입니다","검색된 자료에 의하면 아니오 입니다","해당 질문은 좋음으로 판단되지 않습니다", "의심되는 질문입니다", "웃기지 마십시오", "당연한 거 아닙니까"]
        ans = random.choice(ans_list)
        await message.channel.send(str(user)+" "+ans)
        return
    #뽑끼이
    elif message.content.startswith("?뽑기"):
        players = message.content.split(" ")
        players.remove("?뽑기")
        lucky = random.choice(players)
        await message.channel.send("뽑기결과: "+str(lucky))
        return
    #야바위
    elif message.content.startswith("?야바위"):
        cups = ["첫 번째", "두 번째", "세 번째"]
        cup = random.randint(1,3)
        await message.channel.send("컵을 섞습니다...")
        await message.author.send("공은 "+str(cups[cup])+" 컵에 있습니다.")
    #동전던지기
    elif message.content.startswith("?동전"):
        coin = random.randint(1,2)
        if coin == 1:
            embed = discord.Embed(title="앞면입니다.", description="", color=0xfae43c)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/525550431930286091/740077564248457246/1024px-1848_CAL_Liberty_Head_quarter_eagle_obverse_transparent_background.png")
        elif coin == 2:
            embed = discord.Embed(title="뒷면입니다.", description="", color=0xfae43c)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/525550431930286091/740077556996374578/cb384480ce296036b6b5e9db285e1f38.png")
        await message.channel.send(embed=embed)
        return
    #데일리퀴즈
    elif message.content.startswith("?퀴즈"):
        asked = message.content.split(" ")
        quiz_list = ["B C D G J O P ? R S U, 이 알파벳들은 어떤 특별한 규칙을 가지고 배열되어 있습니다. ?에 들어가야 할 알파벳은 무엇일까요?","조커를 뺀 52장 1세트의 트럼프가 있습니다. 이를 잘 섞어서 26장씩 두 세트 A와 B로 나누었을 때, A에 있는 검은 카드의 매수와 B에 있는 빨간 카드의 매수가 정확히 일치하는 일은 1000번 중 정확히 몇 번 일어날 수 있을까요? (문제출처: 레이튼 시리즈)", "한 가게에서 케이스를 포함한 카메라가 310달러에 팔리고 있었습니다. 카메라 본체는 케이스보다 300달러가 비싸고, 나머지 금액이 케이스의 가격에 해당합니다. 케이스만 사기로 한 후 100달러 지폐로 지불했다면, 거스름돈은 얼마입니까?"]
        num = int(asked[1]) - 1
        quiz = str(quiz_list[num])
        await message.channel.send("```"+str(quiz)+"```")
    #힌트
    elif message.content.startswith("?힌트"):
        asked = message.content.split(" ")
        hint_list = ["선", "일반적인 카드의 빨간 카드의 수와 검은 카드의 수는?", "카메라의 가격과 케이스를 포함한 가격의 총 합은? (문제출처: 레이튼 시리즈)"]
        num = int(asked[1]) - 1
        hint = str(hint_list[num])
        await message.channel.send("```힌트: "+hint+"```")   
    #답
    elif message.content.startswith("?정답"):
        ans_list = ["Q, 풀이는 필에게 물어보세요.", "1000번 중 1000번입니다.", "95달러입니다."]
        ans = message.content.split(" ")
        asked = int(ans[1]) - 1
        answer = str(ans_list[asked])
        await message.channel.send("```정답: "+answer+"```")
    #조사지문
    elif message.content.startswith("?조사"):
        invest = message.content.split("$")
        await message.channel.purge(limit=1)
        await message.channel.send(invest[1])
    #설치마법사
    elif message.content.startswith("?설치마법사"):
        talk = message.content.split("$")  
        await message.channel.purge(limit=1)
        await message.channel.send('" '+talk[1]+' " -설치마법사')
    #젠가
    elif message.content.startswith("?젠가"):
        suc = random.randint(1,1000)
        user = message.author.mention
        await message.channel.send(str(user)+" 젠가를 뽑습니다...")
        if suc <= 800:
            await message.channel.send("앗!\n젠가가 안정적으로 뽑혔습니다. 성공!")
        elif suc > 800:
            await message.channel.send("앗!\n젠가가 와르르 하고 무너졌습니다. 게임 오버.")
    else:
        return


client.run("NzM4OTE2MjYxNDM3NjM2NzIw.XyS3ZQ.a9qdO63Cgc6UFMKj-s-iX26Xp8Q")
