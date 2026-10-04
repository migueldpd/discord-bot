from discord.ext import commands
import json

bad_words = ['shit','nigger','nigga']

class Eventos(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'we ready to go in {self.bot.user.name}')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        await member.send(f'Welcome my goat {member.name}')

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(f"Erro de comando  : {error}")

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user: 
            return

        with open('data.json','r') as file:
            x = json.load(file)

        with open('data.json','w') as file:
            id_stringified = str(message.author.id)
            if id_stringified in x:
                print("existe") 
                x[id_stringified] += 1
                json.dump(x,file,indent=4)
            else:
                print("nao existe") 
                x[id_stringified] = 1
                json.dump(x,file,indent=4)


        # id message.author.id


        for x in bad_words:
            if x in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention}, dont do that")
                return

        if 'amote' in message.content.lower():
            await message.channel.send('Querias dizer amo-te ? Seu pato.')


async def setup(bot):
    print("events cog loaded")
    await bot.add_cog(Eventos(bot))
