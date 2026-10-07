import discord
from discord.ext import commands
import json,random

class Gambler(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #?dice [aposta] [número]
    
    @commands.command()
    async def dice(self,ctx,bet:int,number:int):
        with open('data.json','r')as file:
            members = json.load(file)
            id_string = str(ctx.author.id)
        if number >= 1 and number <= 6:#if dice 1-6
            if bet <= members[id_string]['coins']:#if has money higher than bet
                dice_number = random.randint(1,6)
                await ctx.send("Rotating dice . . . ")
                await ctx.send(f"🎲 - {dice_number}")
                if number == dice_number:
                    await ctx.send(f'🎊 You guessed it and won {bet}')
                    members[id_string]['coins'] += bet
                else:
                    await ctx.send(f'❌ You missed and lost {bet}')
                    members[id_string]['coins'] -= bet
            else:
                await ctx.send('No money')
        else:
            await ctx.send('Our dice is only 1 to 6')
        with open('data.json','w') as file:
            json.dump(members,file,indent=4)

async def setup(bot):
    print("Gambler Cog loaded")
    await bot.add_cog(Gambler(bot))