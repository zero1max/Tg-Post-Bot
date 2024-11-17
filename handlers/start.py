from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from loader import dp, bot

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