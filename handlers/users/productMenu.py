from aiogram import types
from loader import dp
from aiogram.types import ContentType
from keyboards.default.StartKeyborad import con
from keyboards.inline.inlineKeybords import inlinemenu, bar_menu

@dp.message_handler(text="💈Записаться на стрижку💈")
async def products(message: types.Message):
    await message.answer("Где хотите преобрести стрижку", reply_markup=bar_menu)

# @dp.message_handler(text="📍Локация филлиалов📍")
# async def loc(m: types.Message):
#     await m.answer("bjhjkb", reply_markup=con)

@dp.message_handler(content_types=ContentType.CONTACT)
async def con(m: types.ContentType):
    await m.answer(m.contact.phone_number)

