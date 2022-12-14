
from datetime               import datetime
from discord.ext            import tasks
from discord.ext.commands   import Cog


class Loop(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_name = 'report'
        self.channel_ids  = []

    @Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            found = False

            for channel in guild.text_channels:
                if channel.name == self.channel_name:
                    self.channel_ids += [ channel.id ]
                    found = True
                    break

            if not found:
                channel = await guild.create_text_channel(self.channel_name)
                self.channel_ids += [ channel.id ]

        self.every_second.start()

    @tasks.loop(seconds = 1)
    async def every_second(self):
        for channel_id in self.channel_ids:
            await self.bot.get_channel(channel_id).send(f'[{datetime.now()}] pong!')


async def setup(bot):
    await bot.add_cog(Loop(bot))
