import asyncio, sys, logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command

API_TOKEN = "your_bot_token"

# Bot va dispatcher obyekti
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Do'stingiz kanalining username va post ID'ni kiriting
FRIEND_CHANNEL_USERNAME = "channel_name"  # @ belgisiz yozing
FRIEND_POST_ID = 'post_id'  # Post ID

@dp.message(CommandStart())
async def start(message: types.Message):
    """Bot start komandasiga javob"""
    await message.reply("Salom! Men siz uchun postlarni ulashaman. 😊")

@dp.message(Command("post"))
async def post_to_channel(message: types.Message):
    """Postni ulashish"""
    post_header = "description 👇"
    post_url = f"https://t.me/{FRIEND_CHANNEL_USERNAME}/{FRIEND_POST_ID}"

    # Inline tugma bilan xabar
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Davomini o'qish", url=post_url)]
    ])

    await bot.send_message(chat_id=message.chat.id, text=post_header, reply_markup=keyboard)

async def main():
    """Botni ishga tushirish"""
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
