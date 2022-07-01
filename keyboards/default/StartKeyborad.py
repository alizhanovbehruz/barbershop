from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

con = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона",request_contact=True)
        ]
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💈Записаться на стрижку💈")
        ],
        [
            KeyboardButton(text="📍Локация филлиалов📍")
        ]
    ],
    resize_keyboard=True

)

languagemenu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="En ➡️ Uz"),
            KeyboardButton(text="Uz ➡️ En")
        ],
    ],
    resize_keyboard=True
)

shart = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Yes")
        ],
        [
            KeyboardButton(text="No")
        ],
    ],
    resize_keyboard=True
)