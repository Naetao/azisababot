
import discord
from discord import member
from discord.ext import commands

bot = commands.Bot(command_prefix="/",help_command=None)

@bot.event
async def on_ready():
        print("起動完了")

@bot.event
async def on_message(message):
        user = message.author
        if 'discord.gg' in message.content:
                if "運営" in [role.name for role in user.roles]:
                        await bot.process_commands(message)
                else:
                        await message.delete()
        else:
                await bot.process_commands(message)
#discord.ggが含んでいる文章を削除する機能

@bot.command(name='commands', description="コマンド一覧を表示する")
async def commands(ctx):
        embedhelp = discord.Embed(title="AzisabaBot",description="AzisabaBotCommands",color=0x00fffa)
        embedhelp.set_thumbnail(url="https://server-icon.minecraft.jp/59b7c551a9b0bd23dc00834d.png?1597177300")
        embedhelp.add_field(name="/commands",value="このコマンド一覧を表示します。",inline=False)
        embedhelp.add_field(name="/support",value="サポートの詳細を表示します。",inline=False)
        embedhelp.add_field(name="/links",value="アジ鯖のリンク一覧を表示します。",inline=False)
        embedhelp.add_field(name="/vote",value="アジ鯖の投票サイトを表示します。",inline=False)
        embedhelp.add_field(name="/buy",value="アジ鯖の寄付サイトを表示します。",inline=False)
        embedhelp.add_field(name="/wiki",value="アジ鯖のwikiを表示します。",inline=False)
        embedhelp.add_field(name="/color ######",value="名前に色を付けます。",inline=False)
        embedhelp.add_field(name="/colorcheck ######",value="入力した色を確認できます。",inline=False)
        await ctx.send(embed=embedhelp)

@bot.command(name='support', description="サポートの詳細を表示する")
async def support(ctx):
        embedsupport = discord.Embed(title="AzisabaBot",description="AzisabaBotSupport",color=0xAFDFE4)
        embedsupport.set_thumbnail(url="https://server-icon.minecraft.jp/59b7c551a9b0bd23dc00834d.png?1597177300")
        embedsupport.add_field(name="サポート送信はこちらのチャンネルから",value="<#763333305688522813>",inline=False)
        embedsupport.add_field(name="サポートの送り方はこちらから",value="[クリック](https://azisabaofficial.playing.wiki/d/%a5%b5%a5%dd%a1%bc%a5%c8%bc%f5%c9%d5%a4%d8%a4%ce%cf%a2%cd%ed%ca%fd%cb%a1)",inline=False)
        embedsupport.add_field(name="サポート送る際の注意事項",value="①サポートにて発言をした後運営の対応が終了するまで閉じないでください。\n②サポートでは どこの鯖か、報告内容、どのように対応してほしいか の三つの記入をお願いします。",inline=False)
        await ctx.send(embed=embedsupport)

@bot.command(name='links', description="リンク一覧を表示する")
async def links(ctx):
        embedlinks = discord.Embed(title="AzisabaBot",description="AzisabaBotLinks",color=0xAFDFE4)
        embedlinks.set_thumbnail(url="https://server-icon.minecraft.jp/59b7c551a9b0bd23dc00834d.png?1597177300")
        embedlinks.add_field(name="アジ鯖Minecraftリンク一覧",value="[ホームページ](https://www.azisaba.net/)\n[Japan Minecraft Servers](https://minecraft.jp/servers/azisaba.net)\n[Monocraft](https://monocraft.net/servers/xWBVrf1nqB2P0LxlMm2v)\n[寄付サイト](https://azisaba.buycraft.net/)\n[公式wiki](https://azisabaofficial.playing.wiki/)\n[非公式wiki](https://aziserver.playing.wiki/)",inline=False)
        embedlinks.add_field(name="アジ鯖Minecraft外リンク一覧",value="[Discord](https://discord.gg/azisaba)\n[Twitter](https://twitter.com/AzisabaNetwork)\n[Youtube](https://www.youtube.com/channel/UCHkH9_MKql1MFi0MZ_tqQbg)\n[GitHub](https://github.com/azisaba)",inline=False)
        await ctx.send(embed=embedlinks)

