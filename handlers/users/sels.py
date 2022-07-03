from aiogram import types
from loader import dp, bot
from aiogram.types import ContentType, Message
from aiogram.dispatcher import FSMContext
from keyboards.inline.inlineKeybords import bar_menu
from states.users_add import user_sels
from keyboards.default.selskey import back, contback, n_back
from keyboards.default.StartKeyborad import menu
import re
from utils.db_api.postgres import send_ex
r_data =r'(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})'

@dp.message_handler(text="◀️Назад")
async def naz(m: types.Message):
    await m.answer("Что вы хотите сделать",reply_markup=menu)

@dp.callback_query_handler(text = "fil1")
async def selss(message :types.CallbackQuery):
    ctr = await n_back(message['from']['first_name'])
    await message.message.answer("Введите полное И.Ф:", reply_markup=ctr)
    await user_sels.full_name.set()

@dp.message_handler(state=user_sels.full_name)
async def name(mes : types.Message ,state = FSMContext):
    if (mes.text == "◀️Назад"):
        await state.finish()
        await mes.answer("Что вы хотите сделать",reply_markup=menu)
    else:
        f_name = mes.text
        async with state.proxy() as data:
            data['f_name'] =f_name
        await mes.answer("Введите номер телефона",reply_markup=contback)
        await user_sels.next()

@dp.message_handler(state=user_sels.numb_phone)
async def cont(mess: types.Message, state = FSMContext):
    if (mess.text == "◀️Назад"):
        await state.finish()
        await mess.answer("Что вы хотите сделать",reply_markup=menu)
    else:
        numb_p = mess.text
        async with state.proxy() as data:
            data["phone"]=numb_p
        await mess.answer("Когда хотите преобрести стрижку",reply_markup=back)
        await user_sels.next()

@dp.message_handler(state=user_sels.numb_phone,content_types=ContentType.CONTACT)
async def cont(mess: types.ContentType, state = FSMContext):
    numb_p = mess.contact.phone_number
    async with state.proxy() as data:
        data["phone"]=numb_p
    await mess.answer("Когда хотите преобрести стрижку (Введите в формате=dd/mm)",reply_markup=back)
    await user_sels.next()

@dp.message_handler(state=user_sels.data)
async def date(mess : types.Message , state = FSMContext):
    if (mess.text == "◀️Назад"):
        await state.finish()
        await mess.answer("Что вы хотите сделать",reply_markup=menu)
    elif re.search(r_data,mess.text):
        async with state.proxy() as data:
            data["data"] = mess.text
        await mess.answer("В какое время суток хотите преобрести стрижку(формат hh:mm)", reply_markup=back)
        await user_sels.next()
    else:
        await mess.answer("Заново введите правильный формат dd/mm/yyyy!!!")

@dp.message_handler(state=user_sels.time)
async def time(m: types.Message ,state = FSMContext):
    dt = m.text
    if (m.text == "◀️Назад"):
        await state.finish()
        await m.answer("Что вы хотите сделать",reply_markup=menu)
    elif ((len(dt)==5)and(int(dt[0]+dt[1])>=8)and(int(dt[0]+dt[1])<=20)and(int(dt[3]+dt[4])<60)):
        async with state.proxy() as data:
            data['time']=dt
        await state.finish()
        send_ex(f"""insert into reg_bar(name,phone,data,time) 
                    values('{data['f_name']}','{data['phone']}','{data['data']}','{data['time']}')
                    returning*""")
        await bot.send_message(chat_id=511172905 , text=f"Имя клиента {data['f_name']}\nТелефон клиента {data['phone']} \nКлиент хочет к вам {data['data']}   в {data['time']} часов")
    else:
        await m.answer("Мы не работаем в этот час!!! , Заново введите время (Формат = HH/MM)")