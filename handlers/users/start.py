from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from aiogram.dispatcher import FSMContext
from keyboards.default.StartKeyborad import menu

from loader import dp , bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name} tarjimon botga xush kelibsiz!",reply_markup=menu)
    await bot.send_message(chat_id=511172905, text=f"{message}")