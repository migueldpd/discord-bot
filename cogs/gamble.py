import discord
from discord.ext import commands
import json,random

active_games = {}

class Gambler(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def dice(self,ctx,bet:int):
        if bet <= 0:
            await ctx.send('Invalid bet amount')
            return
        
        with open('data.json','r')as file:
            membro = json.load(file)
        stringified_id = str(ctx.author.id)
        saldo = membro[stringified_id]['balance']
        if bet <= saldo:  
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            soma = dice1 + dice2
            await ctx.send(f"🎲-{dice1} 🎲-{dice2}")
            await ctx.send(f"Total is {soma}")
            if soma == 7:
                await ctx.send('Its a draw')
            elif soma < 7:
                await ctx.send('You lost')
                saldo -= bet
            elif soma > 7:
                await ctx.send('You win')
                saldo += bet
            membro[stringified_id]['balance'] = saldo
            with open('data.json','w')as file:
                json.dump(membro,file,indent=4)
        else:
            await ctx.send('Not enough money')

    def countpoints(self,cartas:list):
        points = 0
        aces = 0
        for carta in cartas:
            if carta[:-2] in ['2','3','4','5','6','7','8','9','10']:
                points += int(carta[:-2])
            elif carta[:-2] in ['Q','J','K']:
                points += 10
            elif carta[:-2] in ['A']:
                points += 11
                aces += 1
        while points > 21 and aces > 0:
            points -= 10
            aces -= 1
        return points

    @commands.command()
    async def blackjack(self,ctx):
        user_id = str(ctx.author.id)
        naipes = ['♥️','♦️','♠️','♣️']
        valores = ['2','3','4','5','6','7','8','9','10','Q','J','K','A']
        baralho = []
        for naipe in naipes:
            for valor in valores:
                baralho.append(f'{valor}{naipe}')
        random.shuffle(baralho)
        player = [baralho.pop(),baralho.pop()]
        house = [baralho.pop(),baralho.pop()]
        active_games[user_id] = {
            'player':player,
            'house':house,
            'deck':baralho
        }
        emb = discord.Embed(title="**🃏 BLACKJACK**")
        emb.description = f"Player\n{player[0]}{player[1]}\n{self.countpoints(active_games[str(ctx.author.id)]['player'])}Points\n\nHouse\n{house[0]}\n ? Points\n\n!hit | !stand"
        await ctx.send(embed=emb)
        if self.countpoints(active_games[str(ctx.author.id)]['player']) == 21 and len(active_games[str(ctx.author.id)]['player']) == 2:
            await ctx.send('YOU HAVE BLACKJACK')
            await ctx.send('HOUSE CARDS : ' + ''.join(active_games[str(ctx.author.id)]['house']))
            if self.countpoints(active_games[str(ctx.author.id)]['house']) == 21:
                await ctx.send('DRAW...')
                del active_games[str(ctx.author.id)]
                return
            elif self.countpoints(active_games[str(ctx.author.id)]['house']) < 21:
                await ctx.send('PLAYER WINS')
                del active_games[str(ctx.author.id)]
                return
        
    @commands.command()
    async def hit(self,ctx):
        if str(ctx.author.id) in active_games:
            hit_card = active_games[str(ctx.author.id)]['deck'].pop()
            active_games[str(ctx.author.id)]['player'].append(hit_card)
            pontos_jogador = self.countpoints(active_games[str(ctx.author.id)]['player'])
            emb = discord.Embed(title="!hit")
            emb.description = f"Player\n" + ''.join(active_games[str(ctx.author.id)]['player'])+f"\n{self.countpoints(active_games[str(ctx.author.id)]['player'])}Points\n\n"
            emb.description += f"House\n"+''.join(active_games[str(ctx.author.id)]['house'])+f"\n{self.countpoints(active_games[str(ctx.author.id)]['house'])}Points"
            await ctx.send(embed=emb)
            if pontos_jogador > 21:
                emb.description += "\n\n**You lost**"
                await ctx.send(embed=emb)
                del active_games[str(ctx.author.id)]
                return
            elif pontos_jogador == 21:
                emb.description += "\n\n**You win**"
                await ctx.send(embed=emb)
                del active_games[str(ctx.author.id)]
                return
        else:
            await ctx.send('**There is no current blackjack game under your name**')

    @commands.command()
    async def stand(self,ctx):
        if str(ctx.author.id) in active_games:
            emb = discord.Embed(title='!stand')
            emb.description = f'Player\n'+''.join(active_games[str(ctx.author.id)]['player'])+f"\n{self.countpoints(active_games[str(ctx.author.id)]['player'])}Points\n\n"
            emb.description += f'House\n'+''.join(active_games[str(ctx.author.id)]['house'])+f"\n{self.countpoints(active_games[str(ctx.author.id)]['house'])}Points\n\n"
            await ctx.send(embed=emb)
            while self.countpoints(active_games[str(ctx.author.id)]['house']) < 17:
                carta = active_games[str(ctx.author.id)]['deck'].pop()
                active_games[str(ctx.author.id)]['house'].append(carta)
                emb.description += f"House\n"+''.join(active_games[str(ctx.author.id)]['house'])+f"\n{self.countpoints(active_games[str(ctx.author.id)]['house'])}Points"
                await ctx.send(embed=emb)
            if self.countpoints(active_games[str(ctx.author.id)]['house']) > 21:
                emb.description += "\n\n**House bust, Player wins**"
                await ctx.send(embed=emb)
                del active_games[str(ctx.author.id)]
                return

            if self.countpoints(active_games[str(ctx.author.id)]['house']) > self.countpoints(active_games[str(ctx.author.id)]['player']):
                emb.description += "**House wins**"
                await ctx.send(embed=emb)
                del active_games[str(ctx.author.id)]
            elif self.countpoints(active_games[str(ctx.author.id)]['house']) < self.countpoints(active_games[str(ctx.author.id)]['player']):
                emb.description += "**Player wins**"
                await ctx.send(embed=emb)
                del active_games[str(ctx.author.id)]
            else:
                emb.description += "**Its a draw**"
                await ctx.send(embed=emb)
                del active_games[str(ctx.author.id)]
        else:
            await ctx.send('**There is no current blackjack game under your name**')
        
async def setup(bot):
    print("Gambler Cog loaded")
    await bot.add_cog(Gambler(bot))