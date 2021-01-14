from discord.ext import commands
import discord



class Commands(commands.Cog, name="Commands"):
    def __init__(self, bot):
        self.bot = bot

    def cog_check(self, ctx):
        if ctx.guild is None:
            return False
        return True


    @commands.command()
    async def ping(self, ctx):
        """What's the latency/ping of the bot?"""
        pong = discord.Embed(title=f"Pong! {round(self.bot.latency * 1000)}ms")
        pong.set_footer(text=f"Requested by: {ctx.author.display_name}")
        return await ctx.send(embed=pong)

    @commands.command()
    async def creator(ctx):
        """What's vishank's github?"""
        github = discord.Embed(title="Vishank's Github:", description="https://github.com/VishankSingh")
        await ctx.send(embed=github)

    @commands.command()
    async def source(self, ctx):
        """Source code"""
        source = discord.embed(title="Source repository", description="https://github.com/VishankSingh")
        await ctx.send(embed=source)

#    @commands.command() 
#    async def invite(self, ctx):
#        invitelinknew = await ctx.channel.create_invite(max_age = 300)
#        embedMsg=discord.Embed(color=0xa36cdd)
#        embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
#        embedMsg.set_footer(text="Discord server invited link.")
#        await ctx.send(embed=embedMsg)

    
    @commands.command()
    async def invite(self, ctx):
        """Gives you the invite link for the bot"""
        link = discord.utils.oauth_url(self.bot.user.id, permissions=discord.Permissions(SEND_MESSAGES = True, 
                                                                                         MANAGE_MESSAGES = True,
                                                                                         EMBED_LINKS = True,
                                                                                         READ_MESSAGE_HISTORY = True, 
                                                                                         MANAGE_EMOJIS = True))                                                              
        embed = discord.Embed(description=f"[**Invite Link**]({link})",
                     color=0x78C7DB)
        await ctx.send(embed=embed)

    


def setup(bot):
    bot.add_cog(Commands(bot=bot))


    

