from loader import dp
from aiogram import types
from states.transstate import TransState
from aiogram.dispatcher import FSMContext
from keyboards.default.StartKeyborad import languagemenu, shart,menu


@dp.message_handler(text="🇺🇿 Tarjimon")
async def translate(message: types.Message):
    await message.answer("Tanlang", reply_markup=languagemenu)
    await TransState.til.set()
    # til = message.text

@dp.message_handler(state=TransState.til)
async def tillar(message: types.Message, state = FSMContext):
    til = message.text
    await state.update_data(
        {"til": til}
    )
    await message.answer("So'zni yuboring ")
    await TransState.next()

@dp.message_handler(state=TransState.suz)
async def tarjima_qil(message: types.Message, state = FSMContext):
    suzz = message.text
    pyttsx3.speak(suzz)
    await state.update_data(
        {"suz": message.text}
    )
    data = await state.get_data()
    leng = data["til"]
    words = data.get("suz")
    if leng == "En ➡️ Uz":

        try:

            translator = Translator(from_lang="en", to_lang="uz")
            translation = translator.translate(words)
        except:
            await message.reply("Suz topilmadi ")
        else:
            await message.reply(translation)
    elif leng == 'Uz ➡️ En':
        try:

            translator = Translator(from_lang="uz", to_lang="en")
            translation = translator.translate(words)
        except:
            await message.reply("Suz topilmadi ")
        else:
            await message.reply(translation)
    else:
        try:

            translator = Translator(to_lang="en")
            translation = translator.translate(words)
        except:
            await message.reply("Suz topilmadi ")
        else:
            await message.reply(translation)
    await message.answer("yana so'z tarjima qilasizmi tanlang", reply_markup=shart)
    await TransState.next()
@dp.message_handler(state=TransState.shart)
async def shrttecshirish(message: types.Message, state=FSMContext):
    if message.text == "No":
        await message.answer("Xayir!!!", reply_markup=menu)
        await state.finish()
    elif message.text == "Yes":
        await message.answer("Marxamat tilni tanlang",reply_markup=languagemenu)
        await TransState.til.set()
    else:
        await message.reply("Bunday kamanda mavjud emas Xayir!!!", reply_markup=menu)
        await state.finish()
