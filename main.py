import discord
import os
from webserver import keep_alive
from discord.ext import commands


help_command = commands.DefaultHelpCommand(
    no_category = 'Other Commands'
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

@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
  client.load_extension(f"cogs.{extension}")
  await ctx.send(f"{extension} loaded")

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
  client.unload_extension(f"cogs.{extension}")
  await ctx.send(f"{extension} unloaded")

@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
  client.unload_extension(f"cogs.{extension}")
  client.load_extension(f"cogs.{extension}")
  await ctx.send(f"{extension} reloaded")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
      client.load_extension(f"cogs.{filename[:-3]}")

@client.command(
        help="Shows the ping/latency of the bot in miliseconds.",
        brief="Shows ping"
)
async def ping(ctx):
    await ctx.send(f"🏓 Pong!\n{round(client.latency * 1000)}ms")

client.load_extension('jishaku')

keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")

client.run(TOKEN)
