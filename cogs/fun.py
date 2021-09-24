import random
from discord.ext import commands

class Fun(commands.Cog):
  
  def __init__(self, client):
    self.client=client

  @commands.command(
        help="funny command"
  )
  async def yeet(self, ctx):
    async with ctx.typing():
      await ctx.send("(╯°□°）╯︵ ┻━┻ YAAAA YEEEEEEEET!!!!")

  @commands.command(
        aliases=["8ball"],
        help="ask me anything"
  )
  async def _8ball(self, ctx, *, question):
    async with ctx.typing():
      responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]
      await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

  @commands.command(
        help="filps a coin... duh"
  )
  async def coinflip(self, ctx):
    async with ctx.typing():
      flip = ['heads', 'tails']
      await ctx.send(f'{random.choice(flip)}')

  @commands.command(
        help="in choice use 👊, ✌️, ✋, rock, paper or scissors"
  )
  async def rps(self, ctx, choice):
    async with ctx.typing():
      pc=['👊', '✌️', '✋', 'rock', 'paper', 'scissors']
      choices=['👊', '✌️', '✋']
      if choice not in pc:
        await ctx.send("error: please put :punch:, :raised_hand:, :v:, rock, paper or scissors")
      else:
        await ctx.send(random.choice(choices))

  @commands.command(
        help="in choice use 👊, 🐶, ✋, punch, pet assist, slap"
  )
  async def fight(self, ctx, choice):
    async with ctx.typing():
      pf=['👊', '🐶', '✋', 'punch', 'pet', 'slap']
      fight=['I 👊 (punch)', 'My 🐶 (pet) bites', 'I ✋ (slap)']
      dam=['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95', '100']
      if choice not in pf:
        await ctx.send("error: please put :punch:, :raised_hand:, :dog:, punch, slap or pet")
      else:
        await ctx.send(f'{random.choice(fight)} you\nI deal {random.choice(dam)}% damage\nYou deal {random.choice(dam)}% damage')

def setup(client):
  client.add_cog(Fun(client))