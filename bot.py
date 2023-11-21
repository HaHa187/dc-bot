import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents = intents)

@bot.event
async def on_ready():
    print("Bot is ready")
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()    
async def add(ctx, x, y):
    result = int(x) + int(y)
    await ctx.send(f"{x} + {y} = {result}") 

@bot.command()  
async def minus(ctx, x, y):
    result = int(x) - int(y)
    await ctx.send(f"{x} - {y} = {result}")

@bot.command()  
async def multiple(ctx, x, y):
    result = int(x) * int(y)
    await ctx.send(f"{x} * {y} = {result}")

@bot.command()  
async def devide(ctx, x, y):
    result = int(x) / int(y)
    await ctx.send(f"{x} / {y} = {result}") 



bot.run("MTE3NjUzOTEwMTMzMjI0NjYxOA.Ge8lxY.9sDjqupfARYB6LTMWAjkkMUDJ8g-dnrqzLjbOo")
