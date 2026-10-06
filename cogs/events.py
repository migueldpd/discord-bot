from discord.ext import commands
import json
from cogs.quiz import active_quiz

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
    async def on_voice_state_update(self,member,before,after):
        channelbotlog = member.guild.get_channel(1556693088385114315)
        if not before.channel and after.channel:
            await channelbotlog.send(f"{member.display_name} joined voice")
        if before.channel and not after.channel:
            await channelbotlog.send(f"{member.display_name} left voice")


    @commands.Cog.listener()
    async def on_message(self,message):
        #quizz
        if message.channel.id in active_quiz:
            answer = active_quiz[message.channel.id]
            if message.content.upper() == answer:
                await message.channel.send('🎊 Spot on')
                del active_quiz[message.channel.id]
            elif message.content.upper() in ['A', 'B', 'C', 'D']:
                await message.channel.send('❌ Wrong answer')
                del active_quiz[message.channel.id]


        channelbotlog = self.bot.get_channel(1556693088385114315)
        if message.author == self.bot.user: 
            return

        #1556693088385114315 id do bot log
        
        with open('data.json','r') as file:
            x = json.load(file)
            id_stringified = str(message.author.id)
            if id_stringified in x:
                x[id_stringified]['xp'] += 1
                x[id_stringified]['coins'] += 5
            else:
                x[id_stringified] = {'xp': 1,'coins':10,'slotsplayed':0}
        with open('data.json','w') as file:
            json.dump(x,file,indent=4)

        # id message.author.id
        for x in bad_words:
            if x in message.content.lower():
                await channelbotlog.send(f"{message.author} enviou **{message.content}**")
                await message.delete()
                await message.channel.send(f"{message.author.mention}, dont do that")
                return

        if 'amote' in message.content.lower():
            await message.channel.send('Querias dizer amo-te ? Seu pato.')

        
        await channelbotlog.send(f"{message.author} enviou {message.content}")


async def setup(bot):
    print("events cog loaded")
    await bot.add_cog(Eventos(bot))
