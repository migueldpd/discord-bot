import discord
from discord.ext import commands
import random,json
import requests
from cogs.quiz import active_quiz, questions
import datetime as dt

bandeiras = {
    "Australia": "🇦🇺",
    "China": "🇨🇳",
    "Japan": "🇯🇵",
    "USA": "🇺🇸",
    "Canada": "🇨🇦",
    "Monaco": "🇲🇨",
    "Spain": "🇪🇸",
    "Austria": "🇦🇹",
    "UK": "🇬🇧",
    "Belgium": "🇧🇪",
    "Hungary": "🇭🇺",
    "Netherlands": "🇳🇱",
    "Italy": "🇮🇹",
    "Azerbaijan": "🇦🇿",
    "Malaysia": "🇲🇾",
    "Singapore": "🇸🇬",
    "Mexico": "🇲🇽",
    "Brazil": "🇧🇷",
    "Qatar": "🇶🇦",
    "UAE": "🇦🇪"
}
nacionalidades = {
    "Italian": "🇮🇹",
    "British": "🇬🇧",
    "Monegasque": "🇲🇨",
    "Dutch": "🇳🇱",
    "French": "🇫🇷",
    "German": "🇩🇪",
    "Australian": "🇦🇺",
    "Argentine": "🇦🇷",
    "Brazilian": "🇧🇷",
    "Finnish": "🇫🇮",
    "Mexican": "🇲🇽",
    "Spanish": "🇪🇸",
    "Japanese": "🇯🇵",
    "Thai": "🇹🇭",
    "Canadian": "🇨🇦",
    "New Zealander": "🇳🇿",
    "American": "🇺🇸",
    "Danish": "🇩🇰",
    "Austrian": "🇦🇹",
    "Belgian": "🇧🇪",
    "Chinese": "🇨🇳",
    "Polish": "🇵🇱",
    "Russian": "🇷🇺",
    "Swiss": "🇨🇭",
    "Portuguese": "🇵🇹",
    "Indian": "🇮🇳",
    "Colombian": "🇨🇴"
}

#bot_commands id = 1554604290264539196

