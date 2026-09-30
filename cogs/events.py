from discord.ext import commands

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
