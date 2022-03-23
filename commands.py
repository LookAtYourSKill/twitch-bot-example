from twitchio.ext import commands


class testCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')


def prepare(bot):
    bot.add_cog(testCommands(bot))