class Comandos(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #F1 COMMANDS START HERE
    #f1 channel = 1556371161653448746
    @commands.command()
    async def f1season(self,ctx,number:int):
        if ctx.channel.id == 1556371161653448746:
            if number >= 1950 and number <= 2026:
                emb = discord.Embed(title=f'Standings of the {number} season',color=0xFF1801)
                emb.set_thumbnail(url='https://images.fastcompany.com/image/upload/f_auto,q_auto,c_fit/wp-cms/uploads/2017/11/p-1-formula-one.jpg')
                url = f'https://api.jolpi.ca/ergast/f1/{number}/driverstandings/'
                resposta = requests.get(url)
                dados = resposta.json()
                pilotos = dados['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
                embed_string = ''
                for i,piloto in enumerate(pilotos):
                    nacionalidade = piloto['Driver']['nationality']
                    embed_string += f"{i+1}. **{nacionalidades.get(nacionalidade,'🏳️')} {piloto['Driver']['givenName']}** **{piloto['Driver']['familyName']}** - {piloto['points']}\n"
                emb.description = embed_string
                await ctx.send(embed=emb)
            else:
                await ctx.send('Season impossible to load')
        else:
            await ctx.send(f"This command only goes in the <#1556371161653448746> channel")

    @commands.command()
    async def f1leaderboard(self,ctx):
        if ctx.channel.id == 1556371161653448746:
            url = 'https://api.jolpi.ca/ergast/f1/2026/driverstandings'
            resposta = requests.get(url)
            dados = resposta.json()
            pilotos = dados['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
            embedf1 = discord.Embed(color=0xE10600,title='🏎️ F1 Standings 2026')
            embedf1.set_thumbnail(url='https://images.fastcompany.com/image/upload/f_auto,q_auto,c_fit/wp-cms/uploads/2017/11/p-1-formula-one.jpg')
            embed_string = ""
            for i,piloto in enumerate(pilotos):
                nacionalidade = piloto['Driver']['nationality']
                embed_string += f"{i+1}. **{nacionalidades.get(nacionalidade,'🏳️')} {piloto['Driver']['givenName']}** **{piloto['Driver']['familyName']}** - {piloto['points']}\n"
            embedf1.description = embed_string
            await ctx.send(embed=embedf1)
        else:
            await ctx.send(f"This command only goes in the <#1556371161653448746> channel")

    @commands.command()
    async def f1calendar(self,ctx):
        if ctx.channel.id == 1556371161653448746:
            url = 'https://api.jolpi.ca/ergast/f1/2026/races'
            resposta = requests.get(url)
            dados = resposta.json()
            races = dados['MRData']['RaceTable']['Races']
            race_embed = discord.Embed(title='🏎️ F1 Calendar 2026 Season')
            calendar_string = ''
            for i,race in enumerate(races):
                bandeira_pais = race['Circuit']['Location']['country']
                calendar_string += f"**{i+1} - {bandeiras.get(bandeira_pais,'🏳️')} {race['raceName']} {race['date']}**\n"
            race_embed.description = calendar_string
            await ctx.send(embed=race_embed)
        else:
            await ctx.send(f"This command only goes in the <#1556371161653448746> channel")

    @commands.command()
    async def f1lastrace(self,ctx):
        if ctx.channel.id == 1556371161653448746:
            url = 'https://api.jolpi.ca/ergast/f1/2026/last/results/'
            result = requests.get(url)
            dados = result.json()
            corrida = dados['MRData']['RaceTable']['Races'][0]['Results'][0]
            nomeCorrida = dados['MRData']['RaceTable']['Races'][0]
            emb = discord.Embed(title=f"{bandeiras.get(nomeCorrida['Circuit']['Location']['country'],'🏳️')} {nomeCorrida['raceName']}")
            emb.description = f"Last race winner was {corrida['Driver']['givenName']} {corrida['Driver']['familyName']}"
            await ctx.send(embed=emb)    
        else:
            await ctx.send(f"This command only goes in the <#1556371161653448746> channel")

    #F1 COMMANDS END HERE     

    @commands.command()
    async def randomfact(self,ctx):
        with open('facts.json','r')as file:
            facts = json.load(file)
            await ctx.send(f"{random.choice(facts)}")

    #delete message inside a specific channel
    @commands.command()
    async def delete(self,ctx,number:int):
        await ctx.channel.purge(limit=number)

    #shows the avatar of that user
    @commands.command()
    async def avatar(self,ctx,member:discord.Member):
        image = member.display_avatar.url
        await ctx.send(image)

    #display information about a specific user
    @commands.command()
    async def userinfo(self,ctx,member:discord.Member):
        embed = discord.Embed(title='Info from user')
        embed.add_field(name='Nome ',value=member.name,inline=False)
        embed.add_field(name='Joined at ',value=member.joined_at,inline=False)
        embed.add_field(name='Account created in ',value=member.created_at,inline=False)
        embed.add_field(name='Top role ',value=member.top_role,inline=False)
        embed.add_field(name='Status',value=member.status,inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def quiz(self,ctx):
        pergunta = random.choice(questions)
        active_quiz[ctx.channel.id] = pergunta['answer']
        await ctx.send(pergunta['question'])
        await ctx.send(pergunta['options'])

    #1x1 on 2 specific users.Both get random values.
    @commands.command()
    async def faceoff(self,ctx,member1:discord.Member,member2:discord.Member):
        if member1 != member2:
            user1power = random.randint(1,100)
            user1speed = random.randint(1,100)
            user1dodge = random.randint(1,100)
            user2power = random.randint(1,100)
            user2speed = random.randint(1,100)
            user2dodge = random.randint(1,100)
            totalplayer1 = user1power + user1speed + user1dodge
            totalplayer2 = user2power + user2speed + user2dodge
            x = discord.Embed(title='Faceoff',colour=0xFF5C00,description=f"""
                {member1.mention}
                💪 Power: {user1power}
                ⚡ Speed: {user1speed}
                🍀 Dodge: {user1dodge}
                🔥 TOTAL POWER: {totalplayer1}

                VS

                {member2.mention}
                💪 Power: {user2power}
                ⚡ Speed: {user2speed}
                🍀 Dodge: {user2dodge}
                🔥 TOTAL POWER: {totalplayer2}
                """)
            await ctx.send(embed=x)
            if totalplayer1 > totalplayer2:
                await ctx.send(f"{member1.mention} wins !!!")
            elif totalplayer2 > totalplayer1:
                await ctx.send(f"{member2.mention} wins !!!")
            else:
                await ctx.send("Empataram")
        else:
            await ctx.send('Nao te podes enfrentar a ti mesmo :D')   

    @commands.command()
    async def howgay(self,ctx,member:discord.Member):
        random_number = random.randint(1,100)
        await ctx.send(f"{member} is {random_number}% gay")

    @commands.command()
    async def daily(self,ctx):
        with open('data.json','r') as file:
            pessoa = json.load(file)
            userid = str(ctx.author.id)
        now = dt.datetime.now().date()
        now_stringed = str(now)
        if pessoa[userid]['daily'] == now_stringed:
            await ctx.send('**You already redeemed your daily coins**')
        else:
            await ctx.send('**You received 1000 coins**')
            pessoa[userid]['balance'] += 1000
            pessoa[userid]['daily'] = now_stringed

        with open('data.json','w') as file:
            json.dump(pessoa,file,indent=4)

    @commands.command()
    async def rps(self,ctx,member:discord.Member):
        emb = discord.Embed(title='🎮 Rock Paper Scissors',description='Let the battle begin')
        rps = ['🗿','📃','✂️']
        player1 = random.choice(rps)
        player2 = random.choice(rps)
        emb.add_field(name=f'{ctx.author.name}',
                      value=f'{player1}',
                      inline=True
                      )
        emb.add_field(name=f'{member.name}',
                      value=f'{player2}',
                      inline=True
                      )
        if player1 == player2:
            await ctx.send('**DRAW**')
            return

        if ((player1 == '🗿' and player2 == '✂️') or
            (player1 == '📃' and player2 == '🗿') or
            (player1 == '✂️' and player2 == '📃')
        ):
            emb.add_field(name="🏆 Result",
                          value=f"**{ctx.author.name} WINS**",
                          inline=False
                         )
        else:
            emb.add_field(name="🏆 Result",
                          value=f"**{member.name} WINS**",
                          inline=False
                         )
        await ctx.send(embed=emb)

async def setup(bot):
    print("Commands Cog loaded")
    await bot.add_cog(Comandos(bot))