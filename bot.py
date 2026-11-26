import asyncio
import os
from aiohttp import web
from twitchio.ext import commands

# Читаем каналы из переменной CHANNELS и превращаем в список
raw_channels = os.environ.get('CHANNELS', '')
channel_list = [c.strip().lower() for c in raw_channels.split(',') if c.strip()]


class Bot(commands.Bot):

  def __init__(self):
    super().__init__(
        token=os.environ['TMI_TOKEN'],
        prefix='!',
        initial_channels=channel_list,
    )

  async def event_ready(self):
    print(f'Бот {self.nick} успешно зашел на каналы: {", ".join(channel_list)}')


# Мини-сервер для Render, чтобы сервис не падал по таймауту
async def handle(request):
  return web.Response(text=f'Бот в сети на каналах: {", ".join(channel_list)}')


async def main():
  app = web.Application()
  app.router.add_get('/', handle)
  runner = web.AppRunner(app)
  await runner.setup()

  port = int(os.environ.get('PORT', 8080))
  site = web.TCPSite(runner, '0.0.0.0', port)
  await site.start()

  bot = Bot()
  await bot.start()


asyncio.run(main())
