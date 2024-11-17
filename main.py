import asyncio, sys, logging

import handlers
from loader import bot, dp

async def main():
    """Botni ishga tushirish"""
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
