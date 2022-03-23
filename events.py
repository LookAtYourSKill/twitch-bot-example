import twitchio
from twitchio.ext import commands

class events(commands.Cog):
    def __init__(
        self,
        bot
    ):
        self.bot = bot

    @commands.Cog.event()
    async def event_ready(self):
        print(
            f'Logged in as | {self.bot.nick}'
        )
        print(
            f'User id is   | {self.bot.user_id}'
        )

    @commands.Cog.event()
    async def event_message(
        self,
        message
    ):
        print(message.content)


def prepare(bot):
    bot.add_cog(events(bot))
