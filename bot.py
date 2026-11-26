import os
from twitchio.ext import commands


class Bot(commands.Bot):

  def __init__(self):
    super().__init__(
        token=os.environ['TMI_TOKEN'],
        prefix='!',
        initial_channels=[os.environ['CHANNEL']],
    )

  async def event_ready(self):
    print(f'Бот {self.nick} успешно зашел на канал!')


bot = Bot()
bot.run()
