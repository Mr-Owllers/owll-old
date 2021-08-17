import discord
import random
import os
from webserver import keep_alive
from discord.ext import commands

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

client = commands.Bot(
    command_prefix = commands.when_mentioned_or('owl.'),
    case_insensitive=True,
    help_command = help_command
)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('eating mice (type owl.help for help)'))
    print('owll is alive!')

@client.event
async def on_member_join(member):
            print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
            print(f'{member} has left (or was removed from) the server')

@client.command(
        help="funny command"
)
async def yeet(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻ YAAAA YEEEEEEEET!!!!")

@client.command(
        help="Shows the ping/latency of the bot in miliseconds.",
        brief="Shows ping"
)
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")

@client.command(
        aliases=["8ball"],
        help="ask me anything"
)
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(
        help="filps a coin... duh"
)
async def coinflip(ctx):
    flip = ['heads', 'tails']
    await ctx.send(f'{random.choice(flip)}')

@client.command(
        help="in choice use 👊, ✌️, ✋, rock, paper or scissors"
)
async def rps(ctx, choice):
    pc=['👊', '✌️', '✋', 'rock', 'paper', 'scissors']
    choices=['👊', '✌️', '✋']
    if choice not in pc:
        await ctx.send("error: please put :punch:, :raised_hand: or :v:")
    else:
        await ctx.send(random.choice(choices))

@client.command(
        help="in choice use 👊, 🐶, ✋, punch, pet assist, slap"
)
async def fight(ctx, choice):
    pf=['👊', '🐶', '✋', 'punch', 'pet', 'slap']
    fight=['I 👊 (punch)', 'My 🐶 (pet) bites', 'I ✋ (slap)']
    dam=['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95', '100']
    if choice not in pf:
        await ctx.send("error: please put :punch:, :raised_hand:, :dog:, punch, slap or pet")
    else:
        await ctx.send(f'{random.choice(fight)} you\nI deal {random.choice(dam)}% damage\nYou deal {random.choice(dam)}% damage')

@client.command(
        help="more info ig"
)
async def h(ctx):
    await ctx.send("```\n---------\nyeet\njust a fun command\n---------\nping\ncheck the ping\n---------\n8ball <question>\nask anything\n---------\ncoinflip\nflips a coin for you\n---------\nrps <👊, ✌️, ✋, rock, paper or scissors>\nrock paper scissors\n---------\nfight <👊, 🐶, ✋, punch, pet, slap>\nfight da bot\n---------\ncoded by Mr.Owllers#0001\n---------\n```")

keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
