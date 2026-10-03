import discord
from discord.ext import commands
import random,json
import requests

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
    "UAE": "🇦🇪",
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
}

class Comandos(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #F1 COMMANDS START HERE
    @commands.command()
    async def f1leaderboard(self,ctx):
        url = 'https://api.jolpi.ca/ergast/f1/2026/driverstandings'
        resposta = requests.get(url)
        dados = resposta.json()
        pilotos = dados['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        embedf1 = discord.Embed(color=0xE10600,title='🏎️ F1 Standings 2026 1/2')
        embedf1.set_thumbnail(url='https://images.fastcompany.com/image/upload/f_auto,q_auto,c_fit/wp-cms/uploads/2017/11/p-1-formula-one.jpg')
        embed_string = ""
        for i,piloto in enumerate(pilotos):
            nacionalidade = piloto['Driver']['nationality']
            embed_string += f"{i+1}. **{nacionalidades.get(nacionalidade,'🏳️')} {piloto['Driver']['givenName']}** **{piloto['Driver']['familyName']}** - {piloto['points']}\n"
        embedf1.description = embed_string
        await ctx.send(embed=embedf1)

    @commands.command()
    async def f1calendar(self,ctx):
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

    @commands.command()
    async def f1lastrace(self,ctx):
        url = 'https://api.jolpi.ca/ergast/f1/2026/last/results/'
        result = requests.get(url)
        dados = result.json()
        corrida = dados['MRData']['RaceTable']['Races'][0]['Results'][0]
        nomeCorrida = dados['MRData']['RaceTable']['Races'][0]
        emb = discord.Embed(title=f"{bandeiras.get(nomeCorrida['Circuit']['Location']['country'],'🏳️')} {nomeCorrida['raceName']}")
        emb.description = f"Last race winner was {corrida['Driver']['givenName']} {corrida['Driver']['familyName']}"
        await ctx.send(embed=emb)
    

    #F1 COMMANDS END HERE

    @commands.command()
    #admin 882269198758326342
    @commands.has_role('882269198758326342')
    async def checkrole(self,ctx):
        await ctx.send('ADMIN ROLE')
        

    @commands.command()
    async def hello(self,ctx):
        print("hello executado")
        await ctx.send(f"Hello {ctx.author.mention}")

    @commands.command()
    async def delete(self,ctx,number:int):
        await ctx.channel.purge(limit=number)

    @commands.command()
    async def avatar(self,ctx,member:discord.Member):
        image = member.display_avatar.url
        await ctx.send(image)

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
    async def roast(self,ctx,member:discord.Member):
        x = random.randint(0,6)
        if x == 1:
            await ctx.send(f'És podre {member.mention}')
        elif x == 2:
            await ctx.send(f'Feiolas {member.mention}')
        elif x == 3:
            await ctx.send(f'Não vales nada {member.mention}')
        elif x == 4:
            await ctx.send(f'Odeio você demais {member.mention}')
        elif x == 5:
            await ctx.send(f'Tu não és ele {member.mention}')

    @commands.command()
    async def compliment(self,ctx,member:discord.Member):
        await ctx.channel.purge(limit=1)
        x = random.randint(0,6)
        if x == 1:
            await ctx.send(f'O GOAT {member.mention}')
        elif x == 2:
            await ctx.send(f'Tu és ele {member.mention}')
        elif x == 3:
            await ctx.send(f'És espetacular {member.mention}')
        elif x == 4:
            await ctx.send(f'Muito lindo {member.mention}')
        elif x == 5:
            await ctx.send(f'You are him {member.mention}')

    @commands.command()
    async def dice(self,ctx):
        x = random.randint(1,6)
        await ctx.send(f'**{x}**')

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
    async def checkxp(self,ctx):
        with open('data.json','r') as file:
            data = json.load(file)

        await ctx.send(f'Your xp is : {data[str(ctx.author.id)]+1}')

    @commands.command()
    async def leaderboard(self,ctx):
        print("LEADERBOARD")
        with open('data.json','r') as file:
            data = json.load(file)
            ordered = sorted(data,key=data.get,reverse=True)
        mensagem = ""
        for x in ordered:
            mensagem += f"ID: {self.bot.get_user(int(x))} - XP: {data[x]}\n"
        await ctx.send(mensagem)


async def setup(bot):
    print("Commands cog loaded")
    await bot.add_cog(Comandos(bot))