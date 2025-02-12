
import discord
from discord.ext import commands
import token
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')




@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba!')

@bot.command()
async def naber(ctx):#dd
    await ctx.send(f'iyiyim ya sen!')
@bot.command()
async def iyiyimbende(ctx):#dd
    await ctx.send(f'çok iyi')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def i(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum! bende oluşan minik bir hata olayıyla yazcağığınız kelimeleri birleşik yazınız lütfen. teşekkür ederim thanks kuralları öğrenmek için bana kural yazabilirsin')

@bot.command()
async def kurallar(ctx):
    await ctx.send(f'kurallar burada küfür ve benzeri şeyler söylemek yasaktır gif veya link paylaşmak yasaktır ve son olarak lütfen burada başkalarıyla saygılı konuşalım. ')
@bot.command()
async def kendinitanıtırmısın(ctx):
    await ctx.send(f' Ben {bot.user}, bir Discord sohbet botuyum! ve daha geliştirme aşamasındayım')

@bot.command()
async def buranınkonusune(ctx):
    await ctx.send(f'burada herkes kendi oyunlarından kesit paylaşabileceği bir oda')

@bot.command()
async def yokartık(ctx):
    await ctx.send(f'evet')

@bot.command()
async def nasılgidiyo(ctx):
    await ctx.send(f'iyii')


@bot.command()
async def sjsj(ctx):
    await ctx.send(f'sjsj')



# @bot.command()
# async def parola(ctx):
#     sifre = sifre_olustur(10)
#     await ctx.send("sizi için oluşturulan şifre     :      "  + sifre_olustur(10))



@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



@bot.command()
async def algila(ctx):
    await ctx.send("Algılama başladı!")
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
            await ctx.send("Görsel kaydedildi!")
    else:
      await ctx.send("Lütfen komutla birlikte bir görsel yükleyin!")










bot.run('token')