@bot.command(name='vote', description="投票サイトを表示する")
async def vote(ctx):
        embedvote = discord.Embed(title="AzisabaBot",description="AzisabaBotVote",color=0xAFDFE4)
        embedvote.set_thumbnail(url="https://server-icon.minecraft.jp/59b7c551a9b0bd23dc00834d.png?1597177300")
        embedvote.add_field(name="Japan Minecraft Servers",value="[ここをクリック!](https://minecraft.jp/servers/azisaba.net)",inline=False)
        embedvote.add_field(name="Monocraft",value="[ここをクリック!](https://monocraft.net/servers/xWBVrf1nqB2P0LxlMm2v)",inline=False)
        await ctx.send(embed=embedvote)

@bot.command(name='store', description="寄付サイトを表示する")
async def vote(ctx):
        embedbuy = discord.Embed(title="AzisabaBot",description="AzisabaBotStore",color=0xAFDFE4)
        embedbuy.set_thumbnail(url="https://server-icon.minecraft.jp/59b7c551a9b0bd23dc00834d.png?1597177300")
        embedbuy.add_field(name="寄付ページはこちらから",value="[ここをクリック!](https://azisaba.buycraft.net/)")
        await ctx.send(embed=embedbuy)

@bot.command(name='wiki', description="wikiを表示する")
async def vote(ctx):
        embedwiki = discord.Embed(title="AzisabaBot",description="AzisabaBotWiki",color=0xAFDFE4)
        embedwiki.set_thumbnail(url="https://server-icon.minecraft.jp/59b7c551a9b0bd23dc00834d.png?1597177300")
        embedwiki.add_field(name="公式wiki",value="[ここをクリック!](https://azisabaofficial.playing.wiki/)",inline=False)
        embedwiki.add_field(name="非公式wiki",value="[ここをクリック!](https://aziserver.playing.wiki/)",inline=False)
        await ctx.send(embed=embedwiki)

@bot.command(name='color', description="名前に色を付ける")
async def color(ctx, arg):
        user = ctx.author
        guild = ctx.guild
        member = ctx.author
        if arg.startswith('#'):
                arg = arg[1:]
                makerole = await guild.create_role(name="すごい染料",colour=discord.Colour(int(arg, 16)))
                embedcolor = discord.Embed(title="AzisabaBot",description="色を" + arg + "に設定しました。",colour=discord.Colour(int(arg, 16)))
                if "すごい染料" in [role.name for role in user.roles]:
                        role = discord.utils.get(user.roles, name='すごい染料')
                        await user.remove_roles(role)
                        await ctx.send(embed=embedcolor)
                        await member.add_roles(makerole)
                else:
                        await ctx.send(embed=embedcolor)
                        await member.add_roles(makerole)
        else:
                makerole = await guild.create_role(name="すごい染料",colour=discord.Colour(int(arg, 16)))
                embedcolor = discord.Embed(title="AzisabaBot",description="色を" + arg + "に設定しました。",colour=discord.Colour(int(arg, 16)))
                if "すごい染料" in [role.name for role in user.roles]:
                        role = discord.utils.get(user.roles, name='すごい染料')
                        await user.remove_roles(role)
                        await ctx.send(embed=embedcolor)
                        await member.add_roles(makerole)
                else:
                        await ctx.send(embed=embedcolor)
                        await member.add_roles(makerole)


@bot.command(name='colorcheck', description="色を確認する")
async def colorcheck(ctx, arg):
        if arg.startswith('#'):
                arg = arg[1:]
                embedcolor = discord.Embed(title="AzisabaBot",description=arg + "を表示しました。",colour=discord.Colour(int(arg, 16)))
                await ctx.send(embed=embedcolor)
        else:
                embedcolor = discord.Embed(title="AzisabaBot",description=arg + "を表示しました。",colour=discord.Colour(int(arg, 16)))
                await ctx.send(embed=embedcolor)

bot.run(TOKEN)
