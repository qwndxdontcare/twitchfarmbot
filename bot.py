import asyncio
import os
from aiohttp import web
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


async def handle(request):
  return web.Response(text='Бот работает!')


async def main():
  # Запускаем мини-сайт для Render
  app = web.Application()
  app.router.add_get('/', handle)
  runner = web.AppRunner(app)
  await runner.setup()
  port = int(os.environ.get('PORT', 8080))
  site = web.TCPSite(runner, '0.0.0.0', port)
  await site.start()

  # Запускаем самого бота
  bot = Bot()
  await bot.start()


asyncio.run(main())
