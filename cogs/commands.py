import discord
from discord.ext import commands
import random

class Comandos(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

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


async def setup(bot):
    print("Commands cog loaded")
    await bot.add_cog(Comandos(bot))