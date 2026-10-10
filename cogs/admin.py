from discord.ext import commands
import discord
import json

class Admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    ADMIN_ROLE_ID = 1181426834282381403
    @commands.command()
    async def givemoney(self,ctx,number:int,member:discord.Member):
        await ctx.channel.purge(limit=1)
        if any(role.id == self.ADMIN_ROLE_ID for role in ctx.author.roles):
            with open('data.json','r') as file:
                membros = json.load(file)
            member_receiver_id = str(member.id)
            membros[member_receiver_id]['balance'] += number
            emb = discord.Embed()
            emb.color = 0x008000
            emb.title = f'Balance added to {member.name}'
            emb.description = f"New balance is {membros[member_receiver_id]['balance']}"
            await ctx.send(embed=emb)
            with open('data.json','w') as file:
                json.dump(membros,file,indent=4)
        else:
            await ctx.send("You dont have permission to do that")

    @commands.command()
    async def resetmoney(self,ctx,member:discord.Member):
        await ctx.channel.purge(limit=1)
        if any(role.id == self.ADMIN_ROLE_ID for role in ctx.author.roles):
            with open('data.json','r') as file:
                membros = json.load(file)
            member_receiver_id = str(member.id)
            membros[member_receiver_id]['balance'] = 0
            emb = discord.Embed()
            emb.color = 0xFF0000
            emb.title = f'Resetted balance to {member.name}'
            emb.description = f"New balance is {membros[member_receiver_id]['balance']}"
            await ctx.send(embed=emb)
            with open('data.json','w') as file:
                json.dump(membros,file,indent=4)
        else:
            await ctx.send("You dont have permission to do that")

    @commands.command()
    async def viewdata(self,ctx):
        if any(role.id == self.ADMIN_ROLE_ID for role in ctx.author.roles):
            with open('data.json','r')as file:
                membros = json.load(file)
            for membro_id,membro in membros.items():
                emb = discord.Embed()
                emb.title = f"👤 {membro['username']}"
                emb.description = f"XP:{membro['xp']}\nBalance:{membro['balance']}"
                await ctx.send(embed=emb)
        else:
            await ctx.send('You dont have permission to do that')

async def setup(bot):
    print("Admin Cog loaded")
    await bot.add_cog(Admin(bot))
